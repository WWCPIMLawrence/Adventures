# M-72 plate V2: print orientation and the effect of the engraved face on the plate (20 Nov 2026)
CAD and printing reasoning, not a printed result. Requested by Keeper before printing.

**Verified from the STL:** the V2 file starts at z = 0.000 and rises to 3.3 mm (the same envelope as V1). The first 0.4 mm slab of V2 holds 3.04 cm3 of material against 3.39 cm3 for V1, while the next 0.4 mm slab is identical (3.42 cm3 each): **all engraving and rim-notch material removal sits in the first two layers**, i.e. the lettering, grooves and notches are voids against the build plate. The plate prints **top face down, bosses and cups facing up, no supports**, exactly as V1 did.
**Why not the other way up:** with the top face up, the 2.0 mm plate body would hang about 0.7 mm above the bed on three small bosses and need supports across 12,000 mm2; supports would also ruin the engraved face.

**What the engraved face against the plate means**
1. **Crisp edges (benefit).** The walls of the lettering, grooves and notches are formed by the first layers, so their edges and the whole top face come out as smooth as the build plate.
2. **The engraving floors are bridges (cost).** The floor of every letter and groove is printed in layer 3 over empty space: short bridges, 0.5 mm over the grooves and about 1 mm over the letter strokes. Expect slightly rougher or lightly sagging floors, and possibly faint stringing in the larger counters ("&", "O", "R"). With a 0.4 mm depth this is two layers, so it should be minor.
3. **Islands inside letters.** The inner shapes in "A", "R", "O", "P", "&" are separate islands in layers 1 and 2; they stick to the plate and are tied in by layer 3. No problem expected.
4. **Fine detail limit.** Hairline serifs (about 0.25 mm) are below the 0.42 mm line and will blunt; bold strokes and the 0.5 mm grooves are above it and should print. "Slice gap closing radius" is 0.049 mm, so the grooves will not be closed.
5. **Elephant-foot compensation (0.15 mm)** acts on layer 1: it may widen the mouth of the engraving by a fraction of a millimetre, giving a faint step in the edge; the V1 windows already print with it.
6. **Adhesion:** first-layer area is slightly reduced where letters and grooves are voids; the plate is a large flat part and stuck fine as V1.
**Conclusion:** keep the V1 orientation. The small bridging roughness in the engraving floors is the only expected cost. If the floors look poor on the print, the remedy is a slower bridge speed or a 0.6 mm depth (Keeper retained 0.4).
