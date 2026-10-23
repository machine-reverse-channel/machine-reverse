"""Make a 1280x720 YouTube thumbnail: real photo, red arrow on the part, big yellow WHY question.
usage: thumb.py out.jpg photo.jpg x,y "WHY THE|HOLE?" [inset.jpg ix,iy]   (x,y and ix,iy are 0-1 fractions)"""
import math, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
W, H = 1280, 720


def arrow(d, tip, angle, length=230, color=(225, 20, 30)):
    """Thick arrow whose tip is at `tip`, coming from direction `angle` (radians)."""
    ux, uy = math.cos(angle), math.sin(angle); px, py = -uy, ux
    tx, ty = tip; hx, hy = tx - ux * 90, ty - uy * 90; bx, by = tx - ux * length, ty - uy * length
    pts = [(tx, ty), (hx + px * 70, hy + py * 70), (hx + px * 28, hy + py * 28), (bx + px * 28, by + py * 28),
           (bx - px * 28, by - py * 28), (hx - px * 28, hy - py * 28), (hx - px * 70, hy - py * 70)]
    d.polygon(pts, fill="white", outline="white", width=18)
    d.polygon(pts, fill=color)


def main(out, photo, xy, text, inset=None, ixy=None):
    im = ImageOps.fit(Image.open(photo).convert("RGB"), (W, H))
    im = Image.eval(im, lambda v: int(v * 0.92))
    d = ImageDraw.Draw(im)
    x, y = [float(v) for v in xy.split(",")]; tx, ty = x * W, y * H
    if inset:  # zoom bubble with the detail the photo can't show
        ix, iy = [float(v) for v in ixy.split(",")]
        src = Image.open(inset).convert("RGB"); sw, sh = src.size; r = int(min(sw, sh) * 0.18)
        crop = src.crop((int(ix * sw) - r, int(iy * sh) - r, int(ix * sw) + r, int(iy * sh) + r)).resize((360, 360))
        mask = Image.new("L", (360, 360), 0); ImageDraw.Draw(mask).ellipse((0, 0, 359, 359), fill=255)
        cx, cy = int(W * 0.79), int(H * 0.66)
        d.ellipse((cx - 192, cy - 192, cx + 192, cy + 192), fill="white")
        im.paste(crop, (cx - 180, cy - 180), mask)
        d.line((tx, ty, cx - 150, cy - 90), fill="white", width=6)
    ang = math.atan2(ty - H * 0.25, tx - W * 0.5) if ty > H * 0.35 else math.pi / 2
    arrow(d, (tx, ty), ang)
    lines = text.split("|"); size = 150
    f = ImageFont.truetype(FONT, size)
    while max(d.textlength(l, font=f) for l in lines) > W * 0.62: size -= 6; f = ImageFont.truetype(FONT, size)
    yy = 30
    for l in lines:
        d.text((40, yy), l, font=f, fill=(255, 212, 0), stroke_width=12, stroke_fill="black"); yy += int(size * 1.08)
    im.save(out, quality=90)


if __name__ == "__main__":
    main(*sys.argv[1:])
