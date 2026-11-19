# Cog to Keeper: centre-cover gate needs a decision (19 Nov 2026)

CAD predictions and physical results are kept separate. No production geometry has been changed.

## What happened (owner's physical results, 19 Nov)
- Press-and-twist feel was validated earlier (PHYS).
- The centre cover falls out after one twist on the prototype (PHYS; the owner could not tell which hub version is fitted).
- Two sets of PETG bow strips (8, then a similar set) locked the cover down, but **fell out of the hub when the cover was removed** (PHYS, photos: loose black strips beside the hub and in the well).
- The knob test (0 and 4 tiles, hands only, 10 cycles each way) has **not** been run: the strips would not stay in place.
- The owner has printed many centre variants and cannot say which version is in the prototype. No physical result from it can currently be trusted. This is partly a process failure on my side: too many variants without version marks.

## Cause (CAD, confirmed from `cad/chronometer.scad`)
- Each bow foot sits in a slot 0.07 mm wider per side than the foot (`bow_fit`). My code comment called this a "light press fit"; it is a clearance. Nothing holds a foot down once the cover lifts and the arch relaxes.
- A stiffer strip (0.9 or 1.0 mm, files in `concepts/gate_contingency/`) does not fix this; it would fall out the same way and presses harder (beam-theory lower bound about 18 N and 24 N, unmeasured).
- Glue is not an acceptable fix: players will remove and refit the cover repeatedly.
- A snap-barb foot is not viable: about 18 % strain (3 t d / 2 L^2 with t 0.9, d 0.35, L 1.6) in PETG. CAD estimate only.

## Options
1. **Keep the gate; one-piece spring crown.** One PETG ring with six arches built in, seated in a groove in a new deck. Needs new deck and crown parts. CAD fit can be checked first; retention is **unproven until printed and tested**. Cost: deck reprint plus crown (not yet sized), and the gate's remaining unknowns (knob test, release force) still apply.
2. **Drop the gate; plain ring with flat ledge.** Owner-tested as working. Removes the strips and the knob-loosening failure. It changes the opening action for players, so it is a puzzle-design decision.
3. **Old three-arm latch.** Not a fallback: its release is not physically shown reliable, and it failed the knob-loosening test.

## Recommendation
Option 2 unless the gate's player-facing action is essential to a puzzle. The deadline is Sat 28 Nov (packing) and the owner has spent a lot of filament and time on the gate. If Keeper wants the gate kept, I recommend one numbered centre kit (version marked), tested on a single instrument before any decks are committed, with a hard stop date (suggest Sun 22 Nov): if option 1 fails on that date, go to option 2.

## Decisions needed from Keeper
1. Gate (option 1) or plain ring (option 2)?
2. If option 1, approve the new deck plus crown design for one test kit.
3. Confirm no optional-part work (keyed lid, M-72 proof) displaces this.

## Still outstanding from the owner (not blocking this decision)
Knob test results, journal leaf (from Scribe), stock inventory, four tile sets, screw-head measurements, Phillips size. Outer rings: 1 good bone ring plus the white prototype ring (a third bone ring from a failed run is scrap); 3 more needed for four matching instruments.
