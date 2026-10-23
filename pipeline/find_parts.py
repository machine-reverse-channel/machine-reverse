"""Find candidate photos for the arrow scenes, with looser filters than fetch_media.py.
Input: a text file, one Commons query per line. Output: report.md with the candidates (title, size,
license) and previews cropped to 16:9 exactly like the render, so arrow positions can be read off them."""
import io, json, pathlib, sys
from PIL import Image, ImageOps
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from fetch_media import api_pages, download  # noqa: E402


def candidates(query, n=8):
    params = {"action": "query", "format": "json", "generator": "search",
              "gsrsearch": f"{query} filetype:bitmap", "gsrnamespace": 6, "gsrlimit": 40,
              "prop": "imageinfo", "iiprop": "url|size|mime|extmetadata", "iiurlwidth": 640}
    out = []
    for p in sorted(api_pages(params).values(), key=lambda x: x.get("index", 0)):
        info = (p.get("imageinfo") or [{}])[0]
        lic = info.get("extmetadata", {}).get("LicenseShortName", {}).get("value", "")
        if info.get("mime") in ("image/jpeg", "image/png") and info.get("width", 0) >= 1000 and \
                lic.startswith(("CC", "Public domain", "PD")):
            out.append({"title": p["title"], "thumb": info["thumburl"], "license": lic,
                        "size": f"{info['width']}x{info.get('height', 0)}"})
        if len(out) >= n:
            break
    return out


def main(listfile, outdir):
    out = pathlib.Path(outdir); (out / "prev").mkdir(parents=True, exist_ok=True)
    rep, data = [], {}
    for n, q in enumerate(x.strip() for x in open(listfile) if x.strip()):
        res = candidates(q); data[q] = res
        rep.append(f"## {n:02d} {q} ({len(res)})")
        for k, r in enumerate(res):
            im = Image.open(io.BytesIO(download(r["thumb"]))).convert("RGB")
            ImageOps.fit(im, (480, 270)).save(out / "prev" / f"{n:02d}_{k}.jpg", quality=80)
            rep.append(f"- {n:02d}_{k} | {r['title']} | {r['size']} | {r['license']}")
        print(n, q, len(res))
    (out / "report.md").write_text("\n".join(rep) + "\n")
    (out / "results.json").write_text(json.dumps(data, indent=1))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
