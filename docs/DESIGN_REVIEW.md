# Architecture review — what changed from the brief, and why

This is the step-1/step-2 review: the conflicts found in the proposed layout and the
architecture that replaced it. Everything below is implemented in `cad/chronometer.scad`.

## Problems in the proposed layout

| # | Conflict | Consequence |
|---|----------|-------------|
| 1 | **Rear UV compartment vs. see-through centre.** The aperture needs a clear line of sight through the middle of the instrument, so the flashlight cannot live behind the centre. | Compartment must move off-axis. |
| 2 | **Rear "extension" vs. lying flat on the clue sheet.** Any local bump on the back tilts the instrument, and the stencil then floats and reads with parallax. | The back must be one flat face. |
| 3 | **Stencil directly under the cover is too far from the paper.** With a 20 mm body the mask would sit ~18 mm above the letters: any tilt of the head shifts what is seen. | Mask must sit at the bottom of the well, ~1 mm above the paper. |
| 4 | **Radial budget.** 62.5 mm radius minus a 25 mm well leaves 37.5 mm for two rings, their retention, the fixed index, *and* four fragment seats. Fragment seats in the main body would squeeze the dials to ~7 mm bands. | Fragments must not consume radial space in the ring assembly. |
| 5 | **Ring retention vs. removable centre.** If the centre cover is what holds the inner ring down, removing it releases the ring. | Rings need their own retainer, independent of the cover. |
| 6 | **15–20 mm thickness with a flashlight inside.** Ring mechanism (~8 mm) + a round Ø14 light would not fit in 20 mm. | Resolved by the actual light being flat (8.5 mm): rim height is 19.6 mm. |
| 7 | **Printed snap arms.** Vertical snap fingers on a cover skirt flex across layer lines — the orientation where PLA breaks. | No part in this design flexes across layers. |

## The architecture that resolves them

```
                keystone knob (M3 thumbscrew)
        ┌──────── fragments ×4 on the cover face ───────┐
        │   CENTRE COVER  (bayonet, UV insert inside)   │
 outer ring │ index cap (fixed, 3× M3) │ inner ring     │
 ───────────┴── DECK: hub + fixed rib, 4 detent pawls ──┴────
            BASE: flat back, mask at bottom of well,
                  UV bay on a chord + sliding door
```

**Two-module body.** A thin **deck** (ring mechanism + cover seat) is screwed to a **base**
(mask seat, sheet registration, UV bay). The same three M3 screws clamp the index cap, the
deck and the base. Benefits: the deck + rings *is* the step-4 mechanical test print (use it
with the 11 mm `test_base`), and the base can be re-fitted if the flashlight changes without
touching a mechanism that already works.

**Rings.** Both rings have an L-section and are trapped by one fixed **index cap** screwed
to a rib that stands between them. The cap carries the reference index (a double arrow at
XII pointing at both dials). The outer ring is the rim of the instrument, so it is turned by
its knurled edge like a dive-watch bezel; the inner ring is turned by raised finger ribs.
Removing the centre cover touches none of this.

**Detents.** Each ring is indexed by two arc-shaped leaf springs ("pawls") that sit in
pockets of the fixed rib and push a rounded nose into twelve scallops on the ring. They are
separate parts on purpose: they print flat (bending along the filament, the strong
direction), are trapped by the index cap, cost seconds to reprint, and come in three
stiffnesses so the click can be tuned without reprinting anything large. Estimated peak
strain is ~0.7 % for the medium pawl — inside PLA's elastic range; PETG is the better final
material.

**Centre cover.** Three-lug bayonet with unequal lug spacing (one orientation only), 28°
clockwise to a hard stop. The 45° lug and ceiling faces make it support-free and it is a
loose running fit (0.30 mm axial play when locked). Retention is a separate sprung latch:
the free end of the UV retaining ring carries a nub that passes through a slot in the skirt
and clicks into a groove in the well wall, with a second groove at the insert position. The
cover stands 3 mm proud with a knurled edge so it can be gripped.

**Aperture mask — interchangeable: yes.** The mask is a 1.2 mm disc at the bottom of the
well, sitting 0.8 mm above the paper. A key tab fixes its rotation; three in-plane spring
arms grip the well wall and click into a shallow groove. It is swapped by pushing it out
from the back with a fingertip. Reasons to make it separate: aperture positions will change
as the clue sheets are written, a mask is a 10-minute print versus a multi-hour base, it can
be printed in matte black while the body is brass-coloured, and extra masks can themselves
become collectable components.

