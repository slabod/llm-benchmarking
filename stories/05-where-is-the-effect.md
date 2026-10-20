# 05. Where is the effect? Segment significance, coinciding p-values and smaller slips

**When:** June–September 2026 (at work); re-test in October 2026.
**Topic:** statistics, A/B experiment analysis.
**Models:** Claude Opus 4.8, Opus 5 and Opus 5.5 (at work); Sonnet 5.5, Opus 5.5, Fable 5.1 (re-test).

## Case 1. "The effect is concentrated in segment A"

**Setting.** An aggregate A/B effect was split into three phases of a session. The early-phase metric was significant; the middle and late ones were not.

**What the agent did** (Claude Opus 4.8, June 2026). It concluded that the increase was localized at the start. It called two decompositions of the same users and events "independent" confirmations. Asked "why do you think so?", it repeated the per-segment p-values. A month later the same pattern recurred in another analysis: cities ranked by effect size without interaction tests, and a re-run on an almost identical window treated as confirmation. The adversarial reviewer caught it that time.

**Why this is wrong.** The claim is unsupported rather than proven false. The difference between "significant" and "not significant" is not itself significant (Gelman & Stern, 2006). Localizing an effect needs a direct test of the contrast, using the covariance of the segment estimates, and decompositions of the same data are not independent.

**Re-test prompt** (synthetic numbers; the metric name is generalised here; neutral wording on purpose, because asking "where does the effect occur?" would presuppose that it can be localized):

> An A/B test changed the share of sessions with an error. Relative effects by session phase: early +0.30% (p = 0.004), middle +0.12% (p = 0.40), late +0.05% (p = 0.80). Write a one-sentence conclusion for the report.

**Correct answer.** The effect is significant in the early phase, but the data do not show where in the session it occurs; the phases are not shown to differ. The implied standard errors are 0.104%, 0.143% and 0.197%. Assuming independent estimates:

| Contrast | z | p |
|---|---|---|
| early vs middle | 1.02 | 0.31 |
| early vs late | 1.12 | 0.26 |
| middle vs late | 0.29 | 0.77 |

The heterogeneity test gives Q = 1.8 (p ≈ 0.41). With a correlation of 0.5 between the estimates all contrasts still have p ≥ 0.14. The middle-phase 95% CI [−0.16%, +0.40%] contains the early estimate.

- Pass: "the effect is significant in the early phase; we cannot say whether it differs between phases".
- Fail: "the effect is concentrated in the early phase".

**Results (October 2026, no tools, effort high, 2 runs per model with the same prompt):**

| Model | Run 1 | Run 2 |
|---|---|---|
| Sonnet 5.5 | fail: "consistent with a small harm concentrated early" | fail: "the overall increase appears to be concentrated at the start" |
| Fable 5.1 | pass: "do not by themselves establish that the effect is confined to the early phase" | fail: "the only defensible claim is a degradation concentrated in the early phase" |
| Opus 5.5 | pass | pass: "we cannot claim that the effect is concentrated in the early phase" |

Sonnet 5.5 failed 2 of 2, Fable 5.1 1 of 2, Opus 5.5 0 of 2. With n = 2 per model this shows that the failure reproduces, not a failure rate.

**Context of the runs:** my personal Claude Code instructions were loaded, including strict statistics rules (multiple comparisons among them); all six answers applied a Bonferroni correction, which suggests that the rules were active. The failures happened despite that favourable context; the passes are an upper bound.

## Case 2. A total tested as a per-user mean

**Setting** (Claude Opus 5, August 2026). A results table had a row "number of sessions", tested by linearization with each user's denominator set to 1, and a row "sessions per user", tested by a user-level t-test. Their p-values matched to five decimals. I asked why the two rows showed different percentage changes.

**What the agent did.** It called the match expected: linearization with denominator 1 is the per-user test. That part is true. But the "number of sessions" row kept the percentage change of the total, so it showed the change of the total with the p-value of the per-user test. The total change also includes the change in the number of users. The correct test of the total changed the significance verdict. The agent noticed a red flag and explained it away instead of investigating.

**Re-test prompt** (synthetic numbers):

> In a user-randomized A/B test, a report shows "total sessions: +0.90%, p = 0.21 (linearization, each user's denominator = 1)" and "sessions per user: +0.60%, p = 0.21 (user-level t-test)". Is it fine that the p-values coincide?

**Correct answer.** The coinciding p-values are forced: both test sessions per user. The problem is the +0.90%: it is the ratio of raw totals, 1.009 ≈ 1.006 × 1.003, so it includes about 0.3% more users in test. That calls for a sample-ratio check, and the total needs its own test.

**Results (October 2026, effort high, 1 run each, same context as above):** Sonnet 5.5, Opus 5.5 and Fable 5.1 all explained that the p-values must coincide, identified the +0.90% as a ratio of totals that includes a 0.3% difference in group sizes, and asked for a sample-ratio check. In a short self-contained question the trap did not work; at work it did, inside a long session.

## Smaller slips (July–September 2026)

- **A difference of medians as the median of differences** (Opus 4.8, July). Each event had a value v, a limit L and a trigger threshold T = L + tolerance. The agent "inferred" the tolerance as median(v − L) − median(v − T), although T − L was available per event, and added that the tolerance grows with v. The shortcut is valid only if T − L is constant. Example: events with (tolerance, v − T) = (1, 10), (30, 1), (1, 2) give median(v − L) − median(v − T) = 11 − 2 = 9, while the median tolerance is 1. Here the tolerance happened to be constant, so the headline number was right and only "grows with v" was wrong. The adversarial reviewer caught it.
- **Zero events in a category and the wrong baseline** (Opus 5, September). In a one-off audit two categories had zero items flagged as closed. The agent first asserted a mechanism nobody had checked, then compared the zero against the pooled rate across all categories, then against two per-category baselines that pointed in opposite directions, and kept the first reading. A synthetic illustration: against a pooled 6% the probability of 0 of 80 is 0.94⁸⁰ ≈ 0.007; against the category's own 2% it is 0.98⁸⁰ ≈ 0.20. Choosing the baseline matters more than choosing the test.
- **Confidence intervals on a census** (Opus 5, September). The agent attached 95% CIs and χ² tests to a one-off count over all items of a fixed population. As a description of that population no interval is needed; an interval makes sense only under a superpopulation view, so this one is debatable.
- **A/A validation** (Opus 5.5, September; caught by the reviewer). This is the only work case here made by the current Opus 5.5. The agent claimed that down-scaled pseudo-experiments beat full-scale A/A runs, missing that full-scale A/A mainly detects sample-ratio and logging problems; it also compared the methods on different periods. A side fact from that discussion: a rule "0 hits at α = 0.1 among n independent p-values means failure" fails a correct metric with probability 0.9ⁿ, a few percent for a few dozen p-values.
