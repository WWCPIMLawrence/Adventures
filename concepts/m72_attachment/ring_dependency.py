#!/usr/bin/env python3
"""NON-PRODUCTION. For a fixed-position window at clock position p (clockwise of the fixed arrow), what pair (outer numeral, inner symbol)
is visible for every one of the 144 ring settings? Reads nothing from the CAD but its stated orders; positions are the 30 deg pitch."""
N = ["XII","I","II","III","IV","V","VI","VII","VIII","IX","X","XI"]                          # outer ring, clockwise from its XII
S = ["SUN","MOON","KEY","FLAME","STAR","WAVE","MOUNTAIN","HOURGLASS","TREE","COMPASS","DIAMOND","EYE"]  # inner ring, clockwise from its SUN
def pair(o, j, p): return (N[(o + p) % 12], S[(j + p) % 12])   # o = outer index at the arrow, j = inner index at the arrow
CORRECT = (0, S.index("STAR"))                                  # outer XII and inner STAR at the arrow (validated calibration)
print("calibrated state (XII / STAR at the arrow): pair at each position p")
print("  " + "  ".join(f"p{p}:{N[(CORRECT[0]+p)%12]}/{S[(CORRECT[1]+p)%12]}" for p in range(12)))
for p in range(12):
    pairs = {pair(o, j, p) for o in range(12) for j in range(12)}
    assert len(pairs) == 144       # every setting gives a different pair at ANY single window: the window shows both ring settings
print("\nat any single window, all 144 ring settings give 144 different pairs: the pair identifies BOTH rings")
p = 6
print(f"\nwindow at p{p}: pair seen for the correct setting and for single-ring errors")
ok = pair(*CORRECT, p); print("  correct:", ok)
for d in (-2, -1, 1, 2):
    print(f"  inner ring {d:+d} click, outer correct:", pair(CORRECT[0], CORRECT[1] + d, p), "|  outer ring", f"{d:+d} click, inner correct:", pair(CORRECT[0] + d, CORRECT[1], p))
# a signature needs BOTH halves: how many settings show the correct numeral / the correct symbol / both?
shown_num = sum(1 for o in range(12) for j in range(12) if pair(o, j, p)[0] == ok[0])
shown_sym = sum(1 for o in range(12) for j in range(12) if pair(o, j, p)[1] == ok[1])
both = sum(1 for o in range(12) for j in range(12) if pair(o, j, p) == ok)
print(f"  settings showing the right numeral: {shown_num} of 144; the right symbol: {shown_sym} of 144; both: {both}")
