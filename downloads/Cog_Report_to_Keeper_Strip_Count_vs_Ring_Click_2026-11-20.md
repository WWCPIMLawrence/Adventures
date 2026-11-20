# Cog to Keeper: gate-strip count against inner-ring feel (owner measurements, 20 Nov 2026)
Owner-reported (PHYS), informal, by hand. No CAD or production geometry changed.

## Measured on the T1-v1 full-assembly unit (strips in their pockets, inner ring and pawls fitted)
| Strips fitted | Inner ring spin and click | Cover |
|---|---|---|
| 0 | clicks and spins "like it always has" | (no gate lift) |
| 1 | clicks and spins "pretty good" | not enough force to hold the cover (earlier test) |
| 2 | "acceptable" click and spin, "obviously not as smooth as 0 or 1" | locks and releases correctly; **the centre piece wobbles slightly when the edges are tapped**; owner thinks it will not be noticeable once locked |
| 3 | **spin greatly reduced; click almost imperceptible** | stable and balanced; locks and releases correctly |
Earlier in the session: with six strips the inner ring was very stiff and strips were damaged during assembly. Strips "want to pop out, especially at the bottom"; once in they are held by the inner ring.

## Cog interpretation (reasoning, not measured)
- Each strip adds drag on the inner ring: the more strips, the less the pawl detent can be felt. The likely mechanism is a strip end touching the ring and/or pushing the ring slightly off-centre so the pawl nose engages less deeply. In CAD a seated strip's corners clear the ring by about 0.46 mm; a strip that sits outward, a hub that prints slightly oversize or a ring bore that prints slightly small would remove that clearance. Not yet isolated physically: the owner has been asked to repeat the tests with the cover off, to push each strip fully inward, and to describe the ring's sideways play.
- The cover needs three-point support to be stable (two strips allow a slight rock); the ring wants as little strip contact as possible. These two needs conflict in the current geometry.

## Options for your decision (none authorised; no CAD change made)
1. **Accept two strips** (owner: click acceptable, slight wobble). This deviates from your approved three-per-instrument standard and is a prototype-testing decision.
2. **Keep three and remove the cause:** confirm the contact (cover-off test, strip seating), then consider a small end stop in each channel or a slightly shorter strip (about 0.4 mm shorter chord), both CAD changes you have not authorised. A shorter chord also stiffens the spring by roughly 10 %, so the cover feel would change.
3. **Strengthen the detent** (a firmer pawl): masks the drag rather than removing it; I would not choose this first.
4. Check the plain fit (inner ring bore against hub, diagnostic ring ladder) in case a general tolerance issue is part of it.
Please state which, and whether prototype testing should continue with two or three strips. The Sunday cutoff stands.
