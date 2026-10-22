"""Build the YouTube description for one video: intro, chapters, sources and photo credits.
usage: make_desc.py videoNN <folder with chapters.txt and credits.json>"""
import html, json, os, re, sys

v, d = sys.argv[1], sys.argv[2]
sj = json.load(open(f"videos/{v}/script.json"))
ch = open(f"{d}/chapters.txt").read().strip()
cr = json.load(open(f"{d}/credits.json"))
intro = sj["scenes"][0]["text"]
sf = f"videos/{v}/sources.txt"
src = open(sf).read().strip() if os.path.exists(sf) else ""
seen, lines = set(), []
for c in cr:
    t = c["title"].replace("File:", "")
    if t in seen: continue
    seen.add(t)
    a = html.unescape(re.sub("<[^>]+>", "", c.get("artist", "") or "")).strip()
    lines.append(f"- {t} by {a or 'unknown'}, {c.get('license', '')}")
out = f"""# {v}: delivery (Machine Reverse)

**Title:** {sj['title']}

## Description (paste on YouTube)
{intro}

Chapters:
{ch}

Sources:
{src}

Photos from Wikimedia Commons (credits):
""" + "\n".join(lines) + "\n"
open(f"{d}/titulo-e-descricao.md", "w").write(out); print(sj["title"])
