# One-piece back plate and aperture: engineering review (no CAD changed; awaiting approval)

Prepared from `cad/chronometer.scad` as it stands. Figures marked *est.* are geometry or beam-theory estimates, not measurements. Section drawing: `images/aperture_section.png`.

## Recommendation

**Adopt the one-piece integrated aperture (floor printed with the plate, back face on the bed), pending a short coupon test.** It replaces my earlier Option A (snap lips). I rejected "option B" earlier because I assumed a disc suspended 0.6 mm above the back face across a 44 mm void. That does not apply to the bed-face geometry proposed here, and I withdraw the bridging objection. The remaining objections (spacing, colour) are real but small, and I quantify them below.

## 1. Cross-section (see `images/aperture_section.png`)

Heights above the sheet (z = 0 is the plate's back face, which rests on the sheet):

| | Now | Proposed |
|---|---|---|
| Aperture layer | mask 0.6 to 1.8 mm, **0.6 mm air gap** to the sheet | floor 0 to 1.2 mm, **flush** with the sheet |
| Held by | three spring nubs plus the plate-ledge and base-lip sandwich | it is part of the plate |
| Plate wall | r 25 mm, to 2.0 mm, with a click groove for the nubs | r 25 mm, to 2.0 mm, plain |
| Base lip | 2.0 to 3.4 mm over the mask rim | deleted |

The floor is a continuous disc, r 0 to 25 mm, bonded to the wall at r 25 mm. Its first layer is the back face on the bed. The four 10.5 mm holes at (0,15), (15,0), (0,-15), (-15,0) and the 2.5 mm sighting hole go through it.

## A. Printability

- **Unsupported bridge or overhang: none new.** Every layer of the floor sits on the layer below, starting from the bed. The proposal also **removes** two overhanging features: the 63 deg V click groove in the plate wall and the 270 deg key slot. The only overhang left in the plate is the existing screw counterbore ceiling, which already printed correctly.
- **Hole formation:** the holes print first-layer-down, as the existing mask's holes already do (the owner's preset has 0.15 mm elephant-foot compensation, and the mask holes look right in the photos). First-layer squish can shrink a hole by 0.1 to 0.15 mm per side at the sheet face. Optically that is a hole of about 10.3 mm, not 10.5 mm, which is negligible. **Check the diameter with calipers on the coupon.** Mitigation if it is under 10.3 mm: open the hole by 0.1 mm in the CAD.
- **Brim:** use an **outer brim only** (or none). Bambu Studio's "auto" brim can add an inner brim inside holes and close them.
- **Flatness:** the floor is continuous with the plate and now closes a window, so it is stiffer than today. The risk is warping of a 125 mm plate, which exists already and the current plate is flat.
- **Support from surrounding geometry:** the flashlight bay is at r 29.5 mm (its nearest edge) and the floor ends at r 25 mm, so the bay and its access do not change.

## B. Optical geometry

Looking through a hole at angle theta from vertical, the visible region on the sheet shrinks by (thickness) x tan(theta), and its centre shifts by (gap + thickness/2) x tan(theta):

| Case | 20 deg | 30 deg | 40 deg |
|---|---|---|---|
| Now: 1.2 thick, 0.6 gap | shrink 0.44, shift 0.44 | 0.69, 0.69 | 1.01, 1.01 |
| Integral 1.2, flush | 0.44, 0.22 | 0.69, 0.35 | 1.01, 0.50 |
| Integral 0.8, flush | 0.29, 0.15 | 0.46, 0.23 | 0.67, 0.34 |

