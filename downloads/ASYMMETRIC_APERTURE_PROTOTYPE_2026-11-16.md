# Asymmetric aperture and one-piece plate: prototype report (coupon only, not production)

Status: **proposal and coupon.** The approved baseline (symmetric cross, separate mask) is still the default in the CAD. Nothing has been
printed or tested. Frozen coordinates: `reference/aperture_geometry.json` (SHA-256 `a37d539b...3a8`; full hash in the package README).

## Pattern asym_v1 (view from above, +X right, +Y toward the double notch, origin = plate centre; no mirror for a face-up sheet)

| Order | Letter | x (mm) | y (mm) | bearing (clockwise from 12) | radius |
|---|---|---|---|---|---|
| 1 | R | +7.053 | +9.708 | 36 deg | 12.0 |
| 2 | I | +14.095 | -5.130 | 110 deg | 15.0 |
| 3 | F | -4.603 | -9.437 | 206 deg | 10.5 |
| 4 | T | -12.977 | +3.721 | 286 deg | 13.5 |

Reading order: start at the double notch (12 o'clock), sweep clockwise: R, I, F, T. Four round 10.5 mm holes; 2.5 mm centre sighting hole kept.

**Why this pattern:** bearing gaps 74/80/96/110 deg and four different radii, so there is no rotational or mirror symmetry (checked to 0.5 mm);
every hole is at least 16 deg from a notch axis, so no hole lines up with a notch line; the furthest hole edge is 20.25 mm, the same as the old
cross; hole-to-hole web 5.1 mm and hole-to-sighting-hole web 4.0 mm. I did not generate an alternative: the constraints leave a large family, and
the time is better spent on the coupon. **Asymmetry alone does not guarantee difficulty;** that needs the blind-pair tests below.

## What changed in the CAD (all options default to the approved baseline)

| Parameter | Default | Variant |
|---|---|---|
| `aperture_pattern` | "cross" | "asym_v1" |
| `aperture_integral` | false | true: 1.2 mm floor with the holes printed in the plate; no ledge, click groove, key slot or base lip |
| `plate_floor_t` | 1.2 | thickness of the floor (same as the mask it replaces) |
| `back_pin_hole_d` | 4.6 | unchanged; 4.2 is **proposed separately and untested** |

Parts: `back_plate`, `back_plate_black` + `back_plate_brass` (two exact, complementary bodies for AMS), `aperture_coupon` (+ `_black`, `_brass`),
`base` (lip and key slot removed in the variant). The `mask` part is unchanged and kept. `make_sheets.py` reads the `apertures` line and
was **not** touched, so the baseline sheets are unchanged; it cannot generate a sheet for asym_v1 (its lattice assumes the cross).

## CAD results

- **Baseline untouched:** all 30 default exports are identical in volume and bounding box; all 27 interference checks pass.
- **Hole positions from the real geometry** (cross-section of the exported plate): every hole centre is exactly at the table coordinates
  (error 0.000 mm); equivalent diameters 10.49 mm (64-sided circle) and 2.49 mm.
- **Variant checks, all empty (no overlap):** plate vs base, floor inside the base well, cover vs base, cover path, cover vs deck, knob vs cover, fragments vs cover.
- **Overhang inventory (downward-facing flat faces above the bed):** the baseline plate and the integral plate are the same: only the existing
  screw-counterbore ceilings (76.5 mm2 at z = 3.2 mm) and a 0.1 mm2 sliver. **No new bridge or overhang.** The floor sits on the bed.
- **Clearances:** the floor ends at r 25 mm. The flashlight bay's nearest edge is at r 29.5 mm, the screws and pin at r 54 mm, and the cover is
  at the top of the well, about 10 mm above the floor. Nothing in the UV pocket, the screw pattern or the gate changes.
- **Slicer (PrusaSlicer, generic profile, no supports used):** coupon 46 min, plate 3 h 28 min, base 4 h 04 min; the P1S is about 3x faster, so about 15 min,
  1 h 10 min (+ about 15 min for the colour changes) and 1 h 20 min.

## BOM and print effects

| | Change |
|---|---|
| Parts per instrument | one fewer (the mask); screws unchanged |
| Filament | plate +1.7 cm3 (floor); base -0.6 cm3 (no lip); mask -1.8 cm3 and its 5 minutes |
| AMS | 12 colour changes on the plate (6 layers x 2) and a purge tower; est. +15 min and about 2 g of waste |

## Tests before approval (none done yet)

1. **Coupon** (brass and two-colour): measure the five holes (10.50, acceptable 10.35 to 10.65 mm; sighting hole 2.50 mm), flatness, glare, opacity, bonding of the black floor, and the letters through the holes on the 1:1 template.
2. **One whole plate on your existing base** (no lip needed, interface unchanged): 20 removals and refits, with the holes' movement measured against crosshairs. Pass: 0.5 mm or less. Pin hole stays 4.6 mm unless that fails.
3. **Anti-shortcut:** give a blind pair the printed sheet alone, then the instrument without notch instructions. Not done; I make no claim about difficulty.
4. **Recoverability** with the intended clue, outdoors and in a car.
5. **Both orders:** aperture, plate off and on, aperture; and plate off and on, then aperture. The same letters both times.

## Risks and open items

- The sheet must be laid out from these coordinates (a different lattice from the cross). Decoy letters need to stay well clear of every hole centre (the old lattice kept 10.6 mm).
- The first-layer squish may shrink the holes by 0.1 to 0.15 mm per side; the coupon measures it, and I can open the holes if needed.
- The black floor bonds to the brass wall only along their shared edge; the coupon pry test checks it. If it fails I will add an interlock.
- A flush floor changes the optics from the 0.6 mm gap (parallax roughly halves, see the integrated-aperture review). The real RIFT sheet is still not on this side.
- I found no concrete reason to keep the symmetric design other than the existing sheet generator.
