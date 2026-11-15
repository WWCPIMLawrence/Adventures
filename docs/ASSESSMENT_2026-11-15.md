# Chronometer assessment of the 15 Nov consolidated handoff

Prepared from the current `cad/chronometer.scad` and the owner's reports. Nothing below has been
applied to a production file except where stated. Estimates are beam-theory figures, not
measurements; **no computer check in this document is a physical pass.**

## 1. What is confirmed, unconfirmed and diagnosed

**Confirmed from the active CAD (read from source or computed)**

| Item | Finding |
|---|---|
| Centre screw, M3 × 10 | Tip ends **1.1 mm below the cover's flange underside** with fragments fitted (1.4 mm with none). 2.9 mm of thread beyond the nut (nut is 2.4 mm). The nut bore is open underneath, so there is nothing to bottom against. It passes through the 4 mm centre hole in the UV disc. Zero to four fragments changes the tip by only 0.3 mm. M3 × 12 would also clear. |
| Screw parameters | The model had tied the back-plate screw check to the knob screw. They are now separate: knob M3 × 10, back plate M3 × 8. No part geometry changed (every re-exported file has identical volume and size). |
| Latch, before | One nub on a ring with its own split beside it. The nub sat on a short free stub, so the spring was weak and lopsided. This is why thickness and groove depth never fixed it. |
| Latch, now | Three equal in-plane arms on the PETG ring, three slots in the cover, six steep-sided grooves in the deck. Built and interference-checked; **not yet printed**. |
| UV ring retention | The ring is held in the cover by **0.1 mm radial interference only**. The slots are open at the skirt's end and there is no axial feature, so anything dragging on a nub can pull the ring out. |
| Mask | New base has a 1.4 mm lip over the mask rim. With the plate on, the mask sits between the plate ledge (0.6 mm) and the lip (2.0 mm) with 0.2 mm of play. It cannot be pushed up. Hole shapes, sighting hole, key and notches are unchanged. |
| Registration notches | Cut in the base and back plate only, at 0°, 180°, 270° and a double at 87°/93°. The deck and rings have none. |
| Knob head pocket | Ø5.4 × 4.0 deep, and the knob prints top-face-down, so the pocket sits in the **first four layers on the bed**. |

**Diagnosed from symptoms (reasoned, not tested)**

- **Knob versus cover.** Loosening a right-hand knob screw is anticlockwise viewed from the top. The
  cover unlocks anticlockwise too. Thread friction on the captive nut, and the cone's friction on
  the fragments (which are pegged into the cover), both push the cover the **unlocking** way. So
  the two failures are linked through one thing: **the latch release torque must exceed the torque
  needed to loosen the knob.** The weak single-nub latch is the likely cause.
