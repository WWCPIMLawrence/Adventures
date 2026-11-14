# Print plan: first test prints, then production

All times and weights below are from PrusaSlicer with a generic machine profile (0.20 mm,
3 walls, 15 % gyroid). They are **not** Bambu Studio estimates: a P1S normally finishes
sooner, and Bambu Studio's own figure for each plate is the one to plan around.

## 1. First test prints

Nothing here needs the final filament colours. Use any ordinary PLA you already own —
**not silk, not wood-filled, not glow** — and any PETG for the spring plate. Fit and click
are material-dependent, so the deck, cover, one ring and the springs get repeated once in
the final filaments before production (section 3, step 0).

Print in this order. Prints 1 and 2 are short and test the riskiest features, so start
there.

| # | STL files (import together, auto-arrange) | Filament | Weight | Time | What it tests |
|---|---|---|---|---|---|
| 1 | `test_seat`, `cover`, `mask` | PLA | 22 g | ~2 h 20 | Cover bayonet through its full 28° turn, latch grooves, mask retention |
| 2 | `plate_springs` | **PETG** | 3 g | ~25 min | Detent springs in three stiffnesses + two latch rings |
| 3 | `deck`, `index_cap`, `test_screw_ring` | PLA | 60 g | ~6 h 30 | Ring journals, pawl pockets, cap retention |
| 4 | `outer_ring`, `inner_ring` | PLA | 30 g | ~3 h 10 | Ring fit, detent scallops |
| 5 | `plate_small_parts`, `plate_fragments` | PLA | 9 g | ~1 h 10 | PLA springs for comparison, keystone clamp, fragment keying |
| 6 | `test_uv_bay`, `door` | PLA | 17 g | ~1 h 30 | Flashlight fit and door (bay now sized to caliper measurements) |

Round total, without the UV piece: about 125 g of PLA, 3 g of PETG, roughly 13½ hours.

Notes on the files:

- `plate_springs` and `plate_small_parts` each hold two outer and two inner pawls in three
  thicknesses. Small bars printed beside each column identify them: **I = 1.0 mm,
  II = 1.2 mm, III = 1.4 mm**. Bag them by thickness when they come off the plate.
- `test_screw_ring` is a light ring that sits under the deck so the three cap screws have
  something to thread into. It replaces `test_base`, which is no longer needed.
- `test_seat` is the centre of the deck and base in one piece. The real `cover` is used
  with it, and the latch ring from print 2 snaps inside the cover.

### Bambu Studio settings (P1S, 0.4 mm nozzle)

Start from **0.20mm Standard @BBL X1C** (the P1S uses the same process presets) and change
only what is listed.

| Setting | PLA plates | PETG spring plate |
|---|---|---|
| Layer height | 0.20 mm | 0.20 mm |
| Wall loops | 3 | 4 (makes the 1.0–1.4 mm springs solid wall, no infill) |
| Top / bottom shell layers | 5 / 4 | default |
| Sparse infill | 15 % gyroid | irrelevant |
| Order of walls | **outer/inner** for everything. Every fit that has passed (cover, rings, detents) was printed with this setting, so production must use it too | default |
| Supports | Off | Off |
| Brim | None | None |
| Seam | Aligned | Aligned |
| Elephant-foot compensation | leave at the preset value | leave |
| Build plate | Textured PEI | Textured PEI, clean and dry |
| Filament profile | the profile for the spool you load | the profile for the spool you load |
| Enclosure | door ajar or top glass off for PLA | closed |
| Speed | preset | preset; if the springs look stringy or rough, drop outer-wall speed |

Other points:

- Do not rotate or flip the STLs; they are exported in print orientation.
- Do not scale anything. If a fit is wrong, tell me the symptom and I change the parameter.
- PETG that has been sitting open should be dried first; wet PETG makes weak springs.
- "Order of walls" is under Quality → Advanced.

### What to check and report

The full pass/fail table is in the README ("Round 1 checks"). The short version, in the
order the prints finish:

1. **Cover in `test_seat`** — drops in, turns to the stop without binding, lifts out. With
   a latch ring fitted: clicks at both ends, stays in when inverted and shaken.
2. **Nut** — drawn into the cover with a long M3 screw; stays put with the latch ring out.
3. **Mask** — slides down the well, clicks, survives inversion, pushes out from the back.
4. **Rings without pawls, cap screws fully tight** — spin freely, no rocking or rubbing.
5. **Detents** — try PETG II, then PETG III, then PLA II. Each of the 12 positions should
   settle by itself; one finger turns the ring; nothing moves when shaken.
6. **Fragments** — each fits only its own socket; immovable with the keystone tight.

For anything that fails, the most useful report is: which part, what it does (binds /
loose / will not click / broke), and roughly how far off it looks.

## 2. Hardware — verified

The model now checks its own screw lengths every time it is built and warns if a screw
would bottom out or fall short. Current output:

- Cap screws: **M3 × 16**, 7.4 mm clearance stack, 8.6 mm of thread in a 10.7 mm pilot.
- Keystone screw: **M3 × 8**, reaches 3.9 mm below the cover face; the nut spans 1.4–3.8 mm.

