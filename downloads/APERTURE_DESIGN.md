# Aperture design record (chosen 16 Nov 2026; first physical results 17 Nov, validation still partial)

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

## Physical results so far (owner-reported, 17 Nov 2026; one two-colour plate, printed from the CAD exports)

| Test | Result |
|---|---|
| Print quality | No print problems. Black floor and brass plate bonded cleanly. |
| Hole diameters (calipers) | **Four main holes 10.5 mm each; sighting hole 2.5 mm** (owner readings, 17 Nov; to caliper resolution, not individually recorded) |
| Flatness | Lies flat on a table |
| Black floor bond (pry test) | No issues |
| Fit on the existing base, repeated refits | No issues (plate fits the base printed before the lip) |
| Arrow at 12 o'clock | Coloured bone-white **by hand** (top two layers of the 0.4 mm pocket); matches the other indicators. Manual colour change accepted; no extra export body needed |
| Letters on the 1:1 template | **Passed.** Template printed on 8.5 x 11 at 100 %; the R, I, F, T lettering and the circles match the plate's holes (owner, 17 Nov). This confirms the coordinates, reading order and orientation on paper at 1:1; it is the engineering template, not the journal proof |
| Real journal proof, both play orders, blind-pair and recoverability tests | **Not yet tested** |

**Still to validate:** glare and opacity outdoors, the real journal proof in both play orders, and the blind-pair and recoverability tests. Nothing here may be called production-approved until the template and journal-proof tests pass.

**Not changed:** the gate, latch and ring variants remain OFF by default; the pin hole stays 4.6 mm; the flashlight bay, screws (M3 x 8) and rings are untouched.
