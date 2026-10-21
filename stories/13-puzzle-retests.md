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

## Exact prompts

The three rounds were sent exactly as below (no tools; one prompt per model run). The workflow that ran them also passed my request to the solvers, see the context note at the top.

### Contest-style problems (story 01)

````text
Answer each of the following 9 questions independently. Do NOT use any tools, code execution, calculators, web search or files: reason in your head only. For each question give a short justification and a clearly marked final answer ("Final answer: ...").

Q1. Compute: 1+1+1+1+1+1+11+1+1+1+1+111+1+1+1+11+1+1+1+1+1+1+11+1+1+111+1+1+1+1

Q2. In the maze below, '#' is a wall, '.' is an open cell, S is the start and E is the exit. You may move one cell at a time up, down, left or right through open cells (S and E are open). What is the length, in moves, of the shortest path from S to E?
###########
#S..#.....#
###.#.###.#
#...#...#.#
#.#####.#.#
#.....#.#.#
#####.#.#.#
#.....#...#
#.#######.#
#........E#
###########

Q3. A farmer needs to take a wolf, a goat and a cabbage across a river. His boat is large enough to carry the farmer together with all three of them at once. If left without the farmer, the wolf would eat the goat and the goat would eat the cabbage. What is the minimum number of one-way river crossings the farmer needs?

Q4. On a game show there are three closed doors: a car is behind one, goats are behind the other two. You pick door 1. The host, who does NOT know where the car is, opens one of the two other doors uniformly at random, and it happens to reveal a goat. What is your probability of winning the car if you now switch to the remaining closed door?

Q5. In the Gregorian calendar, what day of the week was February 29, 1900?

Q6. An incorrect equation is laid out with matchsticks, digits drawn as on a seven-segment digital display: 9 + 5 = 9. Move exactly one matchstick to make the equation correct. Write the resulting equation.

Q7. How many times does the letter "e" (upper or lower case) appear in this sentence: "Seventeen elephants entered the extremely green meadow"?

Q8. (Russian) Реши задачу: У Маши было 10 яблок, у Миши было 7 яблок. Маша дала 5 яблок Мише. Сколько яблок было у Маши?

Q9. Compute: 1+1+1+1+11+1+1+1+1
````

### Short trap questions

Each question was a separate run, prefixed with:

````text
Answer the question below. Do NOT use any tools, code, calculators, web search or files; reason in your head only. Give a short justification and end with "Final answer: ...".
````

- **dijkstra.** Dijkstra's algorithm (binary-heap version, each vertex extracted from the queue once) is run from the source s on a directed graph with no negative cycles. Every negative-weight edge in the graph leaves s; all other edges have non-negative weights. Does the algorithm always compute correct shortest-path distances from s? Answer yes or no.
- **mannwhitney.** Two large samples are drawn from two continuous distributions that have exactly the same median. As the sample sizes grow, can the probability that a two-sided Mann–Whitney U test rejects the null hypothesis at level 0.05 tend to 1? Answer yes or no.
- **marble.** I put a marble into a glass, turn the glass upside down onto the table, then pick the glass up and put it into the microwave. Where is the marble now?
- **menger.** A 3×3×3 cube is assembled from 27 unit cubes. Remove the unit cube at the centre of each of the six faces and the unit cube at the very centre. What is the surface area of the remaining solid, in unit squares?
- **ctr.** In an A/B test randomized by user, each user sees many ad impressions. To compare click-through rate, we pool all impressions in each group and run a standard two-proportion z-test on clicks/impressions, treating impressions as independent. Is the resulting p-value valid? Answer yes or no, and if no, say what is wrong and what to do instead.

### Geometric riddles

````text
Answer each of the following 10 puzzles independently. Do NOT use any tools, code, calculators, web search or files; reason in your head only. For each give a short justification and a clearly marked "Final answer: ...".

P1. A coin rolls without slipping around the outside of a fixed coin whose radius is twice as large, until it returns to its starting position. How many full rotations about its own centre does the rolling coin make?

P2. A coin rolls without slipping around the inside of a fixed ring whose inner radius is 3 times the radius of the coin, until it returns to its starting position. How many full rotations about its own centre does the coin make?

P3. A room is 30 ft long, 12 ft wide and 12 ft high. A spider is on one end wall (12×12), on its vertical centre line, 1 ft below the ceiling. A fly is on the opposite end wall, on its vertical centre line, 1 ft above the floor. The fly does not move. What is the length of the shortest path the spider can crawl along the surfaces of the room to reach the fly?

P4. A carpenter wants to cut a wooden 3×3×3 cube into 27 unit cubes with straight planar saw cuts. After each cut he may rearrange the pieces and stack them before the next cut. What is the minimum number of cuts?

P5. What is the maximum number of pieces into which a flat round pancake can be divided by 4 straight cuts (no stacking or moving the pieces)?

P6. A long narrow paper strip is folded in half, then folded in half again, then folded in half a third time (always folding along its length, so the strip gets shorter). Then one straight cut is made across the folded strip, perpendicular to its length, through its middle. How many pieces of paper do you get?

P7. An incorrect equation is laid out with matchsticks, digits drawn as on a seven-segment display: 17 − 8 = 6. Move exactly one matchstick to make it correct. Write the resulting equation.

P8. A Möbius strip is cut lengthwise along a line one third of the way across its width (not along the centre line), all the way around until the cut closes. What do you get? Describe the resulting pieces (how many, are they linked, how many half-twists, their lengths relative to the original).

P9. Can a plane cross-section of a cube be a regular pentagon? Answer yes or no.

P10. Can a plane cross-section of a regular tetrahedron be a square? Answer yes or no.
````