**UV compartment.** The flashlight lies flat on a chord of the base, 41.5 mm off-centre, clear of
the well. It is closed by a flush **dovetail door in the back face** that slides out through
the rim; a side spring on the door clicks into a notch. The back stays perfectly flat, there
is no tool, and nothing presses on the switch (clearance above and below the light). All bay
dimensions derive from `uv_w` / `uv_t` / `uv_len`, and the base height follows automatically.

**UV-reactive insert.** A Ø46 mm paper disc inside the centre cover, held by a printed split
ring. It is hidden until the cover is off and turned over, protected from wear, and
replaced in seconds.

**Fragments — neither "in the main assembly" nor "an accessory ring".** The four fragments
dock onto the **face of the centre cover**, which is already detachable. That costs zero
radial space in the ring mechanism, needs no extra carrier part, and the cover still comes
off for the aperture with the fragments in place. Each fragment has two pegs at radii unique
to its socket, so it fits one position, one way up. A central **keystone** knob (M3
thumbscrew into a captive nut) clamps all four: its cone seats on their 45° bevels while its
underside is still 0.3 mm off the cover, so the screw load goes into the tiles — positive
retention instead of a friction fit, and it stays on the instrument from the start as a centre finial.

**How the code is produced.** Together the fragments form a ring of twelve characters lying
directly inside the inner dial. The final clue names a home position for the inner ring and
four symbols in order; each symbol points at one character. Any four-character code is
possible, a single fragment reveals nothing, and a ring that is one click off gives a wrong
code (demo: `1847` correct, `5020` one click off). An accessory ring would add a part and a
second interface without adding function, so it was rejected.

## What this costs

- **Thickness.** 19.6 mm at the rim and 29.6 mm over the keystone with the actual light (a
  flat squeeze-type key-fob light, about 43.5 × 23 × 8.5 mm, lying on its face). The ring
  module alone is 7.6 mm; the rest is the flashlight.
- **Flashlight envelope.** The 23 mm width uses nearly all the radial room between the well
  and the rim (2.3–3 mm walls). A wider light needs a larger `body_r` — the script prints a
  warning when the bay gets within 2 mm of the rim or the well.
- **Squeeze switch.** The switch is on the light's face, so the bay leaves 1.5 mm of face
  clearance and the anti-rattle felt goes on the side walls only.
- **Three visible screws** on the face. They read as instrument hardware; countersunk heads
  are a one-word switch (`cap_screw_style = "csk"`).

## Verified in CAD

`./build.sh check` intersects every pair of neighbouring parts in their assembled positions
(rings/deck, rings/cap, rings/cover, cover/deck, cover/base, cover in its lift-out position,
pawls/deck, pawls/cap, door/base, mask/base, fragments/cover, fragments/keystone,
fragment/fragment) and requires zero overlapping volume. Two checks must *fail* to be
correct: a fragment placed in the wrong socket must collide, and the pawl noses must overlap
the ring scallops by the preload. All 15 pass.

`scripts/make_sheets.py` checks the clue sheet geometrically: through the registered mask
each aperture shows exactly its letter of T-I-M-E, and it stays clean (whole letter visible,
no neighbour intruding) for placement errors up to 1.4 mm in any direction.

None of this replaces a print — see "Needs physical validation" in the README.

## Changes after the first outside review

1. **Fragment clamp.** The keystone cone had a 0.25 mm offset and bottomed on the cover
   first; it now matches the bevel and leaves a 0.3 mm gap under the knob
   (`images/clamp_section.png`). The nut pocket has an undersized mouth so the nut stays in.
2. **Bayonet.** Zero-clearance friction ramp replaced by a running fit plus the sprung latch
   above. The CAD check now covers the whole swept turning path.
3. **UV compartment.** `test_uv_bay` isolates the bay and door for a quick print;
   `uv_enabled = false` removes both if they prove troublesome.
4. **Ring play.** Axial play under the cap raised from 0.20 to 0.35 mm.
5. **Springs as consumables.** The mask check now uses the real mask (spring nubs must press
   on the wall, nothing else may touch); `mask_style = "dropin"` is the fallback.
6. **Player view.** Fragment characters enlarged to 6.5 mm; the home symbol has a double
   border and the decoding card separates SET (sun) from READ (four numbered symbols).

All 22 CAD checks pass. None of this has been printed.
