> **UPDATE 20 Nov (Keeper): two strips supersede three for prototype testing.** Use the pockets at about **5 o'clock (148.6 deg)** and **9 o'clock (271.2 deg)**; leave the rest empty. The table below is kept for reference.

# T1-v1 three-strip standard: exact pocket positions (Keeper-approved for prototype testing, 20 Nov 2026)
Keeper: three 0.7 mm PETG strips per Chronometer, one per pocket pair, the same side of each pair; the other three pockets stay empty. Preserve the T1-v1 deck and cover geometry (no end stops). No PETG retaining ring. This is prototype testing, not four-unit production.

## How to find the pockets
View the deck from above with the **double notch at 12 o'clock** (the fixed-arrow side). Angles are **clockwise from 12 o'clock**. The six strip pockets are in three pairs, one pair in each gap between the cover's lug tracks.
| Pair | Pocket (bearing) | Use? | Approx. position |
|---|---|---|---|
| A | 353.5 deg | leave EMPTY | just left of 12 o'clock |
| A | **28.3 deg** | **FIT A STRIP** | about 1 o'clock |
| B | 113.8 deg | leave EMPTY | just before 4 o'clock |
| B | **148.6 deg** | **FIT A STRIP** | about 5 o'clock |
| C | 236.4 deg | leave EMPTY | just before 8 o'clock |
| C | **271.2 deg** | **FIT A STRIP** | about 9 o'clock |
**Rule: in each pair, fit the clockwise-most pocket** (the one further round clockwise, seen from above). The three strips are then 120.3, 122.6 and 117.1 degrees apart (three-point support).
CAD angles (counterclockwise from 3 o'clock, as in `bow_angles` in `cad/chronometer.scad`): used 61.7, 301.4, 178.8; empty 96.5, 336.2, 213.6. Diagram: `docs/images_strip_positions_T1-v1.png`.
These bearings come from the CAD. If the owner's previously built unit used different pockets, record which; all four instruments should follow this table from now on.

## Build reminders
Slide each strip in from the hub's outer edge, arch up and feet down, only just before fitting the inner ring; fit the inner ring promptly; do not disturb the strips afterwards. Check after handling for any strip that has drifted outward.
