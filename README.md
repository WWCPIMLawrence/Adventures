# The Chronometer

A 3D-printed mechanical puzzle instrument for *The Timekeeper's Paradox* (26 Nov 2026).
Two indexed dials, a removable centre cover over a stencil well, a hidden UV-flashlight
compartment and four dockable code fragments. Parametric OpenSCAD, support-free, M3 only.

![assembly](images/assembly.png)

| | |
|---|---|
| ![section](images/section.png) | ![exploded](images/exploded.png) |

**Status:** architecture reviewed, functional prototype geometry modelled, clearances
verified in CAD, paper sheets generated. **Nothing has been printed yet** — the next step is
the mechanical test print below. Decoration is deliberately minimal until that passes.

The reasoning behind the layout (and what was changed from the original brief) is in
[`docs/DESIGN_REVIEW.md`](docs/DESIGN_REVIEW.md).

## Repository

| Path | Contents |
|------|----------|
| `cad/chronometer.scad` | The whole model. Set `part` (or use the Customizer) to view/export any part. |
| `stl/` | One STL per part, already in print orientation, plus two convenience plates. |
| `sheets/aperture_test_sheet.pdf` | Clue sheet that reads **TIME** through the mask. |
| `sheets/labels_and_templates.pdf` | Inner-dial symbol labels, UV insert discs, fragment template, demo decoding card. |
| `sheets/aperture_proof.png` | Simulated view through the mask, registered and 1 mm off. |
| `images/` | Assembled, back, section and exploded views. |
| `build.sh` | Re-exports STLs, renders images, runs the interference checks. |
| `scripts/make_sheets.py` | Regenerates the PDFs from the CAD parameters. |
| `docs/Chronometer_design_handoff.pdf` | Self-contained design brief for an outside reviewer (`scripts/make_handoff.py`). |

```bash
./build.sh            # STLs + checks + images  (needs openscad; ~1 min)
```

```bash
python3 scripts/make_sheets.py   # needs reportlab, pillow, pdftoppm
```

## Parts and print settings

Bambu Studio, 0.4 mm nozzle, **0.20 mm layers, 3 walls, 15 % gyroid, no supports, no brim**,
PLA. STLs are already oriented; do not rotate them. Suggested colours are only that.

| Part (per instrument) | Qty | Orientation as exported | Notes |
|---|---|---|---|
| `base` | 1 | back face down | Longest print (several hours, not yet sliced). One short 29 mm bridge (door-slot ceiling). Bay sized for the purple squeeze light. |
| `deck` | 1 | underside down | Wall order outer/inner for accurate journals. |
| `outer_ring` | 1 | face up | Numerals are 0.5 mm deep; paint-fill or colour-swap at the last 3 layers. Seam: aligned. |
| `inner_ring` | 1 | face up | 12 label pockets, 0.4 mm deep. |
| `index_cap` | 1 | face up | |
| `pawl_outer`, `pawl_inner` | 2 + 2 | flat | Start with the medium (1.2 mm) ones. PETG recommended for the final sets. |
| `cover` | 1 | face down | Smooth plate gives the best face. |
| `keystone` | 1 | top down | |
| `uv_ring` | 1 | flat | |
| `mask` | 1 | flat, marker up | Matte black. |
| `door` | 1 | back face down | |
| `fragment_1…4` | 4 | text down | Or print `plate_fragments`. With the AMS, paint the first 2 layers of the characters in a contrast colour. |

`plate_small_parts.stl` = keystone, UV ring and two of each pawl in three stiffnesses
(1.0 / 1.2 / 1.4 mm, left to right). `test_base.stl` is an 11 mm base without the UV bay for
the mechanical test.

## Bill of materials (per instrument)

| Item | Qty | Use |
|---|---|---|
| M3 × 16 socket-head cap screw | 3 | index cap → deck → base (M3 × 20 also fits) |
| M3 × 8 socket-head cap screw | 1 | keystone |
| M3 hex nut | 1 | captive in the centre cover |
| Keychain UV squeeze light, ~43.5 × 23 × 8.5 mm | 1 | key ring and split ring removed |
| Self-adhesive felt, ~6 × 40 mm | 2 | on the two long **side walls** of the bay, against rattle |
| Sticker paper / plain paper | — | dial labels, UV disc |

Screws self-tap into 2.8 mm printed pilots. For four instruments: 12 × M3×16, 4 × M3×8,
4 nuts. For heat-set inserts set `screw_pilot_d` to the insert's hole size.

## Assembly

1. **Keystone:** press the M3 × 8 screw through the keystone from the top until the head is
   seated in its bore (a drop of CA is fine here — it is not a moving joint).
2. **Cover:** press the M3 nut into the hex pocket inside the cover. Lay a UV disc in,
   written side visible, and push the split ring in on top of it. Screw the keystone on.
3. **Base:** stick felt to the two long side walls of the flashlight bay — never to the door
   or the roof, which must stay clear of the light's squeeze switch. Lay the light in flat. Slide the door in from the
   rim, grooves outward, until it clicks.
4. **Deck:** place the deck on the base. Drop the four pawls into their pockets, noses
   pointing at the rings: `pawl_outer` (nose on the convex side) in the two pockets that open
   outward, `pawl_inner` (nose on the concave side) in the two that open inward.
5. **Rings:** lower the inner ring, then the outer ring, each with a scallop over each pawl
   nose. They should drop in under light pressure.
6. **Index cap:** arrow at XII (the side opposite the lone screw). Three M3 × 16 screws,
   snug only — over-tightening strips PLA and can pinch the rings.
