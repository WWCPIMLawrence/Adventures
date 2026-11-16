# Stencil / back-plate retention: assessment (no CAD changed; awaiting approval)

Prepared from `cad/chronometer.scad` as it stands. Figures marked *est.* are beam-theory or reasoning, not measurements.

## 0. What the current CAD actually does (read from source)

Heights above the back face (the plane that rests on the RIFT sheet):

| Feature | Height | Belongs to |
|---|---|---|
| Ledge the mask sits on (annulus r 22 to 25) | 0 to 0.6 mm | back plate |
| Mask | 0.6 to 1.8 mm | loose part |
| Click groove for the mask's spring nubs (wall r 25) | 0.7 to 1.7 mm, 0.25 deep, V-shaped | back plate |
| Retaining lip over the mask rim (r 22 to 25.1) | 2.0 to 3.4 mm | **base** |

- **Actual mask-to-sheet spacing is 0.6 mm** (mask underside), not 0.8 mm. It was lowered by 0.2 mm earlier to give the mask 0.2 mm of play under the lip. The mask top is 1.8 mm above the sheet.
- The back has a 44 mm window (r 22), so the sheet is seen through the mask's four 10.5 mm holes and the 2.5 mm sighting hole. The back is therefore not a closed plate.
- The mask has three in-plane spring arms. The nubs press 0.65 mm into the wall and sit in the V groove, leaving about 0.4 mm of preload.
- The plate is keyed by a pin at 0 deg. The mask is keyed by a tab at 270 deg. The registration notches are cut in the base and plate.

## 1. Why the current lip lets the stencil get loose

1. **The mask is held by a sandwich, not by either part.** The ledge is in the plate and the lip is in the base. Remove the plate and the lip's partner is gone.
2. **With the plate off, the only thing holding the mask is friction.** The groove is in the *plate's* wall, so the nubs' V-groove hold is all that keeps the mask in the plate (est. well under 1 N, a shallow 27 deg flank). The base has no groove, so nothing holds the mask to the base either.
3. **Orientation decides where it goes.** Back face down, the mask stays on the plate. Back face up, gravity pulls it out of the plate onto the underside of the lip, where it is loose in the base. Turn the instrument over and it falls out through the open bottom.
4. **The 0.2 mm axial play** lets it rattle against the lip and the ledge between those two states.

## 2. Options compared

| Approach | Verdict | Why |
|---|---|---|
| **A. Capture the existing mask on the plate** with three snap lips | **Recommended** | See section 3. Mask rides with the plate. |
| **B. Print the aperture into the back plate** | Not recommended | The mask would be a 1.2 mm disc spanning a 44 mm window. Printed back-face down, its underside is a 44 mm bridge (sags). Setting the disc flush to the back face avoids the bridge, but then the sheet spacing is 0 mm, not 0.6 mm. The plate is brass PLA: thin bright PLA around the holes glares and may transmit light, against the approved matte black. A colour change inside one plate layer needs multi-material purging. Any stencil change means reprinting the plate. |
| **C. Hold the mask in the base only** | Not viable | The base has no wall below 2.0 mm. Holding the mask there lifts it to at least 2.0 mm above the sheet and breaks the optical spacing. |
| **D. Bond the mask into the plate with adhesive** | Fallback only | Zero redesign and certain to hold, but permanent, with a risk of glue near the apertures. Acceptable for the four hunt units if A fails. |

## 3. Recommended: three snap lips on the plate

- Three short lips (about 24 deg each) rise from the plate's collar and overhang the mask rim by about 0.5 mm, centred on the three spring arms. Each has a flat catch face 0.15 mm above the mask top and a 45 deg lead-in on its top face.
- **The mask snaps in from above:** the spring arms are in-plane and already flex 0.65 mm when the mask is pressed into the well, so they flex inward under the lead-in and spring back under the lip.
- **Pressed from below, it cannot pass** (flat catch face). **With the plate off, the mask stays in the plate** (the lips hold it in every orientation).
- **Removal for service:** push the three arms inward with a thin pick from above (the plate is already off the base). The mask has no other exit.
- **The base lip is deleted.** The plate lips take over its job. The base's bottom face gets three small notches (about 0.8 mm deep) so the lips can sit in it, which also locates the plate. Hence the base and plate both change; the mask itself does not.
- Estimated arm strain at the lips: about 0.75 % (3 t d / 2 L^2, t = 1.6 mm, d = 0.8 mm, L = 16 mm), acceptable in PLA or PETG.

**Exact CAD changes (on approval):**

| Part | Change | Parameters |
|---|---|---|
| `back_plate` | Add the three lips. | New: `mask_catch_n = 3`, `mask_catch_deg = 24`, `mask_catch_ov = 0.5`, `mask_catch_gap = 0.15`, `mask_catch_t = 0.8` |
| `base` (plate mode) | Delete the lip ring. Cut three notches in its bottom face to take the lips. | Replaces `mask_lip_t` |
| `mask` | **No change** (hole positions, diameters, tab and arms identical). | none |
| Checks | Replace `chk_mask_lip`. Add: lips clear the seated mask (EMPTY); a mask lifted 0.3 mm is caught (NON-EMPTY); notches clear the lips (EMPTY). | |

**Reuse and reprint:** the mask, cover, deck, rings, index cap, fragments and screws are unchanged. The base and back plate were going to be reprinted anyway for the old-base problem, so there is no extra reprint scope beyond one **short test piece** (plate region plus a base ring, about 20 min each, with the mask at about 5 min).

## 4. Compatibility

- **Aperture geometry:** identical. The four 10.5 mm holes at (0,15), (15,0), (0,-15), (-15,0) and the 2.5 mm sighting hole are in the unchanged mask part. The 0.6 mm spacing is unchanged.
- **Plate orientation:** the 0 deg pin and the registration notches (three singles and a double) are untouched, so the plate still fits one way. The mask's 270 deg key is unchanged.
- **UV bay:** its nearest edge is at r 29.5 mm; the lips are at r 22 to 25. The four M3x8 screws, bosses and counterbores are at r 54 and are unchanged.
- **Gate-only variant:** no interaction. The gate and the ring change only the deck, cover and ring. The cover's skirt ends about 10 mm above the mask.
- **Stencil through the open well:** unchanged. It stays in place at the bottom of the well and is read down the well.
- **Opening the bottom:** no extra information is revealed, and the mask is not removable, so there is nothing to damage. Players must refit the plate before the RIFT puzzle, because the mask goes with it. The clue should say so.

## 5. Acceptance tests (both orders)

All with the real RIFT sheet when it is available, otherwise `sheets/aperture_test_sheet.pdf` page 2.

1. **Music House first:** remove the cover, place the instrument on the sheet, align the notches, read the four letters without touching the mask. Refit the cover. Later remove the four hex screws, take off the plate (mask stays in the plate), take the light, refit the plate. Confirm the mask is still in place and the notches line up.
2. **Battle Creek first:** remove the four screws and the plate, take the light. Hold the plate and instrument right-side up, inverted and tilted: the mask must not fall or shift. Refit the plate. Later remove the cover and read the same sheet correctly.
3. **Handling:** shake the assembled instrument, press the mask hard from the back (it must not move), and open and close the plate 20 times without cross-threading or loosening of the screws in PLA.
4. **Neither order** may require touching the stencil or reveal the light early.

**Pass:** the mask stays in the plate in every orientation, with the plate on or off; it cannot be pushed up; the letters read within +/-1.5 mm of registration; the mask can still be removed with a pick.

## 6. Decision needed

Approve option A (snap lips on the plate, lip removed from the base). Until then, **do not print the current base and plate** if the redesign is likely: both change.
