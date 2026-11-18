# Production plan: four Chronometers for the 27 November 2026 hunt

Prepared 17 Nov 2026 (Tuesday). **Production preparation is due Wed 25 Nov; Thu 26 is Thanksgiving; the hunt is Fri 27 Nov.**
Printer: one Bambu P1S with AMS. Times are **estimates**: PrusaSlicer's generic profile divided by 3 (the P1S rule of thumb used earlier), not measured.
**Please send the real time of your last back plate so I can calibrate them.** Nothing here assumes what you already have printed (see section 7).

## 0. Calibration update (18 Nov, 7:28 PM)

The owner is printing **two two-colour back plates on one bed, Bambu estimate 1:45** (about 53 min per plate, including colour changes). My estimate was about 1 h 25 per plate. So:

- The slicer-generic / 3 rule is too slow for the plate (ratio about 3.9 from this one data point). **Use generic / 4 as a working figure, and treat it as one data point, not a rule.**
- **Two 125 mm parts fit on one bed.** Plan two bases, two decks and two plates per run (halves the run count for batches A, B and C).
- Revised totals: about 4.5 to 5 h per instrument and about 19 h for four (about 24 h with spares), down from 26 and 32.
- All four plates take two runs (about 3.5 h); a third run adds spares.

## 1. What is settled and what is not

| Item | State | Needed before printing |
|---|---|---|
| Back plate with the integral asym_v1 aperture | Printed and tested by you: holes 10.5 / 2.5 mm, flat, bond, fits the base, template matches. Journal proof not yet | Nothing. **Start now** |
| New base (no lip) | Designed, not printed; your old base accepts the new plate | Nothing |
| Rings, index cap, pawls, tiles | Tested earlier (rings, pawls, tiles); brass cap and rings not yet in final colours | Nothing |
| Centre cover retention: **gate (G)** vs **three-arm latch (L)** | Gate mechanism works (press and twist); **knob test pending** | **Knob test result (Gate G1)** |
| Knob (keystone) screw-head pocket | Held | Phillips screw head size, or use the socket-head screw as designed (**Gate G2**) |
| Journal proof (Work), both play orders | Not tested | Work's page; I still need the two documents |

## 2. Parts per instrument (gate variant G; the fallback L differs only in deck, cover and ring)

P1S time = generic / 3 (rounded), without AMS colour-change time. Weight = slicer filament volume x 1.24 (PLA) at 15 % infill, 3 walls.

| Part | Qty | Material and colour | P1S time | Weight | Notes |
|---|---|---|---|---|---|
| `base` | 1 | PLA brass | 1 h 20 | 47 g | No lip. One per plate |
| `back_plate` | 1 | PLA brass + black floor (two bodies) | 1 h 10 + 15 min | 25 g brass + 2 g black | Bone arrow by hand. Outer brim only. Already validated |
| `deck` (G: gate pockets, no latch grooves) | 1 | PLA brass | 1 h 15 | 30 g | |
| `cover` (G: smooth rim, no slots, ledge) | 1 | PLA brass | 20 min | 11 g | Print flange down |
| `uv_ring` plain (G) | 1 | PETG | 3 min | 1.5 g | PETG, flat |
| gate strips (6 per unit) | 6 + spares | PETG | 3 min per set of 6 | under 1 g | Press-fit feet (v2). Keep soft and firm sets apart |
| `outer_ring` | 1 | PLA black, ivory numerals | 35 min + colour change | 19 g | One change at layer 29 |
| `inner_ring` | 1 | PLA black, ivory symbols and ribs | 22 min + colour change | 12 g | One change at layer 29 |
| `index_cap` | 1 | PLA brass, ivory arrow | 16 min + colour change | 8 g | Change at layer 13 |
| `keystone` (knob) | 1 | PLA brass | 3 min | 1.5 g | Pocket held (G2) |
| fragment tiles (4) + black digit inlay | 1 set | PLA ivory + black | 12 min | 5.5 g | As tested: separate inlay bodies |
| `pawl_outer` x2, `pawl_inner` x2 | 4 | PETG | 3 min | 0.8 g | 1.4 mm thick, as confirmed |
| **Total per instrument** | | | **about 6 h 30 with colour changes** | **about 165 g** | brass about 122 g, black about 33 g, ivory about 10 g, PETG about 3 g |

**Fallback L** (three-arm latch, if the knob test fails): `deck`, `cover` and `uv_ring` (three-arm) from the current defaults; no strips. Times are within a few minutes of the above.

## 3. Totals

