"""Machine Reverse. Narration (Piper, one call per sentence so timings are exact) -> fast-cut photo scenes (ffmpeg)
-> "Why does this exist?" scenes with a red arrow on the part
-> captions burned in LAST, timed from the real audio. Outputs video, preview, frames, .srt, chapters."""
import json, sys, pathlib, subprocess, wave, re, os
from concurrent.futures import ThreadPoolExecutor

W, H, FPS = 1920, 1080, 30
MODEL = os.environ.get("PIPER_MODEL", "voices/en_US-ryan-high.onnx")
SCALE = os.environ.get("PIPER_LENGTH_SCALE", "1.2")  # >1 slows the voice to a documentary pace
GAP, TAIL = 0.18, 0.35  # silence between sentences / at the end of a scene


def run(*a, **k):
    subprocess.run(a, check=True, **k)


def piper(text, wav):
    for flag in ("--length-scale", "--length_scale"):
        try:
            run("piper", "--model", MODEL, flag, SCALE, "--output_file", str(wav), input=text.encode()); return
        except subprocess.CalledProcessError:
            continue
    run("piper", "--model", MODEL, "--output_file", str(wav), input=text.encode())


def probe(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                                capture_output=True, text=True, check=True).stdout)


def ts(t):
    h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f"{int(h):02}:{int(m):02}:{int(s):02},{int((s % 1) * 1000):03}"


def sentences(text):
    return [x.strip() for x in re.findall(r"[^.?!]+[.?!]+|[^.?!]+$", text) if x.strip()]


def chunks(text, n=7):
    """Caption chunks that end at punctuation when possible, at most n words."""
    out, cur = [], []
    for w in text.split():
        cur.append(w)
        if len(cur) >= n or (w[-1] in ".,?!:" and len(cur) >= 3):
            out.append(" ".join(cur)); cur = []
    if cur:
        out.append(" ".join(cur))
    return out


def tts_scene(job):
    """One wav per sentence, joined with fixed gaps. Returns the exact start/end of every sentence."""
    i, s, out = job
    spans, frames, rate, t = [], [], None, 0.0
    for k, sent in enumerate(sentences(s["text"])):
        wav = out / f"{i}_{k}.wav"
        piper(sent, wav)
        with wave.open(str(wav)) as w:
            rate, params = w.getframerate(), w.getparams()
            data = w.readframes(w.getnframes()); n = w.getnframes()
        spans.append((sent, t, t + n / rate)); frames.append(data)
        pad = TAIL if k == len(sentences(s["text"])) - 1 else GAP
        frames.append(b"\x00" * int(pad * rate) * params.sampwidth * params.nchannels)
        t += n / rate + pad
    with wave.open(str(out / f"{i}.wav"), "wb") as w:
        w.setparams(params); w.writeframes(b"".join(frames))
    return {"dur": t, "spans": spans}


ARROW = pathlib.Path("voices/arrow.png")  # generated once per run, next to the voice model


