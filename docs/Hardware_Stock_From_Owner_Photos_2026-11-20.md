# Owner's fastener stock, read from photos of the box labels (20 Nov 2026)
**Quantities are what the box labels say when sold. Actual counts remaining are UNKNOWN until the owner counts them. Nothing here is marked "available" for the checklist beyond what the labels show the boxes contain.** Head dimensions below are standard catalogue values, not measurements of these screws.

## Boxes shown
| Box | Contents (label) | Notes |
|---|---|---|
| Baocuz 380-piece, "M3 carbon steel cross-head screw nut set" | **Countersunk (flat) head, Phillips (cross), black, machine thread**: M3x20 (30), x16 (30), x12 (30), x10 (30), x8 (30), x6 (40), x4 (40); M3 nuts (150) | The "flat head" option |
| Kernmax 950-piece "12.9 grade M3 hex socket head screw kit" | **Socket head, 2.5 mm hex, black**: M3x6 (40), x8 (40), x10 (35), x12 (35), x16 (30), x20 (30), x25 (20), x30 (20); M3 nuts (250), washers (250), spring washers (200), 1 hex key | Back-plate screws (M3 x 8 socket) |
| 3DZWMAN 380-piece heat-set threaded inserts | **M3 x 4 x 4.2 inserts (100)** (4.2 mm outer diameter, 4 mm long), plus M2, M2.5, M4, M5, M6, M8 and insert tips | Not used in the current design |
| Black zinc-plated DIN 7981 pan head **self-tapping** screws, 500-piece | M3x6 (100), x8 (100), x10 (100), x12 (100), x16 (40), x18 (30), x20 (30) | The rounded-head screws on the prototype; **tapping thread, not machine thread** |

## What each screw is for, and what the photos show
- **Index cap (3 per instrument, M3 x 16 Phillips, Allen key must not fit):** the prototype uses the **pan-head self-tapping** M3 x 16 (40 on the label; need 12). The alternative is the **Baocuz countersunk M3 x 16** (30 on the label; need 12). The CAD already has a countersunk mode (`cap_screw_style="csk"`, 6.4 mm countersink, 1.7 mm deep); **the three existing caps were printed without countersinks, so choosing flat heads means reprinting the index caps.** Which look is preferred is Keeper's call; the owner will show both.
- **Back plate (4 per instrument, M3 x 8 socket head, 2.5 mm hex):** Kernmax M3 x 8 (40 on the label; need 16).
- **Knob screw (M3 x 10 now; M3 x 12 under trial):** the knob screw must be a **machine-thread M3 screw if it goes into the nut** in the cover. The **self-tapping pan-head screws have a coarser tapping thread and are NOT compatible with an M3 nut**; they only suit plastic. The Baocuz M3 x 10 and x 12 are machine thread and compatible with the nut, but their countersunk head (about 6 mm across) is **bigger than the 5.4 mm recess in the knob**: a recess change would be needed, which is not authorised. The Kernmax socket-head M3 x 10 and x 12 (head about 5.5 mm) fit the recess but are socket heads (the Allen key would remove them), which the owner does not want. **The owner has not said which screw is in the knob now** (see questions).
- **Nuts for the cover's hex pocket:** M3 nuts are available (Baocuz 150, Kernmax 250 on the labels).

## The owner's stripping worry (CORRECTED 20 Nov)
**Correction:** an earlier version of this note said the old centre piece had no nut. **That was wrong.** The owner's photo of the old centre piece's underside shows an **M3 nut seated in the hex pocket**, with the screw end visible in it. What the owner said is that the **newer-design covers used for the T1-v1 tests and the UV writing do not have a nut sunk in yet**, so those are samples.
- With a nut present, a **machine-thread M3 screw** runs in a steel nut and should not strip it. A **self-tapping (coarse-thread) screw** does not match an M3 nut's thread pitch and could damage it; the owner has not yet said which screw type is in the knob.
- In the photo the screw end looks level with or slightly inside the nut face. At M3 x 10 the tip should hang about 1.1 mm below the cover's flange underside; so either the knob is partly unscrewed in the photo or a shorter screw is fitted. Unconfirmed.
- Not yet physically tested for wear with a nut over many cycles; the owner reports many removals with no problem so far.

## Open questions for the owner
1. Which screw is in the knob now (which box, head type, length)? Does its head sit snugly in the knob's recess?
2. Counts remaining of: M3 x 16 (pan self-tapping or flat), M3 x 8 socket, M3 x 10 and x 12 machine screws, nuts.
3. Head diameter and height of the cap screw you prefer (calipers).
