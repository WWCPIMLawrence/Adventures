# The Timekeeper's Paradox: Chronometer, complete status handoff for planning
**Date:** Tuesday 17 November 2026 (evening, owner's local time)   **From:** Claude Code (engineering: CAD, validation design, production files)   **To:** the other AI tool (game design, journal pages, scheduling)
**Hunt:** **Sunday 29 November 2026** (moved from the 27th on 17 Nov). **Production preparation deadline:** Wed 25 Nov as last stated; **whether it moved with the hunt is unconfirmed** (ask the owner).

This file replaces all earlier status handoffs where they disagree (some still say 26 or 27 Nov, or describe a separate mask). Nothing below is reported as tested unless the owner reported it. Estimates are labelled.

---
## 1. The project in one paragraph
Four identical hand-held brass-and-black puzzle instruments ("Chronometers", 125 mm across, about 20 mm tall), one per team, 3D-printed on one Bambu P1S with AMS (PLA and PETG, M3 hardware, parametric OpenSCAD). Players turn two rings, remove and refit a centre cover, add four numbered fragment tiles one at a time, read a four-letter word through an aperture stencil, and finally recover a hidden UV flashlight from behind a screwed back plate. The engineering goal is four reliable, identical instruments by the hunt.

## 2. Settled puzzle facts (do not change without discussion)
- Fragments: **281 (Whitewater), 361 (Battle Creek), 924 (Baggs), 507 (Lookout)**. Code ring **813619245072**. Twelve-symbol order, UV message **"THE SUN IS FALSE. TRUST THE ARROW."**, **11:47**, aperture word **RIFT**, final outcome MIRROR to ORIGIN.
- Colours: brass fixed housing and centre elements; matte black rotating rings; bone-white raised markings; ivory fragment tiles with black digits; black screws.
- The **Allen key (2.5 mm) is a team clue-envelope reward, not a compartment in the device.** (A hidden key in the base was rejected: it needs its own order-proof hidden door.)
- The UV flashlight is **behind the screwed back plate** (four M3 x 8 socket-head screws). It stays a genuine hidden surprise.
- Team routes (Music House = aperture, Battle Creek = UV light): Red UV first (Battle Creek stop 4, Music House stop 6); Blue aperture first (1 then 6); Green UV first (2 then 8); Yellow aperture first (Music House 3, Battle Creek 7). **Both orders must work with identical hardware.**
- Journal: six-ring leather journal, pages about **82 x 129 mm**. The instrument cannot sit on a bound page. Players remove the compositor's proof leaf, lay it flat, and set the instrument on it. The page carries a central position cross and a directional rotation mark. (Work built this page; this side has **not** received it or its test document.)

## 3. Subsystem status (engineering view)
| Subsystem | Status | Evidence |
|---|---|---|
| Rings, detents (PETG pawls 1.4 mm), raised numerals and symbols, fragment tiles, flashlight bay | **Confirmed** | Owner physical tests |
| Back plate with **integral asym_v1 aperture** (replaces the separate mask) | **Validated by the owner on a printed plate**; journal proof not yet | See section 4 |
| Centre-cover retention: old three-arm latch | **Failing** (weakens after a few openings; cover comes off when the knob is loosened; its ring snags on insertion and falls out) | Owner reports |
| Centre-cover retention: **push-and-turn gate** (new) | **Mechanism works flawlessly in the owner's hands** (pulling does nothing; press and twist releases). **Knob test pending.** Springs fell out of the seat: fixed in CAD, not yet printed | Owner test 16 Nov |
| Plain retaining ring with positive ledge | **Works**: stays in, nothing to snag | Owner test 16 Nov |
| Smooth cover rim | Printed on the gate cover; no feedback yet on grip or look | |
| Knob screw (M3 x 10) head pocket | **Held** until the owner supplies the Phillips screw head size (diameter, height, style) | |
| Brass index cap with bone arrow; revised back-plate bosses | Built, not printed in final colours | CAD checks |

## 4. The aperture: decision, design and results
**Decision (16 Nov):** replace the loose stencil with a one-piece back plate: a **1.2 mm floor printed with the plate, back face on the bed, flush with the sheet (0 mm gap)**. The old separate mask (0.6 mm above the sheet) is retired. Reason: with the plate removed for the UV light, the old mask fell loose.

**Coordinates asym_v1 (frozen).** Looking DOWN onto the instrument from above (cover off); origin = centre; **+X right (3 o'clock); +Y toward the double notch (12 o'clock)**; **no mirror** for a face-up sheet. Reading order: from the double notch, sweep **clockwise**.
| Order | Letter | x (mm) | y (mm) | bearing clockwise from 12 | radius |
|---|---|---|---|---|---|
| 1 | R | +7.053 | +9.708 | 36 deg | 12.0 |
| 2 | I | +14.095 | -5.130 | 110 deg | 15.0 |
| 3 | F | -4.603 | -9.437 | 206 deg | 10.5 |
| 4 | T | -12.977 | +3.721 | 286 deg | 13.5 |
- Four round holes, **diameter 10.5 mm**; **sighting hole 2.5 mm at (0, 0)** over the sheet's centre cross (no solution letter may sit under it). Furthest hole edge 20.25 mm from the centre. Hole-to-hole web 5.1 mm; no symmetry; every hole at least 16 deg from a notch axis.
- Rim notches (radius 62.5): singles at 3, 6 and 9 o'clock; **double at 12 o'clock** (CAD angles 87 and 93 deg). Plate locating pin at 3 o'clock, radius 54; four screws at 45/135/225/315 deg, radius 54. The plate fits one way.
- Files: `reference/aperture_geometry.json` (SHA-256 `a37d539b04742708671a6f8608ef5e3975aca82f4068ecf44af8edda2a374aa8`) and the 1:1 template `reference/aperture_template_asym_v1.pdf`. **Do not approximate, mirror, scale, rotate or reorder.**
- **Sheet constraints for Work:** the floor is flush, so parallax is small (visible-region shift about 0.35 mm at 30 deg viewing, 0.5 mm at 40 deg); registration budget +/-1.5 mm; decoy letters must stay well clear of every hole centre (the old lattice kept neighbours 10.6 mm away; **this pattern is not on that lattice, so the old lattice generator cannot be reused**). The rim notches cannot register to marks on an 82 mm page, so registration comes from the sighting hole over the cross plus the page's direction mark.

**Physical results (owner-reported, 17 Nov, one two-colour plate):** no print problems; the four holes measure **10.5 mm** and the sighting hole **2.5 mm**; plate lies flat; black floor does not come away when pried; fits the owner's existing base through repeated refits; **the 1:1 template printed at 100 % on 8.5 x 11 matches (R, I, F, T and the circles line up)**; bone-white arrow at 12 o'clock coloured by hand (accepted; no extra file needed).
**Not yet tested:** the real journal proof in both play orders; blind-pair tests (can a pair infer RIFT from the sheet alone? from the instrument without notch instructions?); recoverability with the intended clue, outdoors and in a car; glare and opacity outdoors.

## 5. The centre cover: what was learned (for the story clue and any rules)
- The cover is the only part that reacts torque from the knob, so loosening the knob (anticlockwise) tends to unlock it. Stiffer latch arms cannot fix this; reversing the direction only moves the problem. **Release direction stays anticlockwise** (agreed).
- **Gate:** the cover sits about **1.2 mm proud** when locked (printed spring strips lift it into pockets); to open, **press down about 1 mm and turn anticlockwise 28 degrees, then lift.** Estimated (not measured) press force 8 to 14 N. Residual risk: pressing down hard on the knob while unscrewing could release it. **A clue such as "press the dial in and turn it back" is needed** (the time-reversal theme can carry it).
- **Knob test (pending, owner):** keystone knob with an M3 x 10 screw, 0 then 4 tiles, loosen and tighten by hand 10 times each way, holding nothing else: the cover must never turn; then repeat while pressing down on the knob.
- Decision rule: **pass = gate-only variant (G); fail = the existing three-arm latch (L).** The print files for both exist (section 7).

## 6. Production plan
**Per instrument (gate variant), P1S estimates** (calibrated from one data point: the owner's two two-colour plates took 1:45 together, about 53 min each; slicer-generic / about 4):
| Part | Qty | Material | Notes |
|---|---|---|---|
| base (no lip) | 1 | PLA brass | about 1 h; two fit on a bed |
| back plate (black floor + brass, arrow by hand) | 1 | PLA | about 53 min; two fit on a bed |
| deck, cover (smooth rim), plain ring (gate) | 1 each | PLA brass; ring PETG | gated by the knob test |
| gate strips | 6 (+ spares) | PETG | press-fit feet v2 |
| outer ring, inner ring | 1 each | PLA black + ivory | one colour change at layer 29 |
| index cap | 1 | PLA brass + ivory arrow | change at layer 13 |
| keystone (knob) | 1 | PLA brass | held for the screw measurements |
| tiles (4) + digit inlay | 1 set | PLA ivory + black | as tested |
| pawls | 4 | PETG | 1.4 mm |
About 4.5 to 5 h per instrument, about 19 h for four (about 24 h with spares). Filament for four with spares: about 610 g brass, 165 g black, 50 g ivory, 15 g PETG (plus colour-change purge, 15 to 20 %). Hardware for four: 16 M3x8 and 12 M3x16 black socket screws, 4 M3x10 knob screws, 4 nuts, 4 hex keys (2.5 mm), 4 UV flashlights and discs (plus spares). **Owner inventory is not assumed.**

**Print status (owner-reported):** back plates: 2 done (9:00 PM Tue), 2 (+1 spare) to go. Bases: 3 printing tonight, 1 (+1 spare) to go. Everything else not started or unknown (the owner has not yet said what rings, caps, tiles, pawls already exist).

**Owner capacity (assumption to confirm):** weekdays one print job in the morning, which runs until the owner returns from work that evening; evenings and weekends free. One printer.

**Schedule (revised for the 29th):**
| Date | Plan |
|---|---|
| Tue 17 | Plates (done); 3 bases tonight |
| Wed 18 | Morning: 2 more back plates. Evening: PETG strips and gate seat v2, then **knob test** |
| Wed night to Thu 19 | **Decision gate or latch; freeze files** (deck, cover, ring queue next) |
| Thu 19 to Sun 22 | Decks, covers, rings, caps, tiles, pawls, strips, keystones. **Pilot instrument assembled first** |
| Mon 23 | Test all four, both play orders, with the real journal proof |
| Tue 24 | Reprints, host kit |
| Wed 25 | Preparation complete as last stated (confirm) |
| Thu 26 | Thanksgiving buffer |
| Fri 27 | Extra test day, or the new deadline if it moved |
| Sat 28 | Final check, pack kits |
| **Sun 29** | **Hunt** |

## 7. Files
Repository: `WWCPIMLawrence/2026---Chronometer-`, branch `claude/brave-ramanujan-dc57dr` (it may be reachable as `Adventures` after a rename). Download folder: `downloads/` (combined zip `ALL_LATEST_2026-11-17.zip`; print files in `chronometer_production_candidates_v1.zip`, folders A to I; `PRODUCTION_PLAN_2026-11-17.md`; `PRINT_CHECKLIST.md`; `APERTURE_DESIGN.md`; `reference/` JSON and template). Baseline (old separate-mask design) is commit `09dfe49`, with exports in `stl/legacy/`. The CAD defaults are the integral asym_v1 plate; the gate, latch and ring variants are optional parameters, off by default. All production files are **pre-freeze**.

## 8. Open items and owners (the critical path)
| # | Item | Owner | Needed by |
|---|---|---|---|
| 1 | Knob test: gate or latch | owner | Wed 18 evening |
| 2 | Phillips screw head size (or keep the socket-head pocket) | owner | Thu 20 |
| 3 | Two missing documents: the journal page physical-fit update and the asym_v1 instructions/test PDF | owner / Work | now (not yet received by Claude Code) |
| 4 | **Journal proof built from the frozen coordinates, then a physical read with the plate, both orders** | Work, owner | before Mon 23 |
| 5 | Blind-pair and recoverability tests | owner, Work | by Fri 27 |
| 6 | Clue wording for the gate ("press the dial in and turn it back") | Work | before print of host material |
| 7 | Whether the Wed 25 preparation deadline moved | owner | now |
| 8 | Owner inventory: what is already printed, filament, screws, keys, lights | owner | now |
| 9 | Smooth cover rim: acceptable? | owner | Wed 18 |
| 10 | Real print times for bases and decks (calibration) | owner | as printed |

## 9. Risks (for scheduling)
- **Gate fails the knob test:** fall back to the three-arm latch parts (same print time). Low schedule cost.
- **Journal proof shows a problem:** only the back plate is involved; a reprint is about 1 h each. Keep Wed 18 to Mon 23 flexible.
- **Printed springs:** their stiffness and life are estimates, not measured. They are consumables (36 planned); a healthy locked cover stands 1.2 mm proud, which doubles as an inspection indicator.
- **Owner time:** one job per weekday morning limits the throughput of long parts; weekends are the production window.
- **Unvalidated numbers:** press force, gate wall engagement under print droop, glare and opacity outdoors.
- The hunt moved by two days after the plan was made: the new slack is testing and reprint time, not new work.

## 10. Remaining engineering work (Claude Code)
Build and check production files after the knob test (deck, cover, ring and strips for G, or L); keystone pocket after the screw measurements; freeze the master files; apply any fixes from the owner's tests; keep the checklist current. Not planned: a general redesign, changes to the frozen coordinates, or changes to the proven mechanics.

## 11. What the other tool is asked to do
1. Confirm the journal page uses these exact coordinates and the no-mirror convention; keep decoy letters clear of every hole centre; send the page and its test PDF.
2. Plan the weekday/weekend print and test calendar from sections 6 and 8, with the owner's one-morning-job limit.
3. Write the gate clue and any host instructions for the plate removal and refit.
4. Define the blind-pair test and who runs it, with pass criteria.
5. Tell Claude Code anything in section 2 that has changed.
