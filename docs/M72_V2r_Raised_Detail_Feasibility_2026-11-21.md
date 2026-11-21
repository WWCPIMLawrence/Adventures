# M-72 plate — raised black lettering/rings: feasibility review (Cog → Keeper, 21 Nov 2026)
STUDY ONLY. No STL is released and nothing is to be printed until Keeper and the owner review this. The dark matte V2b/V2c plate remains the fallback; no approved geometry is changed. Figures are CAD calculations or estimates; I have no physical result for raised detail.
CAD preview: `downloads/M72_V2r_Raised_Feasibility/` (oblique, top view, upper-title close-up) and source `concepts/m72_attachment/m72_sight_plate_V2r.scad` (parts exist only as previews/analysis).

## Bottom line
Raised black detail is feasible as a design: heights, widths, windows, notches and clearances all work. The cost is the print ORIENTATION. Raised features need the plate printed FACE UP, which (a) needs supports under the whole plate because the three screw-seat bosses hang 1.3 mm below the plate, and (b) puts the visible face on a top-surface layer instead of the matte build plate, i.e. it gives back the low-reflectivity finish that the matte plate just gave you. I recommend NOT starting a raised-detail plate unless Keeper/owner accept that trade; the cheaper path is one more face-down V2c print with the slicer changes already listed.

## 1-2. Raised heights (0.4-0.6 lettering, 0.3-0.4 rings)
- Practical heights are layer multiples at 0.20 mm: lettering and rule arcs 0.4 (two layers) or 0.6 (three); rings 0.2 or 0.4. Recommended: letters 0.4, rings 0.4. (0.3 is not a layer multiple; use 0.2 or 0.4.)
- Raised features sit only on the flat top face and stay 0.3 mm clear of every window's chamfered opening and of the fixed-arrow window. CAD checks: features over windows EMPTY; features overlapping the plate's own footprint EMPTY.
## 3. Minimum widths (0.4 mm nozzle assumed; owner's nozzle UNKNOWN)
- A single extrusion line is about 0.42-0.45 mm. Reliable raised detail: >= 0.5 mm as one line, >= 0.8 mm as two lines (no gap-fill). Hairlines/serifs below 0.5 mm will be skipped or beaded.
- V2c lettering (strokes grown 0.12 mm per side) has only 3.9 % of its area below 0.5 mm and 0.4 % below 0.4 mm (V2b: 27.6 % and 21.8 %), so it is usable raised as-is. Rings/rule arcs at 0.8 mm = two clean passes. No narrower than 0.8 mm for any raised line.
## 4. Face-up with a late black colour change
- Practical. The brass body finishes at the plate top (z = 2.0 above the plate underside); every layer above it contains only black, so there is ONE filament change, not several (the current inlay needs changes in layers 1-2). Fewer changes, less purge; brass-in-black specks at the first black layer are still possible, mitigated by the prime tower/flush volume.
- Matching the Chronometer's raised numerals: those are printed the same way (face up, late change). Whether the owner's AMS applies a layer colour change automatically or needs a multi-part/second-object setup is UNKNOWN to me; the multi-part method used for the plate works.
- Hazards: black stringing across the brass between letters (retraction, travel avoidance), and a glossy top surface (see 5).
## 5. Underside cups face up?  No: they face the bed.
- Modelled face up, the bosses (7.6 mm) and cups (5.2 mm, open downward) are on the build plate side. The plate body then floats 1.3 mm above the bed on three small bosses: supports are needed under the whole underside: about 8,600 mm² (annulus minus windows) x 1.3 mm = ~11 cm³ envelope, in practice perhaps 2-4 cm³ of support plus interface layers, and extra print time (guess +30-60 min). The underside would be rough (not visible; clearance to the rings is 0.8 mm, so it is acceptable).
- Each cup roof is a 5.2 mm bridge or must be supported: bridge sag of about 0.1-0.2 mm changes the seat height, and support inside a 1.4 mm deep cup is awkward to clear. The cups are the accuracy-critical feature, and they print best in the CURRENT face-down orientation (open upward, no supports).
- Finish: the visible top would be a top-surface layer (glossier, layer lines), not the matte-plate texture the owner just preferred. Bed texture would end up on the hidden underside.
## 6. Interference and handling
- Nothing sits above the plate near r 41-59: the centre cover is r <= 27.8 and the rings are below the plate. CAD check of raised features against rings, index cap and cover: EMPTY (no interference). Plate top rises to z 2.4 (0.4) or 2.6 (0.6) above the underside.
- Handling: raised black on brass can be scratched by a fingernail and may print-stack/rub if plates are stored together; keep raised height at 0.4. No effect on windows, notches or the XII/STAR readings.
## Options for Keeper/owner
A. Stay face-down: one more V2c print (slicer changes: elephant foot 0, slow first layer, thin-wall detection). No supports, matte finish, cups exact. Likely cleanest path; the N defect is one print failure, not a design limit.
B. Raised, face-up: letters/rings 0.4 raised, supports under the plate, glossy top, one colour change. Test plate needs Keeper approval; I would first print only a small coupon (a 40 mm arc with WREN and one ring) to judge appearance before a full plate.
C. Keep the dark matte plate as the fallback in all cases.