def make_arrow():
    """Thick red arrow with a white outline, tip at the bottom-right corner of a 300x300 canvas."""
    if ARROW.exists():
        return
    from PIL import Image, ImageDraw
    big = 4
    im = Image.new("RGBA", (300 * big, 300 * big), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    # arrow drawn pointing right, then rotated 45 degrees so it points down-right
    pts = [(20, 115), (175, 115), (175, 60), (285, 150), (175, 240), (175, 185), (20, 185)]
    pts = [(x * big, y * big) for x, y in pts]
    d.polygon(pts, fill=(255, 255, 255, 255))
    inner = [(30, 127), (187, 127), (187, 86), (267, 150), (187, 214), (187, 173), (30, 173)]
    d.polygon([(x * big, y * big) for x, y in inner], fill=(225, 16, 30, 255))
    im = im.rotate(-45, resample=Image.BICUBIC, expand=True)
    bbox = im.getbbox(); im = im.crop(bbox).resize((260, 260), Image.LANCZOS)
    ARROW.parent.mkdir(exist_ok=True); im.save(ARROW)


def arrow_target(s):
    a = s.get("arrow")
    if not a:
        return None
    if a is True:
        return 0.5, 0.5
    return float(a.get("x", 0.5)), float(a.get("y", 0.5))


def render_scene(job):
    i, s, d, out, dur = job
    imgs = sorted((d / "media").glob(f"{i}_*.jpg"), key=lambda p: int(p.stem.split("_")[1]))
    total = int(dur * FPS) + 1
    n = len(imgs); base = total // n
    cap = s["caption"].replace("'", "").replace(":", " -")
    target = arrow_target(s)
    if target:
        # "Why does this exist?" scene: big yellow question centered at the top instead of the red tag
        label = (f"drawtext=text='{cap}':fontcolor=0xFFD400:fontsize=78:borderw=7:bordercolor=black:"
                 f"x=(w-text_w)/2:y=70")
    else:
        label = (f"drawtext=text='{cap}':fontcolor=white:fontsize=56:borderw=4:bordercolor=black:"
                 f"box=1:boxcolor=0xC8102E@0.9:boxborderw=18:x=60:y=60")
    parts = []
    for k, img in enumerate(imgs):
        f = base + (total - base * n if k == n - 1 else 0)
        part = out / f"{i}_{k}.mp4"
        fill = "scale=2880:1620:force_original_aspect_ratio=increase,crop=2880:1620"
        if target and k == 0:
            # slow zoom INTO the pointed part: the point stays fixed on screen, so the arrow stays on it
            tx, ty = target
            zoom = (f"zoompan=z='1+0.0008*on':x='{tx}*iw*(1-1/zoom)':y='{ty}*ih*(1-1/zoom)'"
                    f":d={f}:s={W}x{H}:fps={FPS}")
            # arrow tip on the target, coming from the upper-left (flipped when the part is near that edge)
            ax, ay = int(tx * W), int(ty * H)
            hflip = tx < 0.25; vflip = ty < 0.3
            ox = f"{ax}-8" if hflip else f"{ax}-w+8"
            oy = f"{ay}-8" if vflip else f"{ay}-h+8"
            bounce = "18*sin(2*PI*t*1.6)"
            ox = f"{ox}{'+' if hflip else '-'}{bounce}"; oy = f"{oy}{'+' if vflip else '-'}{bounce}"
            flips = ",".join(x for x in ["hflip" if hflip else "", "vflip" if vflip else ""] if x) or "null"
            graph = (f"[0:v]{fill},{zoom},format=yuv420p[bg];[1:v]{flips}[ar];"
                     f"[bg][ar]overlay=x='{ox}':y='{oy}':shortest=1,{label},format=yuv420p[v]")
            run("ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", str(img), "-loop", "1", "-i", str(ARROW),
                "-filter_complex", graph, "-map", "[v]", "-frames:v", str(f),
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-r", str(FPS), "-an", str(part))
        else:
            # alternate zoom in / zoom out so consecutive cuts never look the same
            z = f"1+0.0006*on" if k % 2 == 0 else f"1.18-0.0006*on"
            zoom = f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={f}:s={W}x{H}:fps={FPS}"
            flash = ",fade=t=in:st=0:d=0.12:color=white" if i < 4 and k > 0 else ""  # hook: flash on every cut
            run("ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", str(img),
                "-vf", f"{fill},{zoom}{flash},{label},format=yuv420p", "-frames:v", str(f),
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-r", str(FPS), "-an", str(part))
        parts.append(part)
    (out / f"{i}_list.txt").write_text("".join(f"file '{p.name}'\n" for p in parts))
    vid = out / f"{i}_v.mp4"
    run("ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(out / f"{i}_list.txt"), "-c", "copy", str(vid))
    run("ffmpeg", "-y", "-loglevel", "error", "-i", str(vid), "-i", str(out / f"{i}.wav"),
        "-c:v", "copy", "-c:a", "aac", "-shortest", str(out / f"{i}.mp4"))


def main(video):
    d = pathlib.Path("videos") / video
    out = d / "out"; out.mkdir(exist_ok=True)
    _sj = json.loads((d / "script.json").read_text())
    scenes = _sj["scenes"]
    global SCALE
    SCALE = str(_sj.get("length_scale", SCALE))
    with ThreadPoolExecutor(4) as ex:
        tts = list(ex.map(tts_scene, [(i, s, out) for i, s in enumerate(scenes)]))
    make_arrow()
    with ThreadPoolExecutor(4) as ex:
        list(ex.map(render_scene, [(i, s, d, out, t["dur"]) for i, (s, t) in enumerate(zip(scenes, tts))]))
    # Captions come LAST and are timed from the audio that is really in the video:
    # scene start = sum of the measured scene lengths, sentence offsets = measured TTS durations.
    srt, chapters, t0, timeline = [], [], 0.0, []
    for i, (s, t) in enumerate(zip(scenes, tts)):
        if s.get("chapter"):
            chapters.append(f"{int(t0//60)}:{int(t0%60):02d} {s['chapter']}")
        for sent, a, b in t["spans"]:
            cs = chunks(sent); chars = sum(len(c) for c in cs); pos = a
            for c in cs:
                end = pos + (b - a) * len(c) / chars
                srt.append(f"{len(srt)+1}\n{ts(t0 + pos)} --> {ts(t0 + end)}\n{c}\n"); pos = end
        dur = probe(out / f"{i}.mp4")
        timeline.append({"scene": i, "start": t0, "dur": dur, "chapter": s.get("chapter"), "caption": s["caption"],
                         "arrow": arrow_target(s), "short": s.get("short")})
        t0 += dur
    (out / "list.txt").write_text("".join(f"file '{i}.mp4'\n" for i in range(len(scenes))))
    (out / "captions.srt").write_text("\n".join(srt))
    (out / "timeline.json").write_text(json.dumps(timeline))
    (out / "chapters.txt").write_text("\n".join(chapters) + "\n")
    nocap = out / "nocaps.mp4"
    run("ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(out / "list.txt"), "-c", "copy", str(nocap))
    style = "FontName=DejaVu Sans,Bold=1,FontSize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=3,Alignment=2,MarginV=40"
    final = out / f"{video}.mp4"
    run("ffmpeg", "-y", "-loglevel", "error", "-i", str(nocap), "-vf", f"subtitles={out/'captions.srt'}:force_style='{style}'",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "26", "-maxrate", "2500k", "-bufsize", "5000k",
        "-c:a", "aac", "-b:a", "96k", str(final))
    run("ffmpeg", "-y", "-loglevel", "error", "-i", str(final), "-vf", "scale=640:360", "-c:v", "libx264", "-preset", "veryfast",
        "-b:v", "250k", "-c:a", "aac", "-b:a", "48k", str(out / "preview.mp4"))
    total = probe(final)
    for k, t in enumerate([8, 25, 45, total * 0.25, total * 0.5, total * 0.75, total - 20]):
        run("ffmpeg", "-y", "-loglevel", "error", "-ss", f"{t:.1f}", "-i", str(final), "-frames:v", "1", "-vf", "scale=960:-1", str(out / f"frame{k}.jpg"))
    print("done", final, f"{total/60:.1f} min, captions {len(srt)}")


if __name__ == "__main__":
    main(sys.argv[1])
