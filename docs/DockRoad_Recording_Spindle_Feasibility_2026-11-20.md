# Dock Road recording spindle: feasibility and recommended dimensions (non-production, 20 Nov 2026)
Answer to Keeper's feasibility request. CAD results are predictions; nothing has been printed. Secondary to T1-v1 and the four Chronometers: no production, no change to any existing component, no four-part run.

## 1. The actual cavity (read from `cad/chronometer.scad`, absolute heights above the bed)
- **Cover off (open well):** diameter 50.0 mm, depth 16.0 mm (plate floor top at 1.2, deck top at 17.2). The floor carries the four 10.5 mm holes and the 2.5 mm sight hole, so anything lying there covers them.
- **Cover on (what sits under the seated cover):** the free height is not 16 mm. It is **11.25 mm** in the outer annulus under the skirt (r 23.2 to 25), **13.3 mm** under the retaining ring (r 19.4 to 23.3) and **14.9 mm** at the centre (knob screw tip at 16.1). So the compact spindle must stay under about 13.3 mm tall to be stored beneath the cover.
- **Check against the owner's observation:** a cylinder of this size accepts an AAA (44.5 x 10.5, maximum length about 47.9 mm) and not an AA (50.5 x 14.5, maximum length about 46.8 mm). That matches what the owner found. **Length across the well is limited by the 50 mm circle, not by the depth.**

## 2. CAD fit results (spindle lying on the plate floor, centred, axis horizontal; checks in `concepts/dock_road_spindle/`)
| Spindle (across flats x length, end lips) | Open well, cover off | Under the seated cover |
|---|---|---|
| 17.5 x 42, lips 0.8 | fits | **collides** (too tall: 19.1 mm with lips) |
| 17.5 x 45, lips 0.8 | fits | collides |
| 17.5 x 47, lips 0.8 | **collides** (longer than the well chord) | n/a |
| 14 x 38, lips 0.8 | | collides |
| 13 x 40, no lips | | fits (13 + 1.2 = 14.2, under the 14.5 ring) |
| 12.5 x 42, no lips | | fits |
| 12 x 40, no lips | | fits |
| 11 x 40, lips 0.8 (12.6 mm overall) | | **fits** |
| 11 x 42, lips 0.8 | | fits |
| 10.5 x 44, lips 0.8 | | fits |
The checks run the spindle against the real base, deck, back plate, cover, retaining ring and knob screw tip, in the plain-ring configuration. No change to any of those parts.

## 3. Recommended dimensions
- **Compact (to travel inside the Chronometer, under the cover): 11 mm across flats x 40 mm long, end lips 0.8 mm proud.** Overall 12.6 mm tall lying flat; six faces each 6.4 mm wide; 38 mm of strip per turn; 36.8 mm between the lips for the strip. It fits under the cover with 0.7 mm to spare at the ring. **Keeper's preliminary 17 to 18 mm across flats cannot go under the cover** (it needs about 18 to 19 mm; the limit is about 13 mm without lips). A 17.5 x 42 spindle fits only with the cover off, which defeats a hidden location.
- **Full-size (travels in the Dock Road envelope): 22 mm across flats x 60 mm long, lips 1.2 mm.** Overall 24.4 x 28 x 60 mm; faces 12.7 mm wide; 76 mm of strip per turn; comfortable for hands and larger lettering.
- Alternative compact if more face width is wanted: 12.5 x 42 with no lips (retention by tape tabs); less strip control.

## 4. Features (all in `spindle_concept.scad`; none of it is production geometry)
- **Six winding faces:** hex section with 0.7 mm corner rounding; the ends chamfered; no sharp edges.
- **Starting orientation:** face 1 is the +X flat; a V-notch in both end lips marks it, so it is found by sight and touch.
- **Strip anchor:** a 0.7 mm radial slit 3 mm deep in face 1, clear of the lips, for the strip's tail (paper or film). Untested: the strip thickness and a possible tape tab.
- **End retention:** the lips stand 0.8 mm (compact) or 1.2 mm (full-size) proud on every side. This limits the build-up: about 8 turns of 0.1 mm paper on the compact version.
- Files (non-production): `spindle_C1_covered_AF11_L40_NONPRODUCTION.stl` (4.2 cm3), `spindle_C2_open_AF17p5_L42_NONPRODUCTION.stl` (11.2 cm3, open-well fit only), `spindle_F1_fullsize_AF22_L60_NONPRODUCTION.stl` (25.3 cm3).

## 5. Print requirements (estimates, not measured)
Print standing on its end (axis vertical): no supports, the hex footprints are 14 x 12.6 mm (compact) and 28 x 24.4 mm (full-size), so a thin tall part on a cold plate: use a clean plate and watch the first layers. PLA, any filament; the printer's earlier data point (cover plus seat, about 37 min for about 24 cm3) does not apply well to tall small parts. Rough guide: **compact about 25 to 35 min** (200 layers at 0.2 mm) and about 4 g; **full-size about 60 to 90 min** and about 30 g. One part per print; do not share a bed with other parts. Four copies of either size would be about 2 h (compact) or about 5 to 6 h (full-size): not requested or started.

## 6. Interactions to decide before anything is made (not engineering unknowns)
- **A loose object lying on the floor covers the four aperture holes.** Players must remove the spindle before reading RIFT; if the cover is put back with it inside, the part is trapped under the cover and rattles.
- **Plate removal for the UV flashlight** with the instrument upside down will tip the spindle out into the player's hand: natural, but it changes what the plate removal step looks like.
- **A rattle** is a giveaway; foam or a card sleeve would stop it (not designed).
- The spindle adds no mechanical load to the cover, ring or knob in these checks.

## 7. Open items and what Cog would do next (only if asked)
Which size and location Keeper wants; the strip dimensions (width up to 36.8 mm, thickness); one test print each of C1 and F1 once capacity allows. No change is made to any existing part.
