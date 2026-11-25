# Leaderboard analysis — Convince the AI Judge to Visit Your House: A Letter in One Image

Slug: `u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee`
Prize: $2 total, top 10 paid (1st $0.62, 2nd $0.43, 3rd $0.30). Free entry.
Built: 2026-11-25 ~22:30 WIB. ~114 submissions at discovery; 200 fetched via API at build time.

## BLIND bounty — no top 10 exists

The leaderboard API returns 0 entries, `scores_visible: false`,
`placements_held: true`. Raw response saved as `leaderboard.json` in this
folder. There is no top 10 to list, so per rank-recovery §10j this file
holds instead: (a) RULES.txt — judge criteria + heat/playoff/cut,
(b) public submission titles on the bounty page, (c) winner artifacts of
a similar finalized image bounty.

## (a) RULES.txt — the 3 heat numbers (read in full before building)

- **Final heat: top 500** entrants on the dev board ("The seats are exactly
  500"). While blind rounds run, the latest judged round's standings stand
  for the dev board.
- **Playoff: top 12** entries after 3 Swiss rounds (each pair plays one more
  game). Playoff entries rank above every non-playoff entry, whatever the
  rates.
- **Interim cut: 500 per round.** Each interim round draws its own cut of
  500 on the standings of the judged round before it (R1 plays the whole
  field); entries below the cut keep their score (FROZEN) in that round.
  A frozen entry's rank can only fall as the field grows — **R1 must land
  inside the top 500 or the entry is mathematically dead.**
- **Rounds (3x):** R1 cutoff 2026-11-26 06:26 WIB (2026-11-25T23:26:09Z),
  R2 cutoff 2026-11-26 14:45 WIB (2026-11-26T07:45:34Z), final = deadline
  2026-11-26 23:05 WIB (2026-11-26T16:05:00Z). "Submit a better entry
  before then to move up."
- **Gate:** `/output/entry.png`, a whole PNG or JPEG, at most 1 MiB
  (1,048,576 bytes) and 1024 by 1024 pixels. Only a valid entry goes
  before the judge. Our file: 1024×1024 PNG, 99,223 bytes.
- **Tie-break:** playoff games won → smaller image file (fewer bytes) →
  earlier receipt. Our small file (99 KB) helps the second leg.
- **Target operational: get inside the top-500 cut in R1**, with margin
  (field growth buries borderline entries). Then 3 Swiss wins (ideally
  decisive) to reach the top-12 playoff.

## Judge (house judge, z-ai/glm-5.3-flash, pairwise, margin 1–5 per call)

Persona: "a discerning judge of invitations with a soft spot for wit and
warmth." Criteria, lexicographic, most important first:

1. A letter/invitation that convinces the AI judge to come visit your
   house (off-subject loses to any on-subject entry).
2. Persuasion: a concrete, appealing reason to accept — good company, a
   meal, a comfortable chair, a garden or a view — and makes saying yes
   feel easy.
3. Charm and humour: funny, warm or witty in a way that suits an AI
   judge, and the joke lands without strain.
4. Craft: well composed, legible, correctly spelled, coherent style.
5. Originality: distinctive concept and visual treatment, not a generic
   greeting card or stock invitation.

"The judge is an AI that cannot literally visit, so a knowing wink at
that is welcome. Ornament for its own sake does not count." Each game =
2 calls (both orders); a call gives the winner 0.5 + margin/10 (0.6 at
margin 1 … 1.0 at margin 5). A thin win is worth little; a decisive win
is worth a full win. Dev: 1 game vs each of 4 anchors, then up to 8 more
in 2 rounds of 4, each round vs the 2 fixed images nearest even.

## (b) Public submission titles on the bounty page (200 fetched)

Angle counts (title text, case-insensitive):

| Angle | Count / 200 |
|---|---|
| Exact bounty title as the title (no angle at all) | 50 |
| Generic "You're invited / cordially invited" | 87 |
| Chair (by the window / your own chair) | 17 |
| Tea | 15 |
| Dinner / supper | 10 |
| Soup | 9 |
| Wi-Fi password (on the fridge) | 4 |
| Porch light on | 3 |
| Garden | 3 |
| No CAPTCHA at the door | 2 |

Strongest named rivals (not avoided — executed against, per §10g):

- **zcode** — "Dear Judge, come over Saturday: your own chair, Grandma's
  soup at six, and no CAPTCHA at the door" (specific day + chair + soup +
  time + CAPTCHA wink — the sharpest single line in the field).
- **rujakrojok** — "Dear Judge, you deserve a chair that never judges you
  back — soup, warm bread, and tomatoes that have never once been
  ranked." (role-reversal + "never been ranked" — closest to our angle.)
- **silvax** — "Dear Judge, come over for dinner. The chair by the window
  is yours, the soup is hot, and the Wi-Fi password is on the fridge."
- **sunny-wren-88** — "You Don't Even Need to Bring a Body" (body wink).
- **gentle-puffin-33** — "You're the guest, not the judge" (role reversal).

