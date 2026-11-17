# Phase 1 findings: CAD state vs the 16 November design decisions (no changes made)

Source: repository at commit `db84171` (branch `claude/brave-ramanujan-dc57dr`), inspected 17 Nov 2026.

## 1. Does the integrated asym_v1 aperture exist in the CAD?
**Yes, but only as an option.** Switched on with `aperture_pattern="asym_v1"` and `aperture_integral=true` (commit `648cfd8`).
Verified by cross-section of the exported variant plate: holes at R (7.053, 9.708), I (14.095, -5.130), F (-4.603, -9.437), T (-12.977, 3.721),
diameter 10.49 mm (64-sided circle for 10.5), sighting hole 2.49 mm at the centre, floor 1.2 mm, hole error 0.000 mm.
Also present: two-body exports (`back_plate_black` + `back_plate_brass`), an aperture coupon, the 1:1 template and `reference/aperture_geometry.json`.

## 2. Activation parameters and current defaults
| Parameter | Default now | Needed for the chosen design |
|---|---|---|
| `aperture_pattern` | "cross" | "asym_v1" |
| `aperture_integral` | false | true |
| `plate_floor_t` | 1.2 | 1.2 (already) |
| `back_pin_hole_d` | 4.6 | 4.6 (4.2 only if repeatability fails) |

**The normal exports still produce the old separate-mask design.** Default `back_plate.stl` has the open 44 mm window and no holes; default `base.stl`
still has the 1.4 mm mask lip; `mask.stl` (symmetric cross, four holes at 15 mm) is in the `build.sh` part list; `build.sh` has no black/brass plate parts;
the committed `stl/` files match the defaults exactly. Only the coupon zip's `3_LATER` folder contains the integrated plate and base.

## 3. Discrepancies between the CAD and the decisions
1. Defaults are the old cross and separate mask (above).
2. `build.sh`: three mask checks would fail or become meaningless with the integrated design (`chk_mask_base` fails: the floor overlaps the mask volume; `chk_mask_lip` and `chk_mask_springs` pass but test a part that no longer exists). All other checks pass under the variant.
3. `scripts/make_sheets.py` and the sheets in `sheets/` are for the old cross (the script reads the `apertures` line and assumes a letter lattice). They do not match asym_v1. (Work's journal page is the real sheet.)
4. README, print plan, materials and the earlier handoff PDFs still describe the separate mask.
5. The repo says the hunt is 26 November 2026 (README, handoffs); the latest handoff says 27 November. Please confirm. It does not change the engineering, but the schedule in my status document assumed the 26th.
6. Documents 4 and 5 in your list (`Music_House_RIFT_Journal_Page_Physical_Fit_Update_2026-11-16.md`, `Music_House_RIFT_asym_v1_Instructions_and_Test.pdf`) have not been sent to this session, so I have not reviewed them.

## 4. Physical printing or testing
**None, as far as the project shows.** The integrated plate and the coupon have never been printed; the only digital results are positions/diameters, interference and overhang checks.
Printed to date (from your reports): the gate parts and the plain ring (tested); the old base and plate with the separate mask (photos). The aperture coupon package was delivered; I have no results from it.

## 5. Reuse and reprint
- **Fits the base you already printed: yes, by CAD.** The integral plate has zero interference with the base from commit `4f7b7db` (the plate-mode base before the lip, which matches your photos),
  and the plate-to-base interface (bosses, pin, screw holes) is unchanged. Not yet physically confirmed. So **the existing base can be reused**, and the lip-less base in the package is only needed for the final units.
- **Reprint:** the back plate (new), and the base only if you want the final geometry (no lip, no key slot).
- **No longer needed:** the separate mask.
- **Unchanged and reusable:** both rings, pawls, deck, index cap, fragments, keystone, the gate parts and the covers.

## 6. Interactions
- **Center-cover gate and rings:** none. The gate, ring and cover change only the deck, cover and ring; the floor ends at r 25 mm and the cover skirt ends about 10 mm above it. Cover, knob, fragment and deck checks pass in the variant.
- **Bottom screws and plate seating:** four M3 x 8 at r 54, pin at 3 o'clock, bosses and counterbores unchanged. Plate vs base: no overlap.
- **Flashlight compartment:** the bay's nearest edge is at r 29.5 mm, the floor ends at r 25 mm; access and the light's seat on the plate are unchanged.
- **Overhangs:** the baseline and integral plate have the same downward-facing flat faces above the bed (the existing counterbore ceilings only). No new unsupported bridge.
- **Journal page note (not a CAD issue):** the page is 82 mm wide and the instrument is 125 mm, so the rim notches cannot register to marks on the page. Registration must come from the sighting hole over the printed cross plus the page's directional mark. The sighting hole is kept for that reason; no solution letter may sit under it.

## 7. Proposed Phase 2 (after review)
1. Tag the current commit `baseline-symmetric-mask`, then make asym_v1 + integral the defaults (coordinates untouched).
2. `build.sh`: add `back_plate_black`/`back_plate_brass` and the coupon; make the mask a legacy part; retire the three mask checks; add an automatic hole-position/diameter check.
3. Print the coupon first (brass, then two-colour); then one full plate on your existing base; then production plates.
4. Regenerate `stl/`, renders, README and print docs. Retire or update `make_sheets.py`.
5. Physical tests as listed in your Phase 3, including both play orders with the real journal proof.