- **Flush is better optically.** The centre shift (parallax) halves, which helps letter isolation. It does not change at straight-on viewing. Against a +/-1.5 mm registration budget, none of these figures is significant.
- **Registration:** the holes become rigid with the plate, so the mask's own 0.3 mm of slop in the well disappears. What remains is the plate's seating repeatability: the locating pin has about 0.3 to 0.7 mm of play in its hole (pin tip 3.2 to 4.0 mm in a 4.6 mm hole). I recommend tightening that hole to about 4.2 mm in the base (a base reprint, which is already due) and testing repeatability.
- **The RIFT sheet, unchanged:** the hole positions and diameters are identical, so by geometry the existing sheet works. This is a mathematical conclusion only. **It still needs a physical test with the final sheet**, which I do not have.
- **Black or brass?** Black is recommended. 1.2 mm of dense PLA is opaque (a phone-torch test on the coupon will confirm), but the brass PLA has glitter that reflects sunlight into the well, and black matches the approved colours. **Brass alone is likely acceptable for legibility** (letters are read inside the holes, against white paper), so decide from the coupon. Black costs one body per plate and about 12 colour changes (six layers, two changes each): est. 10 to 15 extra minutes and about 2 g of purge. Use two separate bodies, not the paint tool (it caused the halos on the tiles).

## C. Assembly and reliability

- **No mask to retain or handle.** Removing the plate removes the aperture with it, in any orientation, and nothing can drop. The base lip and the key slot are deleted.
- **Nothing on the other face snags:** the inner face is unchanged except that the floor top is 1.2 mm up.
- **Interchangeable mask:** for this hunt, not needed. The cost is that a bad plate needs a full reprint (about 1 hour) instead of a 5-minute mask. Keep the `mask` part in the repository as an optional style.
- **One-way fitting:** the pin at 0 deg and the notches are unchanged, so the plate still fits one way. Repeatability is the test below.

## D. Cost, scope and risk: against Option A

| | One-piece | Option A (snap lips) |
|---|---|---|
| Parts changed | back plate (floor, no ledge, groove or key slot); base (lip and key slot deleted, pin hole tightened) | back plate (lips); base (lip replaced by notches) |
| Parts removed | the separate mask | none |
| Reprints | plate and base | plate and base |
| Print time (P1S, est.) | plate about 1.2 h, with colour; base about 1.4 h | plate about 1 h; base about 1.4 h; mask exists |
| New mechanism to prove | none | snap lips and arm flexing |
| Optical change | flush: parallax halves; unvalidated sheet | none |
| Colour work | one extra body for black (or brass alone) | none |
| Main risk | hole size and glare, caught by the coupon | lip printing and arm fatigue |

I see no concrete reason Option A is better. Its mechanism is new and untested, and the integrated plate removes the problem it was solving.

## Test plan (smallest first)

1. **Coupon (about 10 min each):** a plate section with the floor (r 32 mm, 2.0 mm wall), no screws, printed in **brass** and in **black**. Check: hole diameters (10.5 +/- 0.15 mm) and positions with calipers; opacity with a torch behind; glare outdoors; sheet read through the holes at 0, 20 and 40 deg; the back face flat on a table. **Pass:** holes within 0.15 mm, opaque, letters clear.
2. **One full plate**, fitted to your **existing base** (the plate's interface outside r 25 mm is unchanged, so it should fit; this assumes your current base has no lip, which the old one does not). Remove and refit it 20 times, and put crosshairs on a test sheet to measure how far the holes move between refits. **Pass:** shift 0.5 mm or less.
3. **Both orders:**
   - **RIFT first:** read the four letters with the cover off, refit the cover, remove the plate for the light, refit, read again.
   - **UV first:** remove the plate and take the light, handle the loose plate (the aperture comes with it), refit, then read the RIFT sheet.
   **Pass:** identical reading before and after, nothing loose.
4. **The real RIFT sheet**, when it arrives, as the final check.

## If approved: files that change

| File / part | Change |
|---|---|
| `cad/chronometer.scad`, `back_plate()` | integral floor with the existing holes; drop the ledge, groove and key slot |
| `base()` | delete the lip (`mask_lip_t = 0`) and the key slot; optionally tighten the pin hole to 4.2 mm |
| New parameters | `plate_floor_t = 1.2`, `aperture_integral = true` (default false, so production is unchanged until approved) |
| New exports | `back_plate` as two bodies (`_brass`, `_black`) for Bambu Studio; a coupon part |
| Checks | `chk_plate_base` and `chk_mask_*` updated; hole-position and diameter check added |
| Unchanged | cover, deck, rings, index cap, fragments, mask (kept as an option), screws |

## Decision needed

Approve the one-piece plate as the preferred option, with the coupon and one full plate as the gate before any production print.