| | 4 instruments | with about 25 % spares and reprints |
|---|---|---|
| Machine time | about 26 h | about 32 h |
| Brass PLA | about 490 g | about 610 g (one 1 kg spool) |
| Black PLA | about 130 g | about 165 g |
| Ivory / bone PLA | about 40 g | about 50 g |
| PETG | about 10 g | about 15 g |

AMS purge adds waste on the coloured parts; allow another 15 to 20 %. **Filament stock is not assumed. Please check it.**

## 4. Hardware (4 instruments)

| Item | Per instrument | Total (+ spares) |
|---|---|---|
| M3 x 8 socket-head, black (back plate) | 4 | 16 (+4) |
| M3 x 16 socket-head, black (index cap) | 3 | 12 (+3) |
| M3 x 10 (knob), Phillips or socket head | 1 | 4 (+2) |
| M3 nut (captive in the cover) | 1 | 4 (+2) |
| 2.5 mm hex key (clue envelope reward; also for testing) | 1 | 4 (+2) |
| UV flashlight and UV paper disc | 1 | 4 (+1) |

Inventory is not assumed. **Please tell me what you already have.**

## 5. Print batches (bed 256 mm; one 125 mm part per plate, small parts together)

| Batch | Contents | Plates | P1S time |
|---|---|---|---|
| A | `back_plate` x 4 (two colours) | 4 | about 6 h |
| B | `base` x 4 | 4 | about 5.5 h |
| C | `deck` x 4 (G or L, after Gate G1) | 4 | about 5 h |
| D | `outer_ring` x 4 | 4 | about 2.5 h |
| E | `inner_ring` x 4 (3 per plate fits) | 2 | about 1.5 h |
| F | `index_cap` x 4 + `cover` x 4 | 2 | about 2.5 h |
| G | tiles x 4 sets + digit inlays | 1 | about 1 h |
| H | PETG: 16 pawls, 4 plain rings, 24 + 12 strips | 1 to 2 | about 30 min |
| I | `keystone` x 4 (after Gate G2) | 1 | about 15 min |

## 6. Schedule

| Date | Plan |
|---|---|
| **Tue 17 (tonight)** | **Start Batch A** (back plates, overnight, about 6 h). Reprint the gate seat and strips v2 (about 20 min) for the knob test |
| **Wed 18** | **Knob test result: choose G or L (Gate G1).** Batch B (bases). Send me the Phillips screw measurements (Gate G2), the two missing documents and your inventory. Run the 1:1 template and the first journal proof when Work delivers it |
| **Thu 19** | **Freeze** the files (a master zip). Batch C (decks), Batch F (caps and covers). Pilot instrument: assemble unit 1 end to end |
| Fri 20 to Sun 22 | Batches D, E, G, H, I. Assemble units 2 to 4 as parts finish. Reprint failures |
| Mon 23 | Test all four: both play orders with the real journal proof, repeated plate refits, gate and knob, shake test |
| Tue 24 | Reprint anything that failed, pack the host kit (keys, lights, proof pages) |
| **Wed 25** | **Production preparation complete** (deadline) |
| Thu 26 | Buffer (Thanksgiving) |
| **Fri 27** | Hunt |

Why the pilot unit first: one fully assembled instrument by Thu 19 exposes any assembly problem (stack height, plate and base fit, the gate with real tiles) before three more are built.

## 7. Credit for what you already have (to fill in)

List what is final-quality and reusable, and I will remove it from the batches: tiles (you said they look perfect), rings printed on 16 Nov, the old base and plate, pawl sets, brass parts. Please tell me. I am not assuming any of it.

## 8. Risks and how they are covered

- **Gate fails the knob test:** fall back to L (deck, cover, ring from the defaults). No new design work, about the same print time.
- **Journal proof shows a problem:** the plate is the only part involved; a reprint is about 1.5 h each, so about 6 h for four. Keep Wed 18 to Mon 23 free for it.
- **Print failures:** about 25 % spares are budgeted; the brass parts are the long ones (base, plate, deck).
- **Colour changes:** keep the paint tool off. The rings and cap use a single layer change; the plate uses two bodies and a hand-coloured arrow, as you did.
- **Strips:** they are consumables. Print 36 for four units, keep them in a bag, and test the press fit on the first deck.
- **Time estimates:** not yet calibrated. Your real plate time fixes this.

## 9. Questions to answer today

1. Real print time of your last plate (and base, if you have it).
2. What you already have that is final-quality (section 7).
3. Brass, black, ivory and PETG stock.
4. Screws, nuts, hex keys and lights in stock.
5. Phillips screw head: diameter, height, style. If you cannot get them by Thu 20, I will keep the current socket-head pocket.
6. The two missing documents: the journal page update and the asym_v1 test PDF.
