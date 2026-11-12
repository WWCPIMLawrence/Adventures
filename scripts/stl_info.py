#!/usr/bin/env python3
"""Bounding box and volume of ASCII STL files (as written by OpenSCAD).
   stl_info.py file.stl ...            -> prints a table
   stl_info.py --volume-below V f.stl  -> exit 0 if |volume| < V mm^3"""
import re, sys

def info(path):
    v = [tuple(map(float, m.groups()))
         for m in re.finditer(r"vertex\s+(\S+)\s+(\S+)\s+(\S+)", open(path).read())]
    if not v:
        return None
    vol = 0.0
    for i in range(0, len(v), 3):
        a, b, c = v[i:i + 3]
        vol += (a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0])
                + a[2] * (b[0] * c[1] - b[1] * c[0])) / 6
    lo = [min(p[i] for p in v) for i in range(3)]
    hi = [max(p[i] for p in v) for i in range(3)]
    return lo, hi, abs(vol)

if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--volume-below":
        r = info(args[2])
        sys.exit(0 if r is None or r[2] < float(args[1]) else 1)
    for f in args:
        r = info(f)
        if r is None:
            print(f"{f}: empty"); continue
        lo, hi, vol = r
        size = " x ".join(f"{hi[i] - lo[i]:.1f}" for i in range(3))
        print(f"{f.split('/')[-1]:24s} {size:24s} mm   {vol / 1000:7.2f} cm3")
