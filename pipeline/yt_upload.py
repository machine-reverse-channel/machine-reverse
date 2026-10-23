"""Upload and schedule Machine Reverse videos on YouTube following agendamento/calendar.json.
usage: yt_upload.py check | upload
Secrets: YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN. Optional: EBOOK_URL, YT_BUDGET (quota units per run)."""
import datetime as dt, json, os, subprocess, sys, pathlib, requests
from zoneinfo import ZoneInfo

STATE = pathlib.Path("agendamento/youtube-state.json")
COST_UPLOAD, COST_THUMB = 1600, 50
# New York times (the audience's clock, daylight saving handled by zoneinfo): long 6 pm, Shorts 3 pm and 9 pm.
# A calendar day can override them with "times": ["18:00", "19:00", "21:00"] (long, short 1, short 2).
NY = ZoneInfo("America/New_York")
SLOTS_NY = ["18:00", "15:00", "21:00"]


def token():
    r = requests.post("https://oauth2.googleapis.com/token", data={
        "client_id": os.environ["YT_CLIENT_ID"].strip(), "client_secret": os.environ["YT_CLIENT_SECRET"].strip(),
        "refresh_token": os.environ["YT_REFRESH_TOKEN"].strip(), "grant_type": "refresh_token"}, timeout=30)
    if not r.ok:
        sys.exit(f"token refresh failed: {r.status_code} {r.text}")
    return r.json()["access_token"]


def queue():
    """Every upload in calendar order: (key, video, file, publishAt, title, description, is_long)."""
    cal = json.load(open("agendamento/calendar.json")); ebook = os.environ.get("EBOOK_URL") or "[LINK HERE]"
    for day in cal:
        items = [("long", day.get("long"), None)] + [("short", v, s) for v, s in day.get("shorts", [])]
        times = day.get("times") or SLOTS_NY
        for slot, (kind, v, s) in enumerate(items):
            if not v: continue
            mf = pathlib.Path(f"agendamento/meta/video{v:02d}.json")
            if not mf.exists(): print("not ready yet:", mf); continue
            m = json.loads(mf.read_text())
            hh, mm = map(int, times[min(slot, len(times) - 1)].split(":"))
            at = dt.datetime.fromisoformat(day["date"]).replace(hour=hh, minute=mm, tzinfo=NY).astimezone(dt.timezone.utc)
            if kind == "long":
                yield f"v{v:02d}", v, f"video{v:02d}.mp4", at, m["title"], m["description"].replace("[LINK HERE]", ebook), True
            else:
                sm = next((x for x in m["shorts"] if x["file"] == f"short{s}.mp4"), None)
                if not sm: continue
                yield f"v{v:02d}-s{s}", v, sm["file"], at, sm["title"], sm["description"].replace("[LINK HERE]", ebook), False


def queue_lote():
    """Long videos 01-10 only, on the dates in agendamento/lote-01-10/longs.json (13:00 Brasilia = 16:00 UTC)."""
    ebook = os.environ.get("EBOOK_URL") or "[LINK HERE]"
    for n, day in json.load(open("agendamento/lote-01-10/longs.json")).items():
        v = int(n); m = json.load(open(f"agendamento/meta/video{n}.json"))
        at = dt.datetime.fromisoformat(day).replace(tzinfo=dt.timezone.utc) + dt.timedelta(hours=16)
        yield f"v{n}", v, f"video{n}.mp4", at, m["title"], m["description"].replace("[LINK HERE]", ebook), True


def upload(tok, path, title, desc, tags, at):
    body = {"snippet": {"title": title, "description": desc, "tags": tags, "categoryId": "28",
                        "defaultLanguage": "en", "defaultAudioLanguage": "en"},
            "status": {"privacyStatus": "private", "publishAt": at.strftime("%Y-%m-%dT%H:%M:%SZ"),
                       "selfDeclaredMadeForKids": False, "embeddable": True}}
    h = {"Authorization": f"Bearer {tok}", "X-Upload-Content-Type": "video/mp4",
         "X-Upload-Content-Length": str(path.stat().st_size)}
    r = requests.post("https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status",
                      headers=h, json=body, timeout=60)
    if r.status_code == 403 and "quota" in r.text.lower(): return "QUOTA"
    r.raise_for_status()
    with open(path, "rb") as f:
        u = requests.put(r.headers["Location"], data=f, headers={"Authorization": f"Bearer {tok}", "Content-Type": "video/mp4"}, timeout=3600)
    u.raise_for_status(); return u.json()["id"]


def main(mode):
    tok = token()
    if mode == "check":
        r = requests.get("https://www.googleapis.com/youtube/v3/channels?part=snippet,status&mine=true",
                         headers={"Authorization": f"Bearer {tok}"}, timeout=30); r.raise_for_status()
        lines = [f"channel: {c['snippet']['title']} {c['id']} {c.get('status', {})}" for c in r.json().get("items", [])]
        print("\n".join(lines) or "no channel on this account")
        open("agendamento/youtube-check.txt", "w").write("\n".join(lines) or "no channel on this account")
        return
    if mode == "status":
        ids = ",".join(x["id"] for x in json.loads(STATE.read_text()).values() if "id" in x)
        r = requests.get("https://www.googleapis.com/youtube/v3/videos", params={"part": "status", "id": ids},
                         headers={"Authorization": f"Bearer {tok}"}, timeout=30); r.raise_for_status()
        for v in r.json()["items"]: print(v["id"], v["status"])
        return
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    lote = mode == "lote"
    budget = int(os.environ.get("YT_BUDGET") or 9900)
    now = dt.datetime.now(dt.timezone.utc); dl = pathlib.Path("/tmp/dl"); dl.mkdir(exist_ok=True)
    for key, v, fname, at, title, desc, is_long in (queue_lote() if lote else queue()):
        if key in state: continue
        if not is_long and os.environ.get("YT_SHORTS") != "1": continue  # Shorts are scheduled by hand
        if at < now + dt.timedelta(minutes=45):
            print("skip (slot already passed):", key, at); state[key] = {"skipped": "slot passed"}; continue
        if budget < COST_UPLOAD + (COST_THUMB if is_long else 0): break
        f = dl / f"{v:02d}-{fname}"
        if not f.exists():
            subprocess.run(["gh", "release", "download", f"video{v:02d}", "-p", fname, "-O", str(f), "--clobber"], check=True)
        tags = json.load(open(f"agendamento/meta/video{v:02d}.json"))["tags"] + ([] if is_long else ["Shorts"])
        vid = upload(tok, f, title, desc, tags, at)
        if vid == "QUOTA": print("quota exhausted"); break
        budget -= COST_UPLOAD; state[key] = {"id": vid, "publishAt": at.isoformat()}
        print("uploaded", key, vid, "publishes", at.isoformat())
        thumb = pathlib.Path(f"agendamento/thumbs/video{v:02d}.jpg")
        if is_long and thumb.exists():
            t = requests.post(f"https://www.googleapis.com/upload/youtube/v3/thumbnails/set?videoId={vid}",
                              headers={"Authorization": f"Bearer {tok}", "Content-Type": "image/jpeg"}, data=thumb.read_bytes(), timeout=120)
            print("thumbnail", t.status_code, t.text[:200]); budget -= COST_THUMB
        f.unlink(missing_ok=True)
        STATE.write_text(json.dumps(state, indent=1))
    STATE.write_text(json.dumps(state, indent=1))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "check")
