"""Cut vertical Shorts (one per "Why does this exist?" part) (9:16, under 60 s) out of a rendered long video.
Uses the caption-free master (nocaps.mp4) and the timeline written by build.py, then burns the
subtitles last, re-timed to each Short, so captions stay in sync with the audio."""
import json, pathlib, re, subprocess, sys

MAX = 58.0   # seconds per Short


def run(*a):
    subprocess.run(a, check=True)


def ts(t):
    h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f"{int(h):02}:{int(m):02}:{int(s):02},{int((s % 1) * 1000):03}"


def tsec(x):
    h, m, s = x.replace(",", ".").split(":"); return int(h) * 3600 + int(m) * 60 + float(s)


def windows(tl):
    """One Short per "Why does this exist?" scene: it starts on the arrow and runs through the
    following scenes (the answer) until the next part begins or MAX is reached.
    Videos without arrow scenes fall back to the hook plus 4 evenly spaced chapters."""
    starts = [t["scene"] for t in tl if t.get("arrow")]
    if not starts:
        ch = [t["scene"] for t in tl if t["chapter"] and t["scene"] > 0]
        mid = ch[:-1] or ch
        starts = [0] + ([mid[round(k * (len(mid) - 1) / 3)] for k in range(4)] if len(mid) >= 4 else mid[:4])
    out = []
    for a in starts:
        group, tot = [], 0.0
        for t in tl[a:]:
            if group and (tot + t["dur"] > MAX or t.get("arrow")): break
            group.append(t); tot += t["dur"]
        out.append(group)
    return out


def main(video):
    d = pathlib.Path("videos") / video / "out"
    tl = json.loads((d / "timeline.json").read_text())
    caps = [m for m in re.findall(r"(\d+)\n(\S+) --> (\S+)\n(.*?)(?:\n\n|\Z)", (d / "captions.srt").read_text(), re.S)]
    sd = d / "shorts"; sd.mkdir(exist_ok=True)
    meta = []
    for n, group in enumerate(windows(tl), 1):
        a = group[0]["start"]; b = group[-1]["start"] + group[-1]["dur"]
        lines = []
        for _, s0, s1, txt in caps:
            x, y = tsec(s0), tsec(s1)
            if y > a and x < b:
                lines.append(f"{len(lines)+1}\n{ts(max(x, a) - a)} --> {ts(min(y, b) - a)}\n{txt}\n")
        srt = sd / f"short{n}.srt"; srt.write_text("\n".join(lines))
        style = ("FontName=DejaVu Sans,Bold=1,FontSize=13,PrimaryColour=&H0000FFFF,OutlineColour=&H00000000,"
                 "BorderStyle=1,Outline=3,Alignment=2,MarginV=60")
        q = group[0]["caption"].replace("'", "").replace(":", " -") if group[0].get("arrow") else ""
        size = 72 if len(q) <= 22 else 58
        question = (f"drawtext=text='{q}':fontcolor=0xFFD400:fontsize={size}:borderw=6:bordercolor=black:"
                    f"x=(w-text_w)/2:y=480," if q else "")
        # the whole 16:9 frame (arrow + question) over a blurred 9:16 copy of itself, so nothing is cropped away
        vf = (f"split[a][b];[a]scale=-2:1920,crop=1080:1920,boxblur=24:2,eq=brightness=-0.12[bg];"
              f"[b]scale=1080:-2[fg];[bg][fg]overlay=0:(H-h)/2,"
              f"drawtext=text='MACHINE REVERSE':fontcolor=white:fontsize=64:borderw=4:bordercolor=black:"
              f"box=1:boxcolor=0xC8102E@0.9:boxborderw=18:x=(w-text_w)/2:y=170,"
              f"{question}"
              f"subtitles={srt}:force_style='{style}'")
        run("ffmpeg", "-y", "-loglevel", "error", "-ss", f"{a:.2f}", "-t", f"{b-a:.2f}", "-i", str(d / "nocaps.mp4"),
            "-filter_complex", vf, "-c:v", "libx264", "-preset", "veryfast", "-crf", "26", "-maxrate", "3000k", "-bufsize", "6000k",
            "-c:a", "aac", "-b:a", "96k", str(sd / f"short{n}.mp4"))
        title = group[0].get("short") or re.sub(r"^\d+\.\s*", "", group[0]["chapter"] or "") or group[0]["caption"].title()
        meta.append(f"short{n}.mp4 ({b-a:.0f}s)\nTitle: {title} #Shorts\n"
                    f"Description: Why does this exist? The full story is on the Machine Reverse channel.\n")
    (sd / "shorts.md").write_text("\n".join(meta))
    print("shorts done", len(meta))


if __name__ == "__main__":
    main(sys.argv[1])
