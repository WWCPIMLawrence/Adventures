# M-72 removable calibration attachment: feasibility study (Cog to Keeper, 18 Nov 2026)

> **Update 18 Nov (evening):** the window sizes in this study were too small for the widest numeral (VIII); they are corrected, with test results to collect, in `M72_Sight_Plate_Evaluation_and_Paper_Test_2026-11-18.md`. The paper template was regenerated.

**Status: assessment and a non-production concept only.** No approved CAD, aperture coordinate, ring, fragment, cover or backplate geometry was changed. Everything new is under `concepts/m72_attachment/`. Not approved for production; not printed; not physically tested.

## Recommendation (ranked)
1. **Rigid printed "sight plate" (concept 2), tested first as a paper overlay (concept 1).** Both rest on the same idea: a flat annular plate that seats on the three fixed cap-screw heads and has windows over the two rings. Test the player experience with the **paper version tomorrow at the office** (no 3D printing, template attached), and print the rigid plates only if the paper test works.
2. Paper or film overlay (concept 1) as the fallback if rigid plates cost too much printer time.
3. Two-head sight bar (concept 3): works in principle, ranked last (tips, one window only).

**The two-ring dependency is real** (proof below). **One honest limit:** a passive attachment cannot create information the rings do not already show; the ring faces are visible with or without it. What it can do is (a) tell players *where* to read, (b) mask every other position, so the "observation" is one exact pair, and (c) provide a recovered-object moment. To make it **necessary**, the archival record must refer to the plate's windows (A, B, C), so the record is meaningless without it.

## What the CAD allows (read from `cad/chronometer.scad` and checked)
- **The only fixed, raised, uneven features on the top face are the three index-cap screw heads:** M3 socket heads, 5.5 mm across, 3 mm tall, at radius 45 mm, at CAD angles 25, 150 and 270 degrees (clock positions 2.2, 10.0 and 6.0 clockwise of the fixed arrow). Spacing 115 / 120 / 125 degrees.
- **Heights above the deck floor:** ring faces 5.6; numerals and symbols top out at 6.0; finger ribs 6.4; index cap 5.4 (arrow 5.8); screw head tops **8.4**. The cover is separate (radius 27.8, inner ring face starts at 28.3).
- **Registration is unambiguous (computed):** a plate with three cups or holes of 6.3 mm over the 5.5 mm heads seats in **exactly one orientation (within 0.5 degrees, about 0.4 mm at the heads)**. Turned 120 or 240 degrees, the heads miss by **3.9 mm against 0.4 mm of clearance**. A mirrored plate cannot seat. No glue, magnets, springs, purchases or precision assembly.
- **Rings stay free:** the plate hovers above the rings (see below), so the rings can still be turned, and the cover can be removed or pressed, with the plate on.

## The ring dependency, enumerated (script: `ring_dependency.py`)
Both rings have 12 positions on the same 30 degree grid, so at the calibrated setting (outer XII and inner STAR at the arrow) each clock position p clockwise of the arrow shows one numeral beside one symbol:
`p0 XII/STAR, p1 I/WAVE, p2 II/MOUNTAIN, p3 III/HOURGLASS, p4 IV/TREE, p5 V/COMPASS, p6 VI/DIAMOND, p7 VII/EYE, p8 VIII/SUN, p9 IX/MOON, p10 X/KEY, p11 XI/FLAME`.
- At **any single window**, the 144 possible ring settings give **144 different pairs**, so the pair identifies both rings.
- At a window at p6, **12 of the 144 settings show the right numeral, 12 show the right symbol, and only 1 shows both.**
- Nothing depends on XII being zero: numerals are used as printed.
- Single-ring errors give believable decoys. With windows A, B, C at p4, p6, p8:
  | State | A (p4) | B (p6) | C (p8) |
  |---|---|---|---|
  | **correct** (XII / STAR) | IV / TREE | VI / DIAMOND | VIII / SUN |
  | inner ring one click back | IV / HOURGLASS | VI / COMPASS | VIII / EYE |
  | inner ring one click on | IV / COMPASS | VI / EYE | VIII / MOON |
  | outer ring one click back | III / TREE | V / DIAMOND | VII / SUN |
  | outer ring one click on | V / TREE | VII / DIAMOND | IX / SUN |
  The record can list several of these lines with different observations, only one of which matches the *calibrated* state. (Scribe owns that wording; these are examples, not final.)