| Item | Per unit | Four units |
|---|---|---|
| M3 × 16 socket-head cap screw | 3 | 12 |
| M3 × 8 socket-head cap screw | 1 | 4 |
| M3 plain hex nut, 5.5 mm across flats, 2.4 mm thick | 1 | 4 |

The one outdated comment in the source ("suits M3x16 (or M3x20)") is corrected. For the
first test prints you need 3 × M3 × 16, 1 × M3 × 8, 1 nut, and any longer M3 screw to draw
the nut in.

## 3. UV flashlight — measured, ready for its fit test

Caliper measurements with the key ring removed: **40.3 mm long** (LED included),
**22.6 mm wide**, **8.7 mm thick**. The photo estimate had been 43.5 × 23 × 8.5 mm, so the
light is 3 mm shorter and marginally thicker than assumed.

The bay is now 42.3 × 24.1 × 10.2 mm (1 mm free at each end, 1.5 mm total at the sides and
on the faces). The shorter light let the bay move 1 mm back from the rim, so the thinnest
walls grew from about 2.3–2.9 mm to 3.2–3.6 mm. The base is 12.2 mm tall (was 12.0) and the
instrument 19.8 mm at the rim.

**Print now:** `test_uv_bay` and `door` (PLA, about 17 g, ~1½ h). Check that the light drops
in flat, does not rattle badly with felt on the two long side walls, does not switch on
when the piece is pressed or knocked, and that the door slides, clicks and does not rub the
bridged ceiling. The full `base` waits until this passes.

The 8.7 mm thickness is at the slide-lock tab, the tallest point of the light; pressing the
tab straight down does not switch the light on, and the squeeze face sits lower, so it has
more than the nominal 1.5 mm of clearance. Load the light with the tab facing away from the
door, and with the LED pointing into the closed end of the bay (away from the rim). The lock
slides away from the LED to turn on, so in that orientation closing the door can only push
it toward off; opening could at worst turn the light on as the player takes it out. Test
both door directions.

Still unmeasured, and not blocking: how far the LED protrudes, and whether a squeeze
anywhere on the face switches the light on or only at one spot.

## 4. Production plan (after the tests pass)

**Step 0 — material check.** Before the batch, print `deck`, `cover`, `outer_ring`,
`inner_ring` and `plate_springs` once in the final filaments and repeat the round-1 checks.
If they pass, these parts become instrument no. 1.

**Step 1 — complete instrument no. 1** (add `base`, `index_cap`, `door`, `mask`,
`keystone`, fragments, labels) and test it as a player would. Freeze the design.

**Step 2 — batch the other three plus spares.** One filament per plate. Two 125 mm parts
fit a plate comfortably; four would crowd the bed edge.

| Order | Plate | Filament | Time | Why this order |
|---|---|---|---|---|
| 1 | `deck` × 2 | Brass PLA | ~7 h | Mechanism first: each deck can be assembled and tested as soon as its rings exist |
| 2 | `outer_ring` × 2 | Charcoal matte | ~4 h | |
| 3 | `inner_ring` × 3 (+ 1 spare) | Ivory matte | ~4 h 40 | |
| 4 | Pawls: 3 sets per instrument, and 8 latch rings | PETG | ~2 h | Spares are cheap; print them all at once |
| 5 | `deck` × 1, `index_cap` × 3 | Brass PLA | ~6 h | |
| 6 | `outer_ring` × 1, `keystone` × 4, `mask` × 7 | Charcoal matte | ~5 h | Includes 4 spare masks, 1 spare keystone |
| 7 | `base` × 2 | Brass PLA | ~9 h | Overnight |
| 8 | `base` × 1, `cover` × 4, `door` × 5 | Brass PLA | ~11 h 30 | Overnight. Includes 1 spare cover, 2 spare doors |
| 9 | `plate_fragments` × 4 | Ivory matte | ~2 h 30 | Includes 1 spare set |

About 52 hours of printing for three instruments and all spares, by the generic estimate;
about 67 hours if instrument no. 1 also has to be reprinted. Plates 1–6 are daytime prints,
7 and 8 run overnight.

**Spares produced:** 2 extra pawl sets per instrument, 4 latch rings, 4 masks, 2 doors,
1 cover, 1 keystone, 1 inner ring, 1 fragment set.

**Step 3 — assembly and finishing,** one instrument at a time: mechanism (deck, pawls,
rings, cap) and test; then base and door; then cover, nut, UV disc, latch ring; then
labels. Roughly 20–30 minutes each once the first one has been done.

### Calendar check

| Days before the event | Work |
|---|---|
| 14–12 | Round-1 test prints, measurements, fit feedback, parameter changes |
| 11–9 | UV bay test; step 0 material check; instrument no. 1 complete |
| 8 | Freeze |
| 7–3 | Batch plates 1–9 (about two plates a day) |
| 2–1 | Assembly, labels, UV discs, spare kit, full play-test |

The slack in this schedule is about two days. The UV compartment is the piece to drop if a
test round has to be repeated: `uv_enabled = false` removes it and saves about 4 hours of
base printing per plate.