- **Head protruding.** The Ø5.4 mm press-fit pocket opens onto the bed, where holes print small
  (the preset's 0.15 mm elephant-foot compensation also acts there). A 5.5 mm head would not seat.
  This needs a caliper measurement of the printed pocket before anyone changes it.
- **UV ring loosening during removal.** Consistent with friction-only retention. Whether it is also
  linked to the latch (a nub catching a groove edge as the cover lifts) is **not established**.

**Unconfirmed, needs a physical test**

Latch release force; ring survival over 20+ cycles; whether the mask stays in the plate or in the
base when the plate is removed; the Phillips screw's head size; the real RIFT sheet; back-plate
screws after repeated removal in PLA; how the groove extension looks.

## 2. Ranked issues

**Must fix before printing the remaining units**

1. **Cover latch strength** (also cures the knob problem if release torque beats knob torque). Fix is
   built; needs the soft/firm print test.
2. **UV ring axial retention.** Proposed, not built (section 3).
3. **Mask retention.** Fix is built (lip); needs the brass base and plate.
4. **Knob screw head seating and anti-spin.** Held for measurements.
5. **The final RIFT sheet.** Not available on this side.

**Optional**

6. Registration notches continued through the deck. 7. Back-screw cycle testing.

## 3. Recommended changes: current → proposed, and compatibility

| Change | Current | Proposed | Compatibility with prints already made |
|---|---|---|---|
| Latch | 1 nub, 2.1 mm ring | **3 arms**, 1.4 mm (variants 1.2 / 1.6), 3 slots, 6 grooves | **New cover, deck and ring needed.** The old cover has one slot: a new ring's other two nubs would jam against the skirt. An old ring in a new cover works but is weak. |
| Mask lip | Ledge 0.8, no lip | Ledge **0.6**, lip over the rim | New base and plate needed (both are being printed in brass anyway). Mask part unchanged. |
| Knob screw | M3 × 8 socket head | **M3 × 10** (already working) | No part change. |
| Knob head pocket | Ø5.4 × 4.0 | **Hold.** Needs measurements | See questions. |
| UV ring retention | Friction, 0.1 mm | **Proposed:** three 0.5 mm bumps on the skirt interior just below the ring, 45° underside so they print without support, ramped on the lead-in side so the ring snaps past | Cover change only. Not built, awaiting approval. |
| Deck grooves | None on deck | Same V notch as the base (1.27 mm deep, 2.55 mm wide) at the same angles | Deck only. **Safe by geometry:** the deck rim there is a 2.0 mm flange, 13 mm of it remains inside the notch, and the nearest functional feature is the outer-ring journal at r 48.3. No pawl, screw or latch feature is nearby. The outer ring is not touched. Not built, awaiting approval. |

## 4. Minimal test plan and go / no-go

Reprints: **cover, deck, one ring pair**, and the brass base and plate. The latch test needs only the
seat piece, a cover and the two ring variants (about 45 minutes).

| Test | Go |
|---|---|
| Knob versus cover | With four fragments fitted and the cover locked, loosen the knob **by hand with nothing else held**: the cover does not turn, 10 of 10 tries. Repeat at 0 fragments. If it moves, use the firm ring. If the firm ring fails too, tell me before any other change. |
| Latch feel | Clear click at both ends. Release takes a deliberate twist but is comfortable. Stays shut upside down and shaken. |
| UV ring | Stays in the cover through 20 cover removals and 20 disc changes. |
| Mask | Does not move under a firm finger push from the back. Plate removal leaves the mask in one known place. The four holes read RIFT on the real sheet. |
| Back screws | 20 remove-and-refit cycles with no loosening. The plate sits flush. |
| RIFT | Registered within ±1.5 mm, only the four intended letters visible. The sheet geometry (below) must be matched. |

**Sheet requirement for the game work:** registration marks at 0°, 180°, 270° and a double at 87°/93°
on a Ø125 mm footprint; four apertures at (0, 15), (15, 0), (0, −15), (−15, 0) mm, Ø10.5; capital
letters 5 mm high on a diagonal lattice with 10.6 mm between neighbours; tolerance ±1.7 mm in the
geometric check; print at 100 %. The RIFT page in `sheets/aperture_test_sheet.pdf` (page 2) is a
working example. **The final Music House sheet is not on this side.**

## 5. Questions for the owner

1. The caliper diameter of the printed knob pocket, and the **Phillips screw head: diameter, height,
   style (pan, cheese or button)**.
2. Approve the UV-ring retention bumps? (needs a cover reprint)
3. Approve continuing the registration notches through the deck?
4. Send the final Music House RIFT sheet file for a registration check.

## Player handling for the knob and cover (no UV spoilers)

- To add a tile: turn only the small brass knob anticlockwise a few turns, lift off the tiles, fit
  the new tile (each fits one place only), and turn the knob clockwise until **hand-tight**.
  Do not twist the large brass disc under it.
- To use the optical sheet: twist the large brass disc anticlockwise about a quarter turn and lift.
  Refit by dropping it in and twisting clockwise until it clicks.

## Update, 16 Nov: the two approved changes

- **Ring retention bumps** (cover only): three bumps on the skirt's inner wall just below the latch ring,
  0.5 mm high, 16° wide, 30° after each latch nub. 45° retaining ramp (prints without support), 26° lead-in.
  They sit below the ring's height, so the spring arms keep their full movement. A beam model puts the
  force to push the ring past them at about 0.3 N per bump (roughly 1 N of pull-out retention in total).
  That is light but many times the friction hold it has now, and ample against a 1 g ring. If the test
  shows it is not enough, the next step is a flat ledge, which needs a pinch to release.
- **Deck notches**: the same V notch as the base, at 0°, 180°, 270° and the double at 87°/93°, through the
  2.0 mm deck flange. The black outer ring is untouched. All 27 interference checks pass.
- **Only two part files changed**: cover (+9 mm³) and deck (−15 mm³).
- **Mask**: the lip blocks the mask from being pushed up. With the back plate off it is no longer locked:
  it comes away with the plate (held by its spring nubs) and can be pressed out of it.
