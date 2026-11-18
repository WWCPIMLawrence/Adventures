#!/usr/bin/env python3
"""NON-PRODUCTION. A shutter disc turning about the plate centre carries the same four holes. At which rotation angles does it cover every floor hole
(zero overlap between any shutter hole and any floor hole)? Distances only: two circles of the same diameter overlap when their centres are closer than the diameter."""
import math
holes = [(7.053, 9.708), (14.095, -5.130), (-4.603, -9.437), (-12.977, 3.721)]
D = 10.5
def rot(p, a): c, s = math.cos(a), math.sin(a); return (p[0]*c - p[1]*s, p[0]*s + p[1]*c)
def min_gap(a):   # smallest centre distance between any shutter hole and any floor hole, minus the hole diameter (positive = no overlap)
    return min(math.dist(rot(p, a), q) for p in holes for q in holes) - D
rows = [(deg, min_gap(math.radians(deg))) for deg in range(0, 360)]
open_at = [d for d, g in rows if g < 0 and d in (0, 359, 1)]
closed = [d for d, g in rows if g > 0.0]
print("rotation angles (degrees) at which the shutter fully closes all four holes (gap > 0):")
runs = []; 
for d in closed:
    if runs and d == runs[-1][-1] + 1: runs[-1].append(d)
    else: runs.append([d])
for r in runs: print(f"  {r[0]} to {r[-1]} deg   (best margin {max(min_gap(math.radians(x)) for x in r):.1f} mm at {max(r, key=lambda x: min_gap(math.radians(x)))} deg)")
print("\nworst overlap at 180 deg (the obvious guess):", round(min_gap(math.pi), 2), "mm gap (negative = still overlapping)")
if runs:
    best = max(rows, key=lambda t: t[1]); print("widest closed margin:", round(best[1], 2), "mm at", best[0], "deg")
    # how far does the shutter have to turn from open to closed, and is the closed zone wide enough for a detent?
    nearest = min(closed, key=lambda d: min(d, 360 - d)); print("smallest turn from open to fully closed:", min(nearest, 360 - nearest), "deg")

# ---- how bad is the best case? leak = area of floor holes still uncovered by solid shutter = overlap with the shutter's identical openings ----
r = D/2
def lens(d):                                  # overlap area of two circles of radius r with centre distance d
    if d >= 2*r: return 0.0
    return 2*r*r*math.acos(d/(2*r)) - (d/2)*math.sqrt(4*r*r - d*d)
def leak(a): return sum(lens(math.dist(rot(p, a), q)) for p in holes for q in holes)
best = min(range(0, 3600), key=lambda t: leak(math.radians(t/10)))
total = 4*math.pi*r*r
print(f"\nbest case turning about the centre: {best/10:.1f} deg, still leaks {leak(math.radians(best/10)):.1f} mm2 of {total:.0f} mm2 ({100*leak(math.radians(best/10))/total:.0f} % of the open area)")
# ---- other pivots: rotate the shutter about any point (a swing shutter) or slide it: is there ANY rigid motion that clears all four holes? ----
def clear(motion):  # returns True if no shutter opening overlaps any floor hole
    return all(math.dist(motion(p), q) >= D for p in holes for q in holes)
def rot_about(c, a): return lambda p: (c[0] + (p[0]-c[0])*math.cos(a) - (p[1]-c[1])*math.sin(a), c[1] + (p[0]-c[0])*math.sin(a) + (p[1]-c[1])*math.cos(a))
found = None
for cx in range(-60, 61, 3):
    for cy in range(-60, 61, 3):
        for deg in range(5, 360, 5):
            if clear(rot_about((cx, cy), math.radians(deg))): found = (cx, cy, deg); break
        if found: break
    if found: break
print("a swing about some pivot clears all four holes:", f"yes, e.g. pivot {found[:2]} mm, {found[2]} deg" if found else "no pivot within 60 mm works")
need = None
for dist in [x/2 for x in range(20, 140)]:
    for deg in range(0, 360, 5):
        d = (dist*math.cos(math.radians(deg)), dist*math.sin(math.radians(deg)))
        if clear(lambda p: (p[0]+d[0], p[1]+d[1])): need = (dist, deg); break
    if need: break
print(f"a straight slide that clears all four holes needs at least {need[0]:.1f} mm of travel (direction {need[1]} deg); the well is 50 mm across" if need else "no slide < 70 mm clears them")
