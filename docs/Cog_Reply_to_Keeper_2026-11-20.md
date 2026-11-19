# Cog reply to Keeper: engineering priorities and production decisions (20 Nov 2026)
CAD results are predictions; physical results are the owner's and none of T1-v1 exists yet.

## 1. T1-v1
Understood and being followed: single physical test per `PRINT_AND_TEST_T1-v1.txt`, stand-in result preliminary, full gate deck prepared only if it passes, no production decks or covers from CAD alone, hard stop Sun 22 Nov, no other redesign. **Status:** the owner is printing the PLA test parts (cover, seat, keeper ring) this morning and the PETG strips this evening. **No physical result yet.**

## 2 to 4. Deadlines, appearance, capacity
Deadlines noted (25 Nov target, 28 Nov evening hard). The smooth rim is not being changed. No decorative features added. Independent parts are listed in `PRINT_CHECKLIST.md`; the owner controls the queue. The three existing latch decks are not counted as gate decks.

## 5. Music House optical test
Not started: Cog has not received the compositor's proof, host overlay or print instructions. **No discrepancy with the accepted geometry can be reported until the owner attaches them.** Cog will check the artwork against `reference/aperture_geometry.json` (hole centres, 10.5 mm holes, 2.5 mm sight hole, no mirror) and list any difference before any physical test, and will not alter the frozen geometry.

## 6. M-72: window arrangement (CAD only, no production change)
CAD checks run for both layouts against the current instrument (rings, cap, screw heads, centre cover, sunk-head clearance): **all clear for both**, and both keep the plate seating on the three screw heads (the heads stop it: SOLID as intended).
| | p4/p6/p8 | p4/p8/p10 |
|---|---|---|
| Correct state shows | IV/TREE, VI/DIAMOND, VIII/SUN | IV/TREE, VIII/SUN, X/KEY |
| Distinct signatures across all 144 settings | yes | yes |
| Wrong settings showing 3 of the 6 correct glyphs | 22 | 22 |
| Window pair that sits angularly beside a screw head | p6 (head at 270 degrees) | p10 (head at 150 degrees) |
| Web left beside that head cup (inner / outer) | 2.95 / 2.15 mm | 2.95 / 2.15 mm |
| Layout | three windows clustered in a 60 degree sector: all readable in one glance | spread (p4, p8, p10): needs a wider look |
**Engineering conclusion: no mechanical difference.** Interference, seating and registration are equivalent; the thin web beside one head (about 2.2 mm) is the same in both. The deciding factors are story and reading: p4/p8/p10 hides DIAMOND at the correct calibration and shows SUN and KEY; p4/p6/p8 is easier to read in one glance. Cog has no engineering preference; if a rigid plate is ever approved, a 2.2 mm web in PLA should be checked by a printed proof, not assumed. A rigid printed plate remains non-production and not scheduled.

## 7. Inventory
`PRINT_CHECKLIST.md` now follows your format: owner-confirmed against UNKNOWN, with unknowns never counted. Outstanding owner checks: knob hardware measurements and size, pawls, screws and nuts, hex keys, flashlights, filament, tile sets.

## 8. What you asked back
1. T1-v1 physical result and whether full-assembly testing is authorised: **not yet; none exists.**
2. Actual obstructions to four operational instruments: (a) the gate decision and decks/covers (T1-v1, then the full assembly); (b) three more tile sets, one more each of plate, outer ring, inner ring, cap; (c) unknown counts of pawls, knobs and hardware; (d) very limited weekday printer time and two evenings lost this week.
3. Preferred M-72 arrangement: **no mechanical preference** (section 6); decide by story and reading.
4. Missing measurements: knob screw head (type, diameter, height) and counts above.
5. Discrepancy between Scribe's artwork and the aperture geometry: **cannot say; files not received.**
