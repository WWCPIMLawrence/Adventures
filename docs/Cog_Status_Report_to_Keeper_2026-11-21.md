# Cog status report to Keeper — 21 Nov 2026
(CAD predictions and estimates are labelled as such. Nothing below is a physical result unless it says "owner measured".)

## 1. M-72 V2b production
- V2b is the final plate. Owner has ONE V2b printed and physically checked (XII/STAR → IV/TREE, VIII/SUN, X/KEY confirmed earlier on the V1/V2 plate; V2b check on all Chronometers still to be reported).
- Count: 1 of 4 done. **3 more to print**: files `14c` (black inlay) + `14d` (brass plate) imported as ONE multi-part object, top face down. Production sheet + per-plate QC: `docs/M72_V2b_Production_Sheet_2026-11-21.txt`.
- Print time of the V2b plate: NOT reported by the owner yet (UNKNOWN). Expected completion: three plates = ~3 print sessions; can finish in the next few days without touching Chronometer printing. V1 and V2 files preserved as fallbacks.
- Scribe ring data supplied: `docs/M72_Ring_Rotation_Data_for_Scribe_2026-11-21.md`.

## 2. Dock Road spindle CAD / STL
- Current: D1 (hex 17.0 mm AF x 56 mm, end lips 1.0 mm proud, 0.7 x 3.0 mm anchor slit in the VI/I corner, single notch bottom, double notch top). Source `concepts/dock_road_spindle/spindle_concept.scad`.
- STL ready for the paper baseline test print: `downloads/15_DOCK_SPINDLE_D1_later.stl` (same as `spindle_D1_handling_AF17_L56_NONPRODUCTION.stl`). Prints standing on end, double notch up, no supports. Paper strip sheet is Scribe's frozen content (7.927 x 243.4 mm incl. tabs).

## 3. Spindle print time (estimate, not measured)
14.1 cm³ → roughly 12–18 g PLA, ~60–90 min with a small brim. Owner's first print gives the real number.

## 4. Issues with the original paper winding design
None found in CAD. Untested items: (a) tab retention in the 0.7 mm slit; (b) four-turn alignment with a real 0.116 mm sheet (CAD: strip 237.2 mm, helix 7.75°, 24 cells at 9.883 mm); (c) readability of the 7.9 mm window while wound. Paper baseline test (Step A) answers all three. Paper remains the fallback.

## 5. Measurements needed for a leather variant (owner, with calipers)
1. Thickness at 5+ points (grain/flesh sides, edge), olive and black separately.
2. Strip width actually obtainable (10–12 mm preferred) and edge straightness.
3. Wrap test on a ~17–20 mm tube: does it follow the faces/corners, or spring back?
4. Stretch under hand winding tension (mark 100 mm, pull gently, re-measure).
5. 1/4 in stamp: impression depth and clarity on grain vs raw backing; contrast on black vs olive; strike on a firm backing board.
6. Wound strip length for four turns (measure, don't compute).

**Assessment (CAD estimate):** D1 usable length between lips = 52.8 mm. With butt-wound turns the axial envelope is 4·pitch + width:
| width | envelope | fits D1? |
|---|---|---|
| 8 mm | 40.2 mm | yes |
| 10 mm | 50.4 mm | yes (tight) |
| 11 mm | 55.5 mm | NO |
| 12 mm | 60.7 mm | NO |

Also, for ~1.59 mm leather (assumed, not measured) the perimeter grows from 58.8 to ~63.4 mm, four-turn length ≈ 256–258 mm, and the 0.7 mm slit / 1.0 mm lips are too small. So: D1 probably works only for a ≤10 mm strip with a different retention; 11–12 mm strips need a leather-specific variant (longer ≥ ~62–66 mm, lips ≥ ~2.2 mm, slit ≥ ~2 mm or alternate retention). I will NOT design it until thickness/width are measured.

## 6. Other dependencies that could threaten 29 Nov
1. T1-v1 formal acceptance (50 cover cycles, 20 knob cycles, 12 detents, plate removal, both visit orders, unit B) not yet reported — gates Keeper's production release.
2. Four-unit production not yet authorised; part counts for covers/strips/pawls/nuts/screws UNKNOWN; short on 1 back plate, 1 inner ring, 1 index cap; 1 knob reprint; covers need nuts + UV writing.
3. Knurled-cover test print + retest still outstanding.
4. Music House real-leaf optical test blocked: Scribe's package (04_MusicHouse_Complete_Current_Review_2026-11-19_Rev2.zip) never received.
5. V2b seating on all four Chronometers (cap-screw heads vary with assembly) — unreported.
6. Leather arrival ~21 Nov and weekday printer time limits; leather must not displace the paper fallback.
