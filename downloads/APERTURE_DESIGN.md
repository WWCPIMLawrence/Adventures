# Aperture design record (chosen 16 Nov 2026; physical validation pending)

**Chosen design:** a one-piece back plate with the optical aperture printed into it. A 1.2 mm floor, flush with the sheet, back face on the bed,
carries four 10.5 mm holes and a 2.5 mm sighting hole at the asym_v1 coordinates. The separate mask, its spring arms, ledge, click groove, key slot and the
base's retaining lip are gone.

| | |
|---|---|
| Coordinates | `reference/aperture_geometry.json` (frozen). View from above, +X right, +Y toward the double notch (12 o'clock), no mirror for a face-up sheet. |
| Reading order | From the double notch, clockwise: R (7.053, 9.708), I (14.095, -5.130), F (-4.603, -9.437), T (-12.977, 3.721) |
| CAD defaults | `aperture_pattern = "asym_v1"`, `aperture_integral = true`, `plate_floor_t = 1.2` |
| Exports | `stl/back_plate.stl` (single body), `stl/back_plate_black.stl` + `stl/back_plate_brass.stl` (two bodies for AMS), `stl/base.stl` (no lip), `stl/aperture_coupon*.stl` |
| Retired baseline | symmetric cross + separate mask: commit `09dfe49`, exports in `stl/legacy/`, switchable with `aperture_integral = false`, `aperture_pattern = "cross"` |
| Automatic checks | `scripts/aperture_check.py` reads the holes back from the exported plate (centres 0.02 mm, diameters) and is run by `build.sh check`. `chk_floor_in_base` and `chk_plate_base` check the floor and plate against the base |
| Reuse | The integral plate has zero interference with the base printed before the lip (commit `4f7b7db`); the plate/base interface is unchanged. Not yet confirmed physically |

**Not yet validated physically:** printed hole diameters, flatness and opacity, black-to-brass bond, plate refit repeatability, the letters through the real journal
proof, both play orders. Nothing here may be called production-approved until the coupon, a whole plate on a base, and the journal proof pass.

**Not changed:** the gate, latch and ring variants remain OFF by default; the pin hole stays 4.6 mm; the flashlight bay, screws (M3 x 8) and rings are untouched.
