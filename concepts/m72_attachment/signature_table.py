#!/usr/bin/env python3
"""NON-PRODUCTION. What windows A, B, C (clock positions p4, p6, p8 clockwise of the fixed arrow) show for every one of the 144 ring settings.
outer = outer-ring numeral at the arrow, inner = inner-ring symbol at the arrow. The validated calibration is outer XII + inner STAR."""
import csv
N = ["XII","I","II","III","IV","V","VI","VII","VIII","IX","X","XI"]
S = ["SUN","MOON","KEY","FLAME","STAR","WAVE","MOUNTAIN","HOURGLASS","TREE","COMPASS","DIAMOND","EYE"]
WIN = {"A": 4, "B": 6, "C": 8}
def sig(o, j): return {w: f"{N[(o+p)%12]}/{S[(j+p)%12]}" for w, p in WIN.items()}
correct = (0, 4)
rows = []
for o in range(12):
    for j in range(12):
        s = sig(o, j); c = sig(*correct)
        same_num = sum(s[w].split('/')[0] == c[w].split('/')[0] for w in WIN); same_sym = sum(s[w].split('/')[1] == c[w].split('/')[1] for w in WIN)
        kind = "CORRECT" if (o, j) == correct else ("outer right, inner wrong" if o == correct[0] else ("inner right, outer wrong" if j == correct[1] else ("both rings moved the same number of clicks" if (o - correct[0]) % 12 == (j - correct[1]) % 12 else "both wrong")))
        rows.append([N[o], S[j], s["A"], s["B"], s["C"], same_num, same_sym, kind])
with open("m72_signature_table_all144.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["outer_at_arrow", "inner_at_arrow", "window_A_p4", "window_B_p6", "window_C_p8", "numerals_matching_correct_(of_3)", "symbols_matching_correct_(of_3)", "state_type"]); w.writerows(rows)
print("rows:", len(rows))
near = [r for r in rows if r[7] != "CORRECT" and (r[5] + r[6]) >= 3]
print("states that show 3 or more of the 6 correct glyphs:", len(near))
print("every state's 6-glyph signature is distinct:", len({tuple(r[2:5]) for r in rows}) == 144)
print("the correct signature:", rows[0*12+4][2:5] if False else sig(*correct))
