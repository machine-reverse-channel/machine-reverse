"""Write agendamento/meta/videoNN.json (what gets published) and agendamento/creditos/videoNN.md.
usage: make_meta.py videoNN <deliveries folder with chapters.txt, credits.json, shorts/shorts.md>"""
import html, json, os, re, sys

v, d = sys.argv[1], sys.argv[2]
n = v.replace("video", "")
sj = json.load(open(f"videos/{v}/script.json"))
chapters = open(f"{d}/chapters.txt").read().strip()
credits = json.load(open(f"{d}/credits.json"))
src = open(f"videos/{v}/sources.txt").read().strip() if os.path.exists(f"videos/{v}/sources.txt") else ""
REPO = "https://github.com/viniciushoscher-ctrl/machine-reverse/blob/main/agendamento/creditos"

seen, lines = set(), []
for c in credits:
    t = c["title"].replace("File:", "")
    if t in seen: continue
    seen.add(t)
    a = html.unescape(re.sub("<[^>]+>", "", c.get("artist", "") or "")).strip() or "unknown"
    lines.append(f"- {t} by {a}, {c.get('license', '')}, {c.get('page', '')}")
open(f"agendamento/creditos/{v}.md", "w").write(f"# Photo credits: {sj['title']}\n\nAll photos from Wikimedia Commons.\n\n" + "\n".join(lines) + "\n")

hook = sj["scenes"][0]["text"]
count = sum(1 for s in sj["scenes"] if s.get("short"))
head = (f"{hook}\n\nMachine Reverse takes apart the machines you see every day and explains, part by part, why each one exists. "
        f"This video covers {count} parts.\n\nChapters:\n{chapters}\n\nSources:\n{src}\n\n")
full = head + "Photos from Wikimedia Commons:\n" + "\n".join(l.rsplit(", http", 1)[0] for l in lines)
short_credit = head + f"Photos from Wikimedia Commons. Full credits and licenses: {REPO}/{v}.md"
desc = full if len(full) <= 4800 else short_credit
desc = desc.replace("<", "").replace(">", "")[:4900] + "\n\n#engineering #machines #whydoesthisexist"

words = re.sub(r"[^a-z ]", "", sj["title"].lower()).split()
stop = {"why", "is", "are", "there", "a", "the", "of", "on", "in", "do", "does", "every", "your", "to", "this", "these"}
key = [w for w in words if w not in stop]
tags = [" ".join(key), *key, "engineering", "how it works", "why does this exist", "machine reverse", "engineering explained"]
tags = list(dict.fromkeys(t for t in tags if t))[:15]

# Short n = the n-th arrow scene; titles come from script.json so they can be fixed without a new render
md = open(f"{d}/shorts/shorts.md").read()
files = re.findall(r"(short\d+\.mp4)", md)
titles = [s["short"] for s in sj["scenes"] if s.get("short")]
shorts = []
for f, title in zip(files, titles):
    shorts.append({"file": f, "title": f"{title} #Shorts",
                   "description": f"Why does this exist? The full story: \"{sj['title']}\" on Machine Reverse.\n#shorts #engineering"})
json.dump({"title": sj["title"], "description": desc, "tags": tags, "shorts": shorts},
          open(f"agendamento/meta/{v}.json", "w"), indent=1, ensure_ascii=False)
print(v, len(desc), "chars,", len(shorts), "shorts")
