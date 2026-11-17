#!/usr/bin/env python3
"""Reads the aperture holes back from the exported back plate (a real cross-section through the floor) and compares them with
reference/aperture_geometry.json. Exit 0 = pass. This replaces the old mask checks."""
import json, math, os, re, subprocess, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ref = json.load(open(os.path.join(ROOT, "reference", "aperture_geometry.json")))
scad = os.path.join(ROOT, "cad", "chronometer.scad")
tmp = tempfile.mkdtemp(); svg = os.path.join(tmp, "cut.svg")
osc = ["openscad"]
if not os.environ.get("DISPLAY"): osc = ["xvfb-run", "-a", "openscad"]
extra = sys.argv[1:]          # optional -D overrides
subprocess.run(osc + ["-o", svg, "-D", 'part="aperture_cut"'] + extra + [scad], check=True, capture_output=True)
loops = []
for d in re.findall(r'd="([^"]+)"', open(svg).read()):
    for sub in re.split(r"(?=M)", d):
        pts = [tuple(map(float, m)) for m in re.findall(r"(-?\d+\.?\d*(?:e-?\d+)?)\s*,\s*(-?\d+\.?\d*(?:e-?\d+)?)", sub)]
        if len(pts) >= 3: loops.append(pts)
def area(p): return 0.5 * sum(p[i][0] * p[(i + 1) % len(p)][1] - p[(i + 1) % len(p)][0] * p[i][1] for i in range(len(p)))
def cen(p):
    a, n, cx, cy = area(p), len(p), 0, 0
    for i in range(n):
        x0, y0 = p[i]; x1, y1 = p[(i + 1) % n]; c = x0 * y1 - x1 * y0; cx += (x0 + x1) * c; cy += (y0 + y1) * c
    return cx / (6 * a), -cy / (6 * a)     # SVG y is down
found = []
for p in loops:
    cx, cy = cen(p)
    if math.hypot(cx, cy) < 22.5 and abs(area(p)) < 400: found.append((cx, cy, 2 * math.sqrt(abs(area(p)) / math.pi)))
want = [(h["x_mm"], h["y_mm"], 10.5, h["letter"]) for h in ref["holes"]] + [(0.0, 0.0, 2.5, "sight")]
ok = len(found) == len(want)
print(f"holes found in the plate floor: {len(found)} (expected {len(want)})")
for (wx, wy, wd, name) in want:
    best = min(found, key=lambda f: math.hypot(f[0] - wx, f[1] - wy), default=None)
    if best is None: ok = False; print(f"  {name}: MISSING"); continue
    e = math.hypot(best[0] - wx, best[1] - wy); dd = best[2] - wd
    good = e < 0.02 and -0.03 < dd < 0.001      # a 64-sided circle is 0.008 under its nominal diameter
    ok &= good
    print(f"  {name:5s} centre error {e:.3f} mm, diameter {best[2]:.3f} (nominal {wd})  {'ok' if good else 'FAIL'}")
print("PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