- Windows B and A/C are only a suggested sketch (positions are Scribe's choice). The correct state puts DIAMOND at p6, beside VI.

## Concept 1: windowed paper or film overlay
- **Principle:** a flat sheet with three round holes over the cap-screw heads and cut windows over the two rings; it lies on the rings' raised markings.
- **Visible at the correct and wrong settings:** as in the table above; the sheet itself carries no answer, only window labels.
- **Dependency:** real (above).
- **Fit risks:** paper sags between supports and rests on the ribs (6.4 mm), so turning a ring under it can drag it; holes tear after repeated use; flimsy to seat. No parallax (it lies on the markings).
- **Fabrication:** office laser printer plus knife and a 6.4 mm punch: about 5 minutes of hand work per overlay, about 30 to 40 minutes for six; **zero 3D-printing time**. Use heavy cardstock. A clear film window would need a purchase; plain cut-outs do not.
- **Template:** `concepts/m72_attachment/m72_paper_overlay_template_NONPRODUCTION.pdf` (print at 100 %, check the 100 mm bar).

## Concept 2: rigid printed "sight plate"
- **Principle:** same geometry in 2.0 mm black PLA: a 124 mm annulus (inner radius 29, outer 62), with **blind locating cups on its underside** that sit on the three screw heads. The plate hovers 0.8 mm above the tallest ring feature. Three window pairs (a symbol window over the inner ring, a numeral window over the outer ring, joined by a solid web that carries the cups), plus a small window that keeps the fixed arrow visible.
- **CAD fit checks (against the real assembly, all as expected):** zero overlap with the rings, the index cap, and the cover (also with the cover lifted 1.2 mm); the heads touch only the cup roofs; **sinking the plate 0.1 mm makes the heads collide (so they, not the rings, hold it up)**, and it is still clear of the rings at that depth.
- **Dependency:** real.
- **Fit risks:** relies on the cap screws being present and tight; head height varies a little (about 0.15 mm), which only changes the hover height; **parallax:** the plate top is about 3.2 mm above the numerals, so at 30 degrees off-axis the window edge hides about 1.8 mm of the feature (windows have only about 0.8 mm margin), which can clip a glyph at oblique angles. Mitigations: chamfer the window edges, widen the windows, or look from above.
- **Fabrication:** 17 cm3 of black PLA each (about 21 g), no supports, simple geometry. Estimate **about 40 minutes each, two per bed (about 80 min per bed); 5 plates (4 + 1 spare) is 3 beds, about 3.5 hours.** Uses one of the weekday slots. Not yet in the print queue.

## Concept 3: two-head "sight bar" (simplest hardware)
- **Principle:** a narrow rigid bar with two cups on two of the heads (for example the 25 and 150 degree heads, 80 mm apart) and one window pair at its far end.
- **Dependency:** real, but only one window pair.
- **Fit risks:** two supports let the bar rock about the line through the heads; the windows are limited to positions along a chord, not freely placed at clock positions; likely to need a third support.
- **Fabrication:** small and fast (about 10 minutes), but I would not recommend it.

## Checks against Keeper's constraints
| Constraint | Result |
|---|---|
| No change to existing CAD, apertures, rings, fragments, cover, backplate | **Met.** New files only, under `concepts/` |
| Preserve outer XII + inner STAR calibration | **Met** |
| Not dependent on XII as zero | **Met** |
| Attachment does not reveal the answer on its own | **Met** (windows only; the record carries the lines) |
| Result depends on both rings | **Met** (1 of 144 settings) |
| Unambiguous registration and orientation | **Met** by the three heads (one seat, 0.5 degrees) |
| No glue, springs, magnets, purchases, precision assembly | **Met** |
| Repeated attachment and removal | Plate: yes; paper: wears at the holes |
| Four instruments | **Met**, heads are the same on all four (the plate fits any unit) |

## Risks and unknowns (untested)
- Nothing here has been printed or tested; the plate hover and parallax need a physical look.
- The screw heads are modelled as plain cylinders; real socket-head screws should match (5.5 mm, 3 mm), but the owner's actual screws are not measured.
- The extra printing competes with the schedule (3.5 hours), and the plate is not in the print queue.
- Whether the puzzle is better with this attachment is a game-design call, not an engineering one.

## Decisions needed from Keeper
1. Approve the **paper test** first (template and geometry are ready; Scribe decides the window positions and the record).
2. If it works, approve printing 5 sight plates, and where in the queue they go (about 3.5 hours of machine time; suggested Mon 23 to Tue 24).
3. Confirm the window positions and number (A, B, C at p4, p6, p8 is a sketch only).

## Files
`concepts/m72_attachment/` (all non-production): `m72_sight_plate_concept.scad`, `m72_sight_plate_concept_NONPRODUCTION.stl`, `ring_dependency.py`, `make_paper_template.py`, `m72_paper_overlay_template_NONPRODUCTION.pdf`; picture `images/m72_sight_plate_concept.png`.