7. **Mask:** drop it into the well, marker up, key tab toward VI; it follows a groove down
   and clicks onto the ledge. To remove, push it up from the back.
8. **Cover:** lower with its mark ~1 hour anticlockwise of XII, twist clockwise to the stop.

## Using the four functions

- **Temporal Alignment** — turn the outer ring by its edge and the inner ring by its ribs;
  read both against the double arrow on the brass index ring.
- **Temporal Aperture** — twist the cover anticlockwise and lift. Set the instrument on the
  sheet, rim notches on the printed ticks (double notch = top), centre target visible in the
  sighting hole. Read clockwise from the mask's arrow.
- **Hidden UV Discovery** — on the back, push the grooved end of the panel toward the rim;
  the door slides out and the flashlight tips out. The UV message is inside the centre cover.
- **Final Synchronization** — unscrew the keystone, seat the four fragments (pegs fit one
  socket each), screw the keystone back. Home the inner ring as the final clue instructs and
  read the fragment character beside each named symbol. Demo: sun at the index, then moon,
  star, hourglass, diamond → **1847**.

## Mechanical test print (do this first)

Print `test_base`, `deck`, both rings, `index_cap`, `plate_small_parts`, `cover`, `mask`,
assemble with the medium pawls, and print `sheets/aperture_test_sheet.pdf`
at 100 %.

| Check | Pass | If not, change |
|---|---|---|
| Rings turn freely with the pawls removed | no rub, < 0.5 mm wobble | `ring_clear` (0.30) ±0.05 |
| Click feel, 12 positions each | positive click, one finger turns it, does not move when the instrument is shaken | swap pawl stiffness; then `notch_depth`, `pawl_preload` |
| Rings with cap screws snug | still free | `ring_axial` (0.20) |
| Cover locks and releases | firm quarter-twist, stays put upside-down and shaken | `bay_play_end` (0 → −0.1 tighter, +0.1 looser) |
| Cover drops in | no forcing | `cover_clear` (0.20) |
| Mask seats, stays in when inverted, pushes out by finger | yes | `mask_clear`; nub size in `mask()` |
| Sheet reads T-I-M-E | each letter whole, nothing else visible | — (CAD margin is ±1.4 mm) |

## Parameters worth knowing

All in the top block of `cad/chronometer.scad`, grouped for the Customizer.

| Parameter | Default | Meaning |
|---|---|---|
| `uv_w`, `uv_t`, `uv_len` | 23, 8.5, 43.5 | Flashlight width, thickness, length (scaled from photos, ±1 mm). Base height follows `uv_t`. |
| `uv_clear`, `uv_z_clear`, `uv_end_gap` | 1.5, 1.5, 1.0 | Side, face and end clearance; face clearance keeps the squeeze switch untouched. |
| `bay_y`, `bay_x` | 41.5, 4.5 | Where the bay sits. A warning is echoed if it nears the rim, the well or a screw. |
| `body_r`, `well_r` | 62.5, 25 | Overall radius and well radius; the outer ring absorbs changes to `body_r`. |
| `apertures`, `aperture_d` | 4 × R15, 10.5 | Stencil holes `[x, y]`. Re-run `make_sheets.py` after changing. |
| `code_ring` | demo | The 12 fragment characters, clockwise from XII. |
| `peg_radii_a/b` | — | Fragment keying. |
| `pawl_t`, `notch_depth`, `pawl_preload` | 1.2, 0.6, 0.15 | Detent strength. |
| `ring_clear`, `ring_axial`, `cover_clear`, `mask_clear`, `door_clear`, `frag_clear` | — | Fits. |
| `bay_play_free`, `bay_play_end` | 0.35, 0 | Cover bayonet play at entry / when locked. |
| `cap_screw_style` | `"cap"` | `"csk"` for flush countersunk screws. |
| `cover_proud` | 3 | Grip height of the cover above the dials. |
| `show_numerals` | true | Roman numerals on the outer ring. |

Override from the command line without editing the file:

```bash
SCAD_ARGS="-D uv_w=23.6 -D uv_t=8.9" ./build.sh
```

## Needs physical validation

1. **Flashlight fit** — the bay is sized from photos (about 43.5 × 23 × 8.5 mm, ±1 mm).
   Confirm with calipers, especially thickness at the thickest point, and check the light
   does not switch on when the instrument is squeezed or set down hard.
2. **Detent feel and life** — force is estimated (~2–3 N at the rim), not measured. Check
   after ~200 clicks, and after a ring has been left between positions overnight (PLA creep).
3. **Cover bayonet grip** — relies on a ±0.1 mm ramp; it is the feature most likely to need
   one tuning reprint of the cover.
4. **Mask retention** — spring-arm preload (0.35 mm) and the click groove are untested.
5. **Door** — click strength of the side spring, and whether the bridged ceiling sags
   enough to rub (0.5 mm allowed).
6. **Deck-to-base seam near XII** — the 120° between the two upper screws spans the
   flashlight bay; check the rim stays closed there.
7. **Self-tapped M3 in PLA** — fine for a few assembly cycles; if the units will be opened
   often, switch to heat-set inserts.
8. **Legibility** — 5.5 mm fragment characters and 6 mm numerals as printed; aperture
   reading down a 22 mm well in poor light.
9. **Keystone screw** — the press fit of the screw head (`knob_head_d` 5.4) varies with
   screw brand.
10. **Printed-paper scale** — confirm the 100 mm bar on each sheet before judging alignment.

## After the test print

Feed back measurements and impressions; then: tune fits, and add the visual layer (minute track, engraved borders, AMS colour inlays, final
symbol set and code).
