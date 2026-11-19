# Cog to Keeper: Option 2 (O2-v1) result and a correction (19 Nov 2026, night)

## Owner's physical observations (PHYS)
- Ring stays in the cover securely and does not snag. The cover and seat assemble easily with no catching, and hold against pulling.
- **Only a small anticlockwise twist releases the cover** (owner: "a tiny bit of leftward untwisting"). Nothing resists turning.
- The owner says the ring has no function in the assembly. Two videos (one earlier, one short) show the cover and seat twisting and separating by hand **without the knob fitted**. The formal knob test A/B (0 and 4 fragments, 10 cycles each) has **not** been run, so no knob-loosening data exists for O2-v1.

## Correction (Cog)
I let Option 2 read as if it resisted rotation. It does not, by construction: with `latch_on=false` and `gate_on=false` the cover is held against lifting by the bayonet only, and the CAD itself notes the fit is "a running fit, NOT a friction lock". The only thing previously validated about the plain ring with ledge is that the ring stays in and does not snag (retention of the ring), not that the cover stays locked. The ring's original job (carrying sprung nubs that click into grooves) is disabled in this variant.

## Consequence (CAD reasoning, not yet a physical measurement)
A cover that turns freely with a small anticlockwise twist, with the knob as the only reaction member, is expected to **fail test A**: loosening the knob (anticlockwise) is the same direction as the release. Keeper's pass criterion cannot be met by O2-v1 as specified. I recommend counting this as a failed Option 2 for the purposes of your stated rule, subject to your ruling, because the exact failure is now known and documented.

## Options for your decision (no CAD changed)
1. **One version-marked spring-crown test kit** (your stated fallback): one-piece PETG ring with six built-in arches and a new deck groove, hard stop date Sun 22 Nov, tested once; if it fails, a different retention concept. Unproven until printed.
2. **A positive rotation detent by shape** (new design, needs approval): for example a latch ring with printed arms that click into grooves, the old nub idea made strong enough and not carried by the cover alone. The old three-arm latch failed the knob test and the ring snagged on insertion, so this would need a clear redesign, not a revert.
3. **Change what the knob reacts against**, for example fixing the cover from turning while the knob loosens (knob tightens on the cover's own flange, hold-down tabs). Not designed; I do not recommend it as a quick fix.
4. **Accept a free-turning cover and cover the risk in the game design** (clue wording, instruction card). Not an engineering fix; your call.

## Schedule note
The owner has lost much of two evenings to failed prints (bed adhesion, a run with a failed ring). Remaining weekday capacity is small; production deadline for preparation (Wed 25 vs later) is still unconfirmed. Please state which option and the stop date.
