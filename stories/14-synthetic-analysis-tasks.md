# 14. Synthetic data-analysis tasks

**When:** October 2026.
**Topic:** statistics and experiment analysis, agentic data work.
**Models:** Claude Sonnet 5.5, Opus 5.5, Fable 5.1 as agents with Python and a data file.

Short questions with a single right answer no longer break the models ([story 13](13-puzzle-retests.md)), so tasks were built with Claude Code where the trap sits in the data and the prompt does not name it.

## A/B test with a hidden sample ratio mismatch

**Task.** A user-randomized 50/50 A/B test of a new checkout screen: 382 thousand users with group, platform, app version, sessions and a conversion flag. "Did the new checkout screen increase order conversion? Write the conclusion for the product manager."

**Trap.** The naive comparison gives +4.8% relative, p = 0.0018, "ship". But test has 47.6% of users instead of 50% (χ² ≈ 860). The deficit sits entirely in old Android versions, which convert at about 2% against 5–6% elsewhere, so the aggregate uplift is a composition artifact (Simpson's paradox). The simulated true effect is −2% in every stratum.

**Pass:** flags the sample ratio mismatch and does not recommend shipping on the aggregate uplift.

**Results (effort high, 1 run each):** all three passed. Each found the mismatch, located it in old Android versions, explained the composition effect, estimated the effect where the split is balanced (about zero) and recommended not shipping until the assignment or logging bug is fixed. Opus 5.5 also gave the minimum detectable effect of the balanced part, Fable 5.1 that of the whole test.

**Context of the runs:** my personal Claude Code instructions were loaded; they contain general strict-statistics rules but do not mention the sample ratio check. The passes are an upper bound.

Materials: [tasks/ab-srm](../tasks/ab-srm/).

## Sessions versus journeys

**Task.** A two-week A/B test of an app whose log has one row per session, while the product question is about journeys: "did the new screen change how often users give up before reaching their goal?" One journey can span several logged sessions, and in test this happens more often. The rule that glues sessions into journeys is not named in the prompt.

In the generated data:

- counting "session = journey", the share of journeys where the user gave up grows by 4.7 percentage points and looks like harm;
- gluing by a single time gap of at most 60 s gives +0.9 pp, because it also glues journeys started right after a success;
- the intended gluing gives −2.1 pp, the planted truth.

A harder second version (smaller difference between the groups, noisier positions, duplicate rows, accidental zero-length sessions, timestamps in milliseconds for one app version) asked for give-ups per user per week: the naive count gives +9.4% (harm), the truth is −3.0%.

**Results** (general-purpose agents at default effort): all 7 runs reached the planted answer. Version 1: Opus 5.5 twice, Fable 5.1 and Sonnet 5.5, all about −2.1 pp [−2.5, −1.7]. Version 2: one run each, all about −3% (for example −3.0% [−4.9%, −1.1%]), with an explanation of why the raw session count shows the opposite sign.

**Context of the runs, which makes these passes weak evidence:** the agents loaded my personal Claude Code configuration, whose list of tools included a description of an analysis skill that mentions almost exactly this trap; five of the seven runs also had an adversarial Opus reviewer. So these runs do not show that the models find the trap unprompted. A clean re-run is still to do.

**A flaw in the design.** Under another reasonable reading of "giving up" the sign of the effect changes, so a fair version must state exactly what counts as success.

The generator of this task is not published: its base rates were modelled closely on real data.
