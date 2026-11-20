# M-72 Surveyor's Observation Plate V2: CAD preview for Keeper and owner review (20 Nov 2026)
Response to Keeper's V2 handoff. **CAD preview and predictions only. Nothing printed. Do NOT print until Keeper and the owner approve the look (Step 2).** V1 is kept untouched as the rollback.

## 1. Can the requested features be added while preserving the tested interface? **Yes.**
V2 **only removes material** from V1: shallow engraving in the top face and five small rim notches. CAD proves it (`chk_v2_adds_nothing`: V2 minus V1 is empty). Everything the physical test validated is unchanged: the three-cup seating bosses (4.6 x 1.9 mm heads), the p4/p8/p10 window positions and sizes, the fixed-arrow window, the plate outline and thickness (124 x 124 mm, body 2.0 mm), clearance to the rings, index cap and the gate-raised centre cover (all EMPTY), and the heads still hold the plate up (SOLID). The Chronometer is not modified.

## 2. What V2 adds (dimensions)
| Feature | V2 |
|---|---|
| **Orientation notches** | The Chronometer's own rim-notch shape and positions: **double at 12 o'clock (CAD 87 and 93 deg), single at 3, 6 and 9**. A 1.8 mm square rotated 45 deg at the rim: about 2.5 mm wide, 1.3 mm deep, through the 2.0 mm thickness; nearest window 30 deg away. |
| **Concentric grooves** | **Engraved**, as Keeper prefers: four fine circles at r 40.6, 41.4, 47.6 and 48.4 mm, 0.5 mm wide, 0.4 mm deep, in the web between the symbol and numeral windows (they stop at the windows). |
| **Title rules** | Four thin engraved arcs (r 51.8 and 58.4) framing each title: 66 deg around 12 o'clock and 88 deg around 6 o'clock. |
| **Title text** | Engraved, 0.4 mm deep, **"WREN & CO."** on the upper arc (letters stand outward, centred at 12 o'clock) and **"SURVEYOR'S PLATE"** on the lower arc (reads left to right, tops toward the centre). Font Liberation Serif Bold; capitals about 4.2 mm tall; band r 53.0 to 57.2 mm; nothing else is written. |
| Colour | Brass, unchanged. |
Files: `m72_sight_plate_V2.scad` (source), `m72_PLATE_V2_decorated_NONPRODUCTION.stl` (print file, top face down like V1), V1 files unchanged.

## 3. Departures from the tested geometry
None except removal: engraved detail, and five rim notches that take about 1.3 mm out of the rim at five places. The plate loses 0.36 cm3 (17.26 to 16.90 cm3, about 2 %): rigidity and seating are unaffected in the CAD.

## 4. Print time and material (estimates, not measured)
Same as V1: about 17 cm3, about 21 g if solid (less with infill), roughly an hour; one plate, existing brass PLA, top face down (no supports).

## 5. Risks and compromises (for Keeper's decision)
1. **Engraved brass-on-brass is low contrast.** The lettering shows by shadow and sparkle, not colour. Legibility at handling distance is expected but not proven; the preview shows it with a render shader. **Option:** engrave 0.6 mm deep (three layers) for stronger shadow, at a slight cost in strength; I kept 0.4.
2. **Fine serifs and the thin strokes** (hairlines about 0.25 mm) will not print crisply with a 0.42 mm line; bold capitals at 4.2 mm should still read. A slightly larger size (for example 5.0) fits only by crowding the windows.
3. **Elephant-foot compensation (0.15 mm) on the bed-side face** may widen the first layer of the grooves and text a little (a small step in the groove profile). Visible only on close inspection.
4. **Rim notches** match the Chronometer's, but the Chronometer's real notches are hidden under the outer ring from above; here they sit on the visible plate edge, which is what Keeper wants.
5. The text is **approximately** spaced (letter widths from the font, not kerning); check the look on the print.

## 6. Decisions requested
(a) Approve the look (or ask for a change); (b) engraving depth 0.4 or 0.6 mm; (c) approve printing ONE V2 test plate. **Four-unit production stays on hold.** The existing V1 plate remains the fallback.
