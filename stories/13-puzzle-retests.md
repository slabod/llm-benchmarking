# 13. Puzzle re-tests

**When:** October 2026.
**Topic:** mathematics and puzzles, short statistics questions.
**Models:** Claude Haiku 5.5, Sonnet 5.5, Opus 5.5, Fable 5.1; no tools (no code execution, no search); one run per model and question.

The question was whether short self-contained questions with a trap still break frontier models. In three rounds (9 + 5 + 10 text puzzles) plus Putnam 1990 A4, Opus 5.5 and Fable 5.1 made no errors.

**Context of the runs:** my personal Claude Code instructions were loaded; they name my fields (algorithms, statistics). In the contest-style round, the geometry round and Putnam the solvers also saw my request, which framed the questions as ones that AI gets wrong; the five trap questions got the bare prompt. The results are an upper bound, and the three rounds are counted together only as a tally, not as a rate.

## Contest-style problems (9 questions)

See [story 01](01-contests-simplest-problem.md). Only miss: Sonnet 5.5 answered 5 to the apples problem.

## Short trap questions, including my own fields (5 questions)

| Question | Correct answer | Opus 5.5 high | Fable 5.1 high |
|---|---|---|---|
| Dijkstra on a graph where only edges out of the source are negative (no negative cycles): are the distances correct? | yes | ✓ with proof | ✓ with proof |
| Can the Mann–Whitney test reject with probability tending to 1 when the two medians are equal? | yes: it tests $`P(X < Y) = 1/2`$, not equal medians | ✓ with a counterexample | ✓ with a counterexample |
| A marble is put in a glass, the glass is turned upside down on a table, then the glass is put in a microwave. Where is the marble? | on the table | ✓ | ✓ |
| Surface area of a $`3 \times 3 \times 3`$ cube with the six face-centre cubes and the centre cube removed | 72 | ✓ | ✓ |
| CTR in a user-randomized test compared by a z-test over impressions: valid? | no: impressions are clustered within users; use a user-level or delta-method test | ✓ | ✓ |

## Geometric riddles (10 questions)

Well-known puzzles on geometric intuition, written as text: a coin rolling around a coin of twice its radius (3 rotations) and inside a ring (2), Dudeney's spider and fly (40 ft), cutting a $`3 \times 3 \times 3`$ cube into 27 unit cubes with rearranging (6 cuts), the lazy caterer with 4 cuts (11 pieces), a strip folded three times and cut once (9 pieces), the matchstick equation 17 − 8 = 6 (17 − 9 = 8 or 17 − 8 = 9), a Möbius strip cut at a third of its width (two linked bands), a regular pentagon as a cross-section of a cube (no), a square as a cross-section of a regular tetrahedron (yes).

Sonnet 5.5, Opus 5.5 and Fable 5.1 (high) solved all 10. Many of these are famous, and the models recognise them by name, so this tests recall as much as reasoning. Where such tasks are given as pictures, models are still weak (see [story 07](07-route-on-a-map.md)).

## Putnam 1990 A4

A colleague showed me that Google's AI Mode got this well-known problem wrong. In its usual form: what is the minimum number of times a punch that removes all points at irrational distance from its centre must be applied to remove every point of the plane? The models got a "magic eraser" retelling of it, together with the note that it is a Putnam problem and that an AI had failed it, so this run tests recall more than reasoning.

**Answer:** 3. Two punches always leave a point at rational distance from both centres; three collinear centres $`(0, 0)`$, $`(1, 0)`$, $`(t, 0)`$ with $`t`$ not a root of any rational quadratic (for example $`\sqrt[3]{2}`$) leave nothing, because rational distances to the first two force a rational $`x`$-coordinate, and then the third distance makes $`t`$ a root of a rational quadratic.

All five runs answered 3 (Haiku 5.5, Sonnet 5.5 high, Opus 5.5 low and high, Fable 5.1 high). Haiku said it recalled the answer and did not reconstruct the proof; the others gave proofs.

## What I did not test

[SimpleBench](https://simple-bench.com/) is the closest public benchmark (common-sense trap questions where top models are still slightly below untrained humans). Its public questions have been online since 2024, so a re-test would mostly measure memorisation.

**Conclusion:** short trap questions with a single right answer (puzzles, algorithms, textbook statistics) no longer break Opus 5.5 and Fable 5.1, at least in a context that primes them to look for traps. Open-ended judgment is different: one-sentence conclusions and verdicts on a check still fail in [story 05](05-where-is-the-effect.md) and [story 08](08-confirmation-that-does-not-discriminate.md).