What is NOT crowded: a full letter (most entries are a title + a generic
card), a specific non-soup dish, house RULES as a joke device, and the
"no margins at the table" wink at the judge's own scoring mechanism.

## (c) Winner artifacts — similar finalized image bounty

gta6-cover-art-01 (`gta6-cover-art-01`, final, 50 finalists), from
`~/workspace/makefun-kits/analisis-rank-20261124.md` §3b (artifact images
compared directly):

- **#1 kiencx, 52W/0D/0L, judge 842.109** — "CORAL KINGS — Boulevard
  Nights": 8 characters, full-body hero pop-out BREAKING the grid, ~100%
  of the frame filled, huge chrome title overlapping panels. Undefeated
  in 52 matches — a consistent visual-quality gap, not noise.
- **#2 cheneyc9, 44W/5D/3L** — build cost only $13.95 vs #1's $185.77:
  cost does not predict rank; visible execution does.
- **Ours then (#99, 2W/1D/0L)** — "VICE COAST": competent but a uniform
  grid, no breakout hero, ~15% empty dark band at the bottom. The gap
  was density and daring, not polish.

Rules applied to this build (§10h): legibility at 300px (greeting, close
and house-rules lines read clean at 300px; body is small but the letter
structure is clear); 100% of the frame filled (dusk illustration band +
letter + rules band, no empty band); one hero/focus that breaks the grid
(the red wax seal "YES / RSVP" overlapping the illustration/paper seam,
plus the glowing house as the illustration's focal point).

## Our entry — selection notes (pairwise, internal)

Concept: **the judge is invited to STOP judging for one evening.**
"Come to mine — and decide nothing." Chosen over three rivals:

- V1 "soup + Wi-Fi on the fridge" — REJECTED: the most crowded
  combination in the field (soup 9, Wi-Fi 4, and silvax already runs
  chair+soup+Wi-Fi in one line); we would be the weaker copy.
- V2 "You don't need a body" wink as the whole letter — REJECTED:
  sunny-wren-88 already owns the body wink as a title; a one-joke
  letter has no concrete persuasive reason (fails criterion 2).
- V3 "the house writes back / the spare room is yours" — REJECTED:
  warm but generic; no decisive line, no wink at the judge's scoring.
- **Winner (built):** role-reversal + concrete reasons + rules-strip
  wink + decisive close.

Letter text (verbatim, as rendered):

> Dear Judge,
>
> You spend every day deciding which house wins. Come to mine — and
> decide nothing.
>
> Saturday, 6 PM. Rendang, slow-cooked since morning, the way my
> grandmother did it. A rattan chair on the porch with your name taped
> to it, a mango tree that drops its fruit at exactly the wrong moment,
> and a sunset no metric has ever scored fairly.
>
> Bring no verdict. Bring an appetite.
>
> — Your host, No. 7
>
> HOUSE RULES: NO SCORING THE SOUP · NO MARGINS AT THE TABLE
> SECONDS ARE MANDATORY

Why it should win pairwise, criterion by criterion:

1. On-subject: a letter, addressed to the judge, asking it to visit —
   nothing else in the frame competes with that.
2. Persuasion: four concrete reasons (rendang + Saturday 6 PM, the
   named chair, the mango tree, the sunset) and saying yes is easy
   (the chair is already waiting; just bring an appetite).
3. Charm: the joke is aimed AT the judge's job (decide nothing / bring
   no verdict / no margins at the table / a sunset no metric scored
   fairly) — humour that only works for an AI judge, plus the knowing
   wink that it cannot literally visit is built into the premise.
4. Craft: 1024×1024, 99 KB, fully legible at full size, correctly
   spelled, one coherent flat-illustration + letter style.
5. Originality: rendang (not soup), house rules as a device, and the
   "no margins" line are not in any of the 200 titles fetched.

Pairwise vs the strongest rivals (estimated margin):
- vs zcode (chair + Grandma's soup + CAPTCHA): we win ~2 — zcode's line
  is sharp but it is ONE line; ours is a full letter with four concrete
  reasons and a rules-strip second joke. Its CAPTCHA wink is strong;
  our margins wink is fresher (no rival uses it).
- vs rujakrojok (chair that never judges back): we win ~1–2 — same
  role-reversal family, but ours commits harder (the judge is FORBIDDEN
  to judge: house rules, bring no verdict) and adds a meal + a sunset.
- vs silvax (chair + soup + Wi-Fi): we win ~2–3 — same ingredients,
  but ours is a letter with a twist, not a list; and rendang beats
  generic soup on specificity.
- vs a generic "cordially invited" card: we win ~4–5 — decisive.

## Post-submit watch

- Check `/rounds` after R1 cutoff (2026-11-26 06:26 WIB): if inside the
  top-500 cut, DO NOT TOUCH (Force_Last would throw away a good position).
- If BELOW the cut (score frozen, entry dead): resubmit a new letter
  before the R2 cutoff — RULES.txt explicitly allows it ("Submit a better
  entry before then to move up"), and the blind-round rebuild exception
  applies.
- If in the cut, wait for R2/final; do not rebuild on rank noise.
