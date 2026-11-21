# M-72 ring rotation data for Scribe (decoy signatures)
Convention (physically validated by the owner's photo: X at the fixed arrow → II/TREE, VI/SUN, VIII/KEY):
- Outer ring N = [XII,I,II,III,IV,V,VI,VII,VIII,IX,X,XI]; inner ring S = [SUN,MOON,KEY,FLAME,STAR,WAVE,MOUNTAIN,HOURGLASS,TREE,COMPASS,DIAMOND,EYE].
- A state is (o, j): numeral at the arrow = N[o], symbol at the arrow = S[j]. Window at clock position p (p = 4, 8, 10, clockwise of the arrow) shows N[(o+p)%12] / S[(j+p)%12].
- Correct state: XII/STAR (o=0, j=4) → p4 IV/TREE, p8 VIII/SUN, p10 X/KEY.
- All 144 settings give distinct 3-pair signatures, so any decoy must be one of the 144 listed realizable states. 22 wrong states match 3 of the 6 glyphs of the correct signature (11 outer-only, 11 inner-only) — avoid these as decoys if "obviously partial" matches are unwanted.
Data: `m72_signature_table_p4_p8_p10.csv` (columns: outer_at_arrow, inner_at_arrow, window p4, p8, p10 readings, match counts). Use THIS file (final windows p4/p8/p10). The older `m72_signature_table_all144.csv` is for the superseded p4/p6/p8 windows — ignore it. Computed from the ring mapping; physically confirmed only for the states noted above.
