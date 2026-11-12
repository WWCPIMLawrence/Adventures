#!/usr/bin/env python3
"""Draws images/clamp_section.png from the five 2D cuts build/clamp_N.svg written by build.sh:
a true section through the centre of the cover with fragments fitted and the keystone tightened."""
import os, re
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTS = [("centre cover", (184, 148, 77)), ("fragments", (225, 219, 196)), ("keystone", (45, 47, 56)),
         ("M3 x 8 screw", (140, 146, 153)), ("M3 nut", (150, 40, 34))]
S, W, H, X0, Y0 = 46, 1500, 760, -16.0, -13.5        # px per mm, canvas, model coords of the top-left corner
img = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(img)
for n, (name, col) in enumerate(PARTS):
    svg = open(os.path.join(ROOT, "build", "clamp_%d.svg" % n)).read()
    polys = []
    for path in re.findall(r' d="([^"]+)"', svg):
        for sub in re.split(r"(?=M)", path):
            pts = [(float(a), float(b)) for a, b in re.findall(r"(-?[\d.]+),(-?[\d.]+)", sub)]
            if len(pts) > 2: polys.append(pts)
    # even-odd fill so holes stay open
    layer = Image.new("L", (W, H), 0); ld = ImageDraw.Draw(layer)
    for pts in polys:
        m = Image.new("L", (W, H), 0)
        ImageDraw.Draw(m).polygon([((x - X0) * S, (y - Y0) * S) for x, y in pts], fill=255)
        layer = Image.composite(Image.new("L", (W, H), 0), layer, m) if False else \
            Image.fromarray(__import__("numpy").bitwise_xor(__import__("numpy").array(layer), __import__("numpy").array(m)))
    img.paste(Image.new("RGB", (W, H), col), mask=layer)
    d = ImageDraw.Draw(img)
    d.rectangle([20, 20 + 30 * n, 44, 40 + 30 * n], fill=col, outline="black")
    d.text((54, 24 + 30 * n), name, fill="black")
d.text((20, H - 30), "Section through the centre, keystone fully tightened: cone seated on the fragment bevels, "
       "0.3 mm gap left under the knob, nut held behind the undersized pocket mouth.", fill="black")
img.save(os.path.join(ROOT, "images", "clamp_section.png"))
