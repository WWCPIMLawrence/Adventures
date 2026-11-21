# M-72 Surveyor's Plate V2c — print-quality refinement (Cog → Keeper, 21 Nov 2026)
V2c is a TEST design. V2b (files 14c/14d, source m72_sight_plate_V2.scad) is unchanged and stays the fallback. Body, windows, chamfers, cups, bosses, notches, outline, diameter and thickness are identical to V2b; only the decoration inlaid in the top 0.4 mm changed.
All numbers are CAD calculations or slicing estimates; nothing here is a physical result.

## 1. Why V2b printed badly (CAD analysis; slicer cause is a hypothesis for the owner to test)
1. **The rings were two PAIRS of 0.5 mm lines with only a 0.3 mm brass gap between them.** Below one nozzle width, so the colours smear into one blobby line. Each line is also only ~1.2 extrusion widths.
2. **Lettering strokes are too thin.** In Liberation Serif Bold at 4.6 mm, 21.8 % of the letter area is thinner than 0.4 mm and 27.6 % thinner than 0.5 mm (hairlines, serif tips).
3. **Ring graze:** the inner ring ran along the fixed-arrow window edge and left thin black slivers (0.8 mm² in the CAD check).
4. **Slicer suspect (not CAD):** the decorated face is layer 1. Elephant-foot compensation (0.15 mm) shrinks layer-1 outlines on both colours, so a 0.5 mm black line can print ~0.2 mm narrow with a gap to the brass. First-layer squish and brass/black flush contamination add to this.

## 2. What V2c changes (CAD)
| Feature | V2b | V2c |
|---|---|---|
| Rings | 4 lines: r 40.6, 41.4, 47.6, 48.4, each 0.5 wide, 0.3 gap in each pair | 2 continuous lines, 0.8 wide: r 41.0 (40.6-41.4) and r 48.0 (47.6-48.4) |
| Arc rules (r 51.8, 58.4) | 0.5 wide | 0.8 wide (0.8 mm clear of the lettering) |
| Ring ends at arrow window | graze edge, slivers | stop 0.5 mm short of the window sides, square ends |
| Lettering | same font, size 4.6, track 0.5 | same font and wording, size 4.35, every glyph grown 0.12 mm all round (rounded corners), track 0.7 |
| Cap height | 4.18 mm | 4.19 mm (same visual size) |
| Letter area thinner than 0.4 mm | 21.8 % | 0.4 % |
| Letter area thinner than 0.3 mm | 4.1 % | 0.2 % |
| Total ink area of lettering | 156 mm² | 200 mm² |
| Smallest gap between adjacent letters | n/a | about 0.3 mm (checked, none below 0.2) |
| Inlay depth | 0.4 mm (2 layers) | 0.4 mm (unchanged) |
Line width: 0.8 mm = two 0.4 mm lines, so the slicer lays two clean parallel passes (0.7 mm would be stretched/squeezed). If the owner's nozzle is not 0.4 mm, tell me (UNKNOWN to me).
Rings reduced from 4 to 2; rule arcs unchanged in position. The decorative character (concentric rings + two framing arcs) is kept.

## 3. Checks (all in OpenSCAD, empty = pass)
- Nothing added outside the original plate body: EMPTY. No gap between brass and black bodies: EMPTY. Brass never gains material vs V2b body: EMPTY.
- Black part is now a clean manifold (watertight); the first V2c draft was not, until the ring-end cut was added.
- Letter-to-letter gaps below 0.2 mm: none. Windows/notches/cups/bosses untouched, so XII/STAR → IV/TREE, VIII/SUN, X/KEY and DIAMOND 11:11 are unaffected (same geometry as V2b).
- Remaining thin spots: lettering corner tips (0.84 mm², rounded, slicer ignores). 
- Sizes: black 0.348 cm³, brass 16.89 cm³ (V2b 0.340 / 16.90). Bbox 124 x 124 x 3.3 mm, starts at z=0.

## 4. Slicer settings to try (Bambu Studio, P1S; I could not run the owner's slicer here)
CAD-fixable (done): ring pairs, thin strokes, ring/window graze. Slicer-fixable (do these):
- Same matte plate; set the plate type in the slicer to match it (bed temp).
- Import `14e` + `14f` as ONE multi-part object, top face down, no rotation. Black = black PLA, brass = brass PLA.
- Layer height 0.20, first layer 0.20 (inlay = exactly layers 1 and 2). Line width 0.42 default is fine (rings = two lines).
- **Elephant foot compensation 0 for this plate only** (hypothesis; restore 0.15 for the fit parts afterwards). XY contour/hole compensation 0.
- Initial layer speed <= 30 mm/s; outer wall <= 60 mm/s; detect thin walls ON; wall generator Arachne; ironing OFF; supports OFF.
- Colour changes: black prints before brass in a layer; keep the prime tower; raise flush volume brass→black (glitter). Check the preview.
- In the preview, look at layers 1-2: black lines continuous, no gap at the brass/black boundary, rings two clean passes, letters solid.
Result: if V2c still shows blobs with elephant-foot comp 0, the cause is the nozzle/extrusion on the matte surface, not the CAD.

## 5. Print time (estimate, V2b time was not reported)
Same volume as V2b, so about the same as the owner's V2b print; my guess is ~1.5-2.5 h with the colour changes in layers 1-2. Please report V2b's actual time.

## 6. Test and decision
One V2c test print, compared directly with the matte V2b: legibility at arm's length, ring continuity, finish, seating, XII/STAR readings IV/TREE, VIII/SUN, X/KEY. If no substantial improvement: keep best V2b, stop cosmetic iteration. Remaining plates stay on hold.

## 7. Files
`downloads/M72_V2c_Test_Print/`: `14e_M72_PLATE_V2c_part1_BLACK_inlay.stl`, `14f_M72_PLATE_V2c_part2_BRASS_plate.stl`, source archive zip, previews (top view, upper/lower close-ups, V2b upper close-up for comparison). Source: `concepts/m72_attachment/m72_sight_plate_V2c.scad`.

## 8. Chronometer production note
Owner is printing the parts for the fourth team Chronometer overnight and one of three parts to turn the prototype into a fifth Chronometer. Recorded as an OPTIONAL SPARE, not a fifth team requirement.
