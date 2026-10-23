"""Download real photos per scene from Wikimedia Commons (several per scene for fast cuts) and record license/credit."""
import json, sys, time, pathlib, requests

API = "https://commons.wikimedia.org/w/api.php"
HEADERS = {"User-Agent": "machine-reverse-channel/1.0 (github.com/viniciushoscher-ctrl/machine-reverse)"}
_cache = {}


def api_pages(params):
    """Wikimedia rate-limits bursts; retry with backoff and cache identical searches."""
    key = json.dumps(params, sort_keys=True)
    if key in _cache:
        return _cache[key]
    for attempt in range(8):
        time.sleep(1.5)
        r = requests.get(API, params=params, headers=HEADERS, timeout=60)
        if r.status_code == 200:
            try:
                pages = r.json().get("query", {}).get("pages", {})
                _cache[key] = pages
                return pages
            except ValueError:
                pass
        time.sleep(5 * (attempt + 1))
    raise SystemExit(f"Commons API kept failing for {params['gsrsearch']}")


def download(url, fatal=True):
    url = url.split("?")[0]  # Commons appends tracking params to unscaled originals; the bare URL is the file
    for attempt in range(8):
        r = requests.get(url, headers=HEADERS, timeout=120)
        if r.status_code == 200:
            return r.content
        print("download", r.status_code, url)
        wait = r.headers.get("Retry-After", "")  # upload.wikimedia.org answers 429 to bursts
        time.sleep(int(wait) if wait.isdigit() else 5 * (attempt + 1))
    if fatal:
        raise SystemExit(f"download failed: {url}")
    return None


def pick(query, used):
    params = {
        "action": "query", "format": "json", "generator": "search",
        "gsrsearch": f"{query} filetype:bitmap", "gsrnamespace": 6, "gsrlimit": 30,
        "prop": "imageinfo", "iiprop": "url|size|mime|extmetadata", "iiurlwidth": 1920,
    }
    pages = api_pages(params)
    for p in sorted(pages.values(), key=lambda x: x.get("index", 0)):
        info = (p.get("imageinfo") or [{}])[0]
        if info.get("mime") != "image/jpeg" or info.get("width", 0) < 2000:
            continue
        if info["width"] < info.get("height", 0) * 1.3 or p["title"] in used:
            continue
        meta = info.get("extmetadata", {})
        lic = meta.get("LicenseShortName", {}).get("value", "")
        if not lic.startswith(("CC", "Public domain", "PD")):
            continue
        artist = meta.get("Artist", {}).get("value", "unknown")
        return {"title": p["title"], "url": info["thumburl"], "page": info["descriptionurl"],
                "license": lic, "artist": artist}
    return None


def exact(title):
    """A specific Commons file chosen for an arrow scene (so the arrow position is known)."""
    title = title if title.startswith("File:") else "File:" + title
    pages = api_pages({"action": "query", "format": "json", "titles": title, "prop": "imageinfo",
                       "iiprop": "url|size|mime|extmetadata", "iiurlwidth": 1920, "gsrsearch": title})
    for p in pages.values():
        info = (p.get("imageinfo") or [{}])[0]
        if not info.get("url"):
            return None
        meta = info.get("extmetadata", {})
        return {"title": p["title"], "url": info.get("thumburl") or info["url"], "original": info["url"],
                "page": info["descriptionurl"],
                "license": meta.get("LicenseShortName", {}).get("value", ""),
                "artist": meta.get("Artist", {}).get("value", "unknown")}
    return None


def main(video):
    d = pathlib.Path("videos") / video
    script = json.loads((d / "script.json").read_text())
    (d / "media").mkdir(exist_ok=True)
    used, credits, last = set(), [], None
    for i, s in enumerate(script["scenes"]):
        for k in range(s.get("cuts", 2)):
            f = d / "media" / f"{i}_{k}.jpg"
            q = s["query"]
            if k == 0 and s.get("local"):  # our own diagram from assets/, no credit needed
                f.write_bytes(pathlib.Path(s["local"]).read_bytes()); last = f; print(i, k, s["local"]); continue
            m = exact(s["file"]) if k == 0 and s.get("file") else None
            data = download(m["url"], fatal=False) if m else None
            for retry in range(3):  # the arrow only fits the chosen photo, so try hard before giving up on it
                if data is not None or not (k == 0 and s.get("file")):
                    break
                print(i, k, "exact photo retry", retry); time.sleep(60)
                m = m or exact(s["file"])
                data = download(m["url"] if retry % 2 else m["original"], fatal=False) if m else None
            if m and data is None:  # the chosen photo would not download: fall back to a search rather than fail
                print(i, k, "exact photo failed, searching instead"); m = None
            if m is None:
                m = pick(q, used)
            while m is None and len(q.split()) > 2:  # query too narrow: drop the last word and retry
                q = " ".join(q.split()[:-1]); m = pick(q, used)
            if m is None:  # search exhausted: reuse the last photo rather than fail the whole video
                if last is None: raise SystemExit("no photo found for scene %d: %s" % (i, s["query"]))
                f.write_bytes(last.read_bytes()); print(i, k, "reuse"); continue
            used.add(m["title"])
            f.write_bytes(data if data is not None else download(m["url"])); data = None; last = f
            credits.append({**m, "scene": i, "cut": k})
            print(i, k, m["title"], m["license"])
    (d / "credits.json").write_text(json.dumps(credits, indent=2))


if __name__ == "__main__":
    main(sys.argv[1])
