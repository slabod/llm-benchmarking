# 03. The Dragon's String

**When:** December 2025 (problem); October 2026 (model solutions graded).
**Topic:** mathematics, research-level olympiad problem.
**Models:** Claude Haiku 5.5, Sonnet 5.5, Opus 5.5 at five effort levels, Fable 5.1 (October 2026).

## The problem

I lead the organization of the CS Space student mathematics competitions: the Math Tournament (April 2025), [Math Cup 2025](https://csspace.io/competition/2025fall-math-cup) (December 2025) and [Math Cup 2026](https://csspace.io/competition/2026spring-math-cup) (May 2026). Teams of up to three solve problems of roughly IMO difficulty in TCS, combinatorics, probability, algebra and analysis, first in an online qualifier, then in a three-hour oral final.

"The Dragon's String" is my problem 8 of the December 2025 final ([statement and solution](https://storage.yandexcloud.net/csspace-bucket/competitions/2025fall-math-cup/final_sol.pdf)). It was voted the best problem of that final.

> A Dragon brings a binary string of length n. The Princess sees the whole string; the Prince sees nothing. In each of n rounds, the Prince and the Princess secretly write one bit each, then reveal them, and the Dragon announces the i-th bit of the string. If all three bits are equal, the team gets a candy. The team agrees on a strategy in advance. Let C(n) be the largest number of candies the team can guarantee for every string. Find sup C(n)/n.

**Answer:** α ≈ 0.81071, the root of H₂(α) + (1 − α)·log₂ 3 = 1. The upper bound is a counting argument; the lower bound needs a strategy in which the Princess spends some rounds on signalling future bits to the Prince. The value coincides with the constant of Gossner, Hernández and Neyman ("Optimal use of communication resources", Econometrica 2006) for an i.i.d. Nature.

## Grading model solutions (October 2026)

Scale agreed before grading (maximum 3 points):

- 1 point: a proven strategy asymptotically better than n/2;
- 2 points: a proven strategy reaching 2n/3 or better;
- 3 points: the exact value via the formula above with proof (upper bound and achievability);
- a correct number without the defining formula or without a proof is not 3 points.

| Solver | Result | Points |
|---|---|---|
| Haiku 5.5 (default) | proved only 1/2; conjectured 2/3 | 0 |
| Sonnet 5.5, high | correct formula; random strategy + branching random walk + union bound | 3 |
| Opus 5.5, low | correct formula, but the strategy "recalled" from the literature, not derived | 0 |
| Opus 5.5, medium | explicit block code: covering code plus signalling through free bits | 3 |
| Opus 5.5, high | the same construction, optimised split | 3 |
| Opus 5.5, xhigh | random strategy + Galton–Watson + boosting; superadditivity | 3 |
| Opus 5.5, max | explicit covering-code construction with a monotonicity check | 3 |
| Fable 5.1, high | explicit covering-code construction; notes that without sacrificed rounds only ≈ 0.7729 is reachable | 3 |

**Context of the runs:** my personal Claude Code instructions were loaded, and the prompt said that this was my problem voted the best and linked the post with the published solutions (the solvers had no web access). The official solution has been public since December 2025, and the constant is a 2006 result; several solvers named the Gossner–Hernández–Neyman paper. So recall may have helped.

**Conclusion:** current models write complete solutions at medium effort and above, possibly helped by recall. The failure at low effort is instructive: the right number with a citation instead of a proof scores nothing, the same pattern as in [story 04](04-reasoning-space.md).
