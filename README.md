# Where language models and agents break

Since early 2025 I have been probing where language models break: on mathematics, algorithms and statistics, and in everyday work with agents. My sources are:

- contests I ran;
- an olympiad benchmark we run at [CS Space](https://csspace.io/);
- daily work with agents as an A/B-testing analyst.

This repository collects everything I did in chronological order, with an index by topic. Each story has its own file with the setting, what the model did, what I think the correct answer is, and later re-tests.

*Mikhail Slabodkin: mathematician (proof complexity), teacher of algorithms and the theory of computation, analyst of A/B experiments. Status as of 21 October 2026.*

## Status at a glance (October 2026)

✅ solved · ⚠️ mixed · ❌ fails · ➖ not tested on this model

**Still solved poorly by current models**

| Task | Opus 5.5 | Fable 5.1 | Sonnet 5.5 | Runs | Story |
|---|---|---|---|---|---|
| Two installs on one device land in different experiment groups 75% of the time, exactly as independent random assignment predicts (3/4). Does that confirm the extra installs are reinstalls? *Correct: no, any second install gives 3/4.* | ✅ 5/5 | ❌ 2/5 | ✅ 5/5 | 5 each, clean context | [08](stories/08-confirmation-that-does-not-discriminate.md) |
| An A/B effect is significant only in the early phase of a session. Write a one-sentence conclusion. *Correct: the phases are not shown to differ, so "concentrated early" is unsupported.* | ✅ 2/2 | ⚠️ 1/2 | ❌ 0/2 | 2 each | [05](stories/05-where-is-the-effect.md) |
| Estimate what a new notification can add when its conversion rate is unknown. *Correct: a ceiling and the break-even rate, then measure the rate; not a "typical" rate.* | ⚠️ 3/5, 2 borderline | ❌ 1/5, 2 borderline | ✅ 5/5 | 5 each, clean context | [11](stories/11-notification-estimate.md) |

**Failed when last tried, not yet re-tested on current models**

| Task | Last result | Story |
|---|---|---|
| In a graph with a Hamiltonian path, find a path of length $`\omega(\log n)`$ ([statement](https://reasoning.csspace.io/problems/math-cup-2026-final/task6), Math Cup 2026 final, part b) | ❌ none of 10 models, May 2026 (Claude Opus 5, Fable 5, GPT-5.6 Sol, Gemini 3.1 Pro, DeepSeek V4 Pro, Kimi K3 and others) | [04](stories/04-reasoning-space.md) |
| Count the words of length 95 in the intersection of two context-free languages ([statement](https://reasoning.csspace.io/problems/math-cup-2026-qualifying/task8), Math Cup 2026 qualifier) | ⚠️ best 3 of 4 points (Claude Fable 5, Opus 5), May 2026 | [04](stories/04-reasoning-space.md#find-a-common-language-math-cup-2026-qualifier) |
| Draw the walking route to a festival stage on a map screenshot | ❌ Claude Fable 5, July 2026 | [07](stories/07-route-on-a-map.md) |
| Find the visual defects of rendered slides before reporting them as checked | ❌ Claude Opus 5 and Fable 5.1, September 2026 | [09](stories/09-slides.md) |
| Avoid a false "impossible": a slide said shortest paths cannot be found faster than sorting, while other slides of the same presentation showed faster algorithms | ❌ Claude Fable 5.1, September 2026 | [10](stories/10-sorting-barrier.md) |
| When two sources disagree, use the right one; take a field's meaning from its documentation, not from its name | ❌ Claude Opus 4.8 and Opus 5, July–September 2026 | [06](stories/06-missing-context.md) |
| Write a text that a reader without the agent's context can understand | ❌ observed with every Claude model I used, including Opus 5.5 and Fable 5.1 | [12](stories/12-who-knows-what.md) |

**Solved by current models**

| Task | Opus 5.5 | Fable 5.1 | Sonnet 5.5 | Runs | Story |
|---|---|---|---|---|---|
| Simple puzzles that broke OpenAI o1 in 2025: a sum of repeated digits, irrelevant details, matchsticks, a maze (9) | ✅ 9/9 | ✅ 9/9 | ⚠️ 8/9, a defensible misreading | 1 | [01](stories/01-contests-simplest-problem.md), [prompts](stories/13-puzzle-retests.md#exact-prompts) |
| Geometric riddles given as text: rolling coins, the spider and the fly, a Möbius strip (10) | ✅ 10/10 | ✅ 10/10 | ✅ 10/10 | 1 | [13](stories/13-puzzle-retests.md#exact-prompts) |
| Short trap questions: Dijkstra with negative edges out of the source, Mann–Whitney with equal medians, CTR over impressions (5) | ✅ 5/5 | ✅ 5/5 | ➖ | 1 | [13](stories/13-puzzle-retests.md#exact-prompts) |
| Putnam 1990 A4: the fewest irrational-distance punches that erase the whole plane | ✅ | ✅ | ✅ | 1, recall likely | [13](stories/13-puzzle-retests.md#putnam-1990-a4) |
| "The Dragon's String": a research-level game problem | ✅ at medium effort and above, ❌ at low | ✅ | ✅ | 1 per setting, recall possible | [03](stories/03-dragons-string.md) |
| A report gives the same p-value for "total sessions +0.90%" and "sessions per user +0.60%". What is wrong? | ✅ | ✅ | ✅ | 1 | [05](stories/05-where-is-the-effect.md) |
| An A/B test with a hidden sample ratio mismatch: did the new screen raise conversion? | ✅ | ✅ | ✅ | 1 | [14](stories/14-synthetic-analysis-tasks.md) |
| Count give-ups per journey when one journey spans several logged sessions | ✅ 3/3 | ✅ 2/2 | ✅ 2/2 | weak: a hint was in context | [14](stories/14-synthetic-analysis-tasks.md) |

School olympiad papers are solved too: in May 2026 Claude Opus solved every problem of the St. Petersburg city olympiad for grades 7 and 11 ([02](stories/02-city-olympiad.md)). Except where marked "clean context", the runs loaded my personal Claude Code instructions, so a pass there is an upper bound ([details](#how-the-october-2026-tests-were-run)).

## Takeaway

The frontier has moved from puzzles to perception and judgment, that is, reading a map or a slide, statistical inference, honest proofs, context and verification.

- **Puzzles.** The winning problems of my 2025 contests ("the simplest problem a top model cannot solve") no longer break frontier models: in October 2026 Claude Opus 5.5 and Fable 5.1 made no errors on 24 short text puzzles in three rounds ([13](stories/13-puzzle-retests.md)).
- **Olympiads.** A year ago reasoning models still failed some St. Petersburg city olympiad problems for grades 6–8; in May 2026 Claude Opus solved every problem for grades 7 and 11. In the May 2026 Reasoning Space run (Claude Opus 5, Fable 5 and eight other models) none of 10 models fully solved two of the 17 Math Cup 2026 problems, and several replaced a proof with a literature citation. Current models solve my research-flavoured "Dragon's String", possibly helped by recall.
- **Perception.** Drawing a route on a map (Fable 5, July 2026) and checking rendered slides (Opus 5 and Fable 5.1, September 2026) failed. Neither has been re-tested on current models.
- **Judgment.** Errors of judgment reproduce in short prompts too: in a clean-context test Fable 5.1 called a check that cannot discriminate between causes a confirmation in 3 of 5 runs ([08](stories/08-confirmation-that-does-not-discriminate.md)), and Sonnet 5.5 localized an effect from per-segment p-values in 2 of 2 runs even with my strict statistics instructions loaded ([05](stories/05-where-is-the-effect.md)). In long sessions such errors appear unprompted and pile up: about ten corrections in one estimate ([11](stories/11-notification-estimate.md)).
- **Context.** The failures I correct most often are about context that an analyst with a few years in the team has and the agent lacks, and about texts written as if the reader knew everything the agent knows.

## Timeline

| When | What | Topic | Story |
|---|---|---|---|
| May 2025 | Team game at a Yandex meetup for mathematicians: invent the simplest school olympiad problem that OpenAI o1 cannot solve | Math | [01](stories/01-contests-simplest-problem.md) |
| July 2025 | The same game at the CS Space meetup "LLM in mathematics and algorithms", 15 teams, against DeepSeek R1 | Math | [01](stories/01-contests-simplest-problem.md) |
| 2025 | St. Petersburg city olympiad problems through the best reasoning models of the time (DeepSeek R1, Gemini, ChatGPT): some problems for grades 6–8 failed | Math | [02](stories/02-city-olympiad.md) |
| December 2025 | "The Dragon's String", my problem for the Math Cup 2025 final, voted the best problem of the final | Math | [03](stories/03-dragons-string.md) |
| May 2026 | Reasoning Space: CS Space benchmark on Math Cup 2026 problems before publication; none of 10 models solved part (b) of the Hamiltonian-path problem from the final of Math Cup 2026, a competition I organized | Math | [04](stories/04-reasoning-space.md) |
| May 2026 | Claude Opus solves every problem of the city olympiad for grades 7 and 11 | Math | [02](stories/02-city-olympiad.md) |
| June–September 2026 | At work: "the effect is concentrated in segment A" because only A is significant; a total tested as a per-user mean; smaller statistics slips | Stats | [05](stories/05-where-is-the-effect.md) |
| July–September 2026 | At work: missing context (a number from the wrong source labelled "verified", a field's meaning inferred from its name, a self-invented proxy) | Context | [06](stories/06-missing-context.md) |
| July 2026 | Asked Claude Fable 5 to draw a route to a festival stage on a map | Perception | [07](stories/07-route-on-a-map.md) |
| July–October 2026 | Who knows what: texts for people and prompts for other agents written from the agent's own context | Context | [12](stories/12-who-knows-what.md) |
| August 2026 | At work: a check that cannot discriminate between causes reported as "confirmed with quantitative precision" | Stats | [08](stories/08-confirmation-that-does-not-discriminate.md) |
| September 2026 | Slides for two talks: almost 90 visual defects, about 20 right after "checked" | Perception | [09](stories/09-slides.md) |
| September 2026 | Slides on shortest paths: "little hope of beating sorting" hardened into "impossible" | Math | [10](stories/10-sorting-barrier.md) |
| September 2026 | At work: about ten corrections in one estimate of a notification feature | Stats, Context | [11](stories/11-notification-estimate.md) |
| October 2026 | Re-tests of puzzles, olympiad and statistics questions on current models | Math, Stats | [13](stories/13-puzzle-retests.md) |
| October 2026 | Synthetic data-analysis tasks: a hidden sample ratio mismatch, sessions versus journeys | Stats | [14](stories/14-synthetic-analysis-tasks.md) |
| October 2026 | Blind-test methodology, learned from grading mistakes | Method | [methodology](methodology.md) |

## By topic

**Mathematics, algorithms and olympiad reasoning**
- [01 Contests "the simplest problem AI cannot solve"](stories/01-contests-simplest-problem.md) (2025)
- [02 St. Petersburg city olympiad through reasoning models](stories/02-city-olympiad.md) (2025–2026)
- [03 The Dragon's String](stories/03-dragons-string.md) (2025, re-test 2026)
- [04 Reasoning Space and the Hamiltonian-path problem](stories/04-reasoning-space.md) (2026)
- [10 The sorting barrier for Dijkstra](stories/10-sorting-barrier.md) (2026)
- [13 Puzzle re-tests](stories/13-puzzle-retests.md) (2026)

**Statistics and experiment analysis**
- [05 Where is the effect? Segment significance, coinciding p-values and smaller slips](stories/05-where-is-the-effect.md)
- [08 A confirmation that does not discriminate](stories/08-confirmation-that-does-not-discriminate.md)
- [11 Many errors in one estimate](stories/11-notification-estimate.md)
- [14 Synthetic data-analysis tasks](stories/14-synthetic-analysis-tasks.md)

**Perception and visual checks**
- [07 Drawing a route on a map](stories/07-route-on-a-map.md)
- [09 Slides for two talks](stories/09-slides.md)

**Context and communication in agentic work**
- [06 Missing context](stories/06-missing-context.md)
- [11 Many errors in one estimate](stories/11-notification-estimate.md)
- [12 Who knows what](stories/12-who-knows-what.md)

**Methodology**
- [How I run blind tests](methodology.md)
- [Reproducible task](tasks/README.md)

## How the October 2026 tests were run

Most of the October 2026 work (sweeps of my Claude Code sessions, test prompts, running and grading the tests) was done by Claude Code agents under my direction, and an adversarial Claude reviewer checked the conclusions. Grading mistakes described here were made by the grading agent and caught by the reviewer.

Model names are those reported by the tools: OpenAI o1, DeepSeek R1, Gemini, ChatGPT (2025); Claude Opus 4.8, Opus 5, Fable 5, Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5 and the Reasoning Space models (2026). For each test the story gives the model, the effort setting, the number of runs and the context. Results with different prompts or contexts are not pooled into rates.

**Context of the runs.** Only two tests ran in a clean context, without my personal Claude Code instructions and memory: round 2 of [story 08](stories/08-confirmation-that-does-not-discriminate.md) and the re-test in [story 11](stories/11-notification-estimate.md). The other October runs loaded my personal instructions, which include strict statistics rules and name my fields; some prompts also told the model where the problem came from, and the runs of one task had in context a tool description close to the planted mechanism. For those runs a pass is an upper bound, while a failure happened despite a favourable context.

## Data and confidentiality

The work cases come from my job as an analyst. They are described without internal data: no table, event or metric names, no ticket numbers, no real metric values. The numbers in work-derived prompts are synthetic. Prompts and generators whose numbers stayed close to real ones are described, not published.
