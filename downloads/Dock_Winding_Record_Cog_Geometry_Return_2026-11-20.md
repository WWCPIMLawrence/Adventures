# Cog to Scribe / Keeper: Dock Winding Record, selected spindle geometry (one prototype), 20 Nov 2026
Answers the geometry request in "Dock Winding Record Pre-Geometry Review, Rev 2". **All values are CAD or arithmetic predictions for ONE prototype. Nothing has been printed or wound; no paper fit is confirmed.** Paper stock thickness is an **assumption (0.10 mm) until measured.** No Chronometer part is changed; no key, shutter, magnet, clip or hidden mechanism is added.

## Selection
**Handling-size spindle "D1": 17.0 mm across flats x 56 mm long, 1.0 mm end lips.** (`spindle_D1_handling_AF17_L56_NONPRODUCTION.stl`; `concepts/dock_road_spindle/spindle_concept.scad`, `sp_af=17 sp_len=56 sp_lip=1.0`.)
Why this size and not the others:
- It **travels in the Dock envelope**. The compact spindle (11 mm) fits under the Chronometer cover in CAD, but that would make the spindle depend on the **unaccepted cover action** and, loose in the well, covers the aperture holes. Your handoff forbids both. Compact storage is left as an optional extra *after* retrieval.
- The full-size 22 mm model I first sketched would need about **305 mm of strip** for four turns, which does **not fit on a Letter page** (279.4 mm). D1 needs about **241 mm of encoded strip** plus tabs.

## Your table
| Required value | Answer |
|---|---|
| Selected file / facet widths / perimeter | File above. Across flats 17.00; across corners 19.63 (sharp), faces 9.82 mm per side sharp; **flat part of each face 9.01 mm** (corner radius 0.7 mm). **Sharp perimeter 58.89 mm; rounded path 58.44 mm** (use the rounded one). |
| Usable straight winding length | **52.8 mm between the end lips** (lips 1.6 mm thick each at 56 mm). The anchor slit runs 50.8 mm (z 2.6 to 53.4 from the bottom end). |
| Winding pitch (axial advance per full turn) | **8.0 mm per turn.** Helix angle 7.80 degrees at the first turn. Strip cut width **7.93 mm (cut 8.0 mm ±0.1)**. Four-turn axial envelope 4p + w cos(alpha) = **about 39.9 mm**, well inside 52.8. |
| Start contact datum / phase | **Cell 1 is centred on the middle line of the Face I flat, 4.0 mm below the inner face of the top lip.** Face I is the flat that carries the V notch in each lip. |
| View, handedness, advance | View **from the top end** (the end with the **double** notch; the bottom end has a single notch). Faces I to VI run **clockwise** as seen from the top end. The strip winds **clockwise seen from the top end and advances toward the bottom end**: a **right-handed helix**, like a normal screw thread. |
| Reading order / which end is top | Top end is the double-notch end. Hold it top end up, Face I toward the reader: Face I (cells 1, 7, 13, 19) reads **M, O, O, N from top to bottom** (turn 1 at the top). Face II reads AT, Face III reads 8:14, clockwise from Face I. |
| Start/end retention and tab allowances | **No clip, glue or loose part.** A 0.7 mm slit, 3.0 mm deep, runs along Face I. **Start:** an unencoded start tab of 4 mm is tucked into the slit at the top of turn 1. **End:** after cell 24 (Face VI) the strip reaches Face I again; an unencoded 4 mm end tab is tucked into the **same slit** at the bottom of turn 4. The tab positions differ by about 32 mm along the slit. The winding itself holds the tension. **Untested: whether the tucked tabs stay put without finger tension.** |
| Stock and total thickness | **ASSUMED 0.10 mm ordinary matte paper.** The perimeter grows by 2 pi x thickness per turn: turn centreline perimeters are 58.75, 59.38, 60.01, 60.64 mm. **Measure the real stock and tell me; I will recompute.** Lamination was not assessed here: a laminated strip will not tuck into a 0.7 mm slit more than one thickness deep. |
| Physical readability from one print | **Not done.** One print and a real winding are needed. |
| Compact storage dimensions | Not selected for this prototype. If later wanted: 11 x 40 mm with 0.8 lips fits under the seated cover in CAD (see `DockRoad_Recording_Spindle_Feasibility_2026-11-20.md`); the strip for it would need a different, shorter cut (about 180 mm) and about 6.5 mm width. |

## Per-turn developed strip figures (zero-gap helix, 0.10 mm paper assumed, from the CAD perimeter)
| Turn | Centreline perimeter | Strip length per turn | Cell interval (equal six per turn) |
|---|---|---|---|
| 1 | 58.75 | 59.29 | 9.88 |
| 2 | 59.38 | 59.92 | 9.99 |
| 3 | 60.01 | 60.54 | 10.09 |
| 4 | 60.64 | 61.16 | 10.19 |
Encoded centreline total **240.9 mm** (235.9 with zero thickness); add the two 4 mm tuck tabs and a margin: about **250 mm strip**, so it fits a Letter page's long side with about 14 mm to spare. Cell height available (strip width 7.93 mm) fits Scribe's 2.5 to 3 mm capitals with about 2.5 mm margin above and below. Faces are 9.0 mm wide (flat part) against a cell interval of about 10 mm along the strip.

## Print requirements for one spindle (estimates, not measured)
Print **standing on its end** (top end up), PLA, no supports. Footprint 19 x 21.7 mm and 56 mm tall: a tall small part, so a clean plate and a first-layer watch. **Volume 14.1 cm3** (solid; real use less with infill, about 12 to 18 g). **About 60 to 80 min** by layer count (280 layers), unmeasured. One part, alone on the bed. A matching one-copy strip is Scribe's job after the owner measures stock thickness.

## What this does not do
Nothing here is authorised for four-copy production and it does not touch T1-v1, the four Chronometers, the aperture, or any existing component. If the winding fails (tab pull-out, corner springback, pitch drift), I report the failure rather than adding features.
