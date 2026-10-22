"""Check Wikimedia Commons coverage for a list of queries (one per line in a text file).
Writes a Markdown report with how many usable photos each query finds and the first 8 file names,
plus small previews of the first 4, so the photos can be reviewed before writing arrow positions."""
import json, pathlib, sys, requests
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from fetch_media import api_pages, download, HEADERS  # noqa: E402


def usable(query):
    params = {"action": "query", "format": "json", "generator": "search",
              "gsrsearch": f"{query} filetype:bitmap", "gsrnamespace": 6, "gsrlimit": 40,
              "prop": "imageinfo", "iiprop": "url|size|mime|extmetadata", "iiurlwidth": 640}
    out = []
    for p in sorted(api_pages(params).values(), key=lambda x: x.get("index", 0)):
        info = (p.get("imageinfo") or [{}])[0]
        lic = info.get("extmetadata", {}).get("LicenseShortName", {}).get("value", "")
        if info.get("mime") == "image/jpeg" and info.get("width", 0) >= 2000 and \
                info["width"] >= info.get("height", 0) * 1.3 and lic.startswith(("CC", "Public domain", "PD")):
            out.append({"title": p["title"], "thumb": info["thumburl"], "license": lic})
    return out


def main(listfile, outdir):
    out = pathlib.Path(outdir); (out / "prev").mkdir(parents=True, exist_ok=True)
    rep = ["| # | Query | Usable photos | First files |", "|---|---|---|---|"]
    data = {}
    for n, q in enumerate(x.strip() for x in open(listfile) if x.strip()):
        res = usable(q); data[q] = res
        for k, r in enumerate(res[:4]):
            (out / "prev" / f"{n:02d}_{k}.jpg").write_bytes(download(r["thumb"]))
        rep.append(f"| {n:02d} | {q} | {len(res)} | " + "<br>".join(r["title"] for r in res[:8]) + " |")
        print(n, q, len(res))
    (out / "report.md").write_text("\n".join(rep) + "\n")
    (out / "results.json").write_text(json.dumps(data, indent=1))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
