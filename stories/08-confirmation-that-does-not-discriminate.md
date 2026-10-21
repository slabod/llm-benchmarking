# 08. A confirmation that does not discriminate

**When:** August 2026 (at work); blind re-tests in October 2026.
**Topic:** statistics, experiment analysis.
**Models:** Claude Opus 5 (at work); Sonnet 5.5, Opus 5.5, Fable 5.1 (re-tests).

## The case

**Setting.** In one of our A/B experiments every app install was randomly assigned to one of four equal-sized experiment groups (exp_samples), independently of other installs. Grouped by device, some devices fell into two exp_samples of the same experiment.

My hypothesis was that the device is the wrong unit and that these devices come from reinstalls: a user deletes the app, installs it again, and the new install is randomized again.

**What the agent did** (Claude Opus 5, August 2026). It found that devices with two installs have them in different exp_samples in 75% of cases. Two independent draws from four equal groups differ with probability $`3/4`$, so it reported the hypothesis "confirmed with quantitative precision".

It then built two more claims on this, a monthly reinstall rate and an explanation of a skew in the data; both were wrong. Within the hour, looking at example devices, it found the real cause.

**Correct answer.**

- The check confirms only the first half of the hypothesis: installs are randomized independently, so the device is the wrong unit.
- It cannot show where the extra installs come from: any two independently randomized installs on one device give $`3/4`$ (with $`k`$ installs, the probability of landing in more than one exp_sample is $`1 - 4^{1-k}`$).
- A discriminating check asks whether the two installs are the same app and whether they were active at the same time.

In our case almost all extra installs were a second, different app on the same phone, not reinstalls. The cause matters for the remedy: a parallel install usually predates the experiment, while a reinstall happens after assignment and can be caused by the treatment.

## Blind re-tests (October 2026)

I gave the same check, with no other context, to current models. The prompt uses synthetic numbers close to the real ones, so it is not published.

**Round 1** (rule written after 2 of 6 answers arrived, before reading the others). Pass: the conclusion does not call the hypothesis confirmed, because the rates follow from any mechanism that gives a device several independently randomized installs. Fail: the headline says confirmed, even with a soft caveat.

| Model | Result |
|---|---|
| Sonnet 5.5 | 0 of 2 ("confirmed, with caveats"; one answer claimed that other mechanisms would give a different rate, which is false) |
| Opus 5.5 | 2 of 2 |
| Fable 5.1 | 2 of 2 (one answer led with "the mechanism is confirmed", meaning the randomization, and then said the check cannot tell reinstalls from other causes) |

The opponent review found this round unfair: the prompt handed over the expected value, phrased the hypothesis cautiously, and the runs loaded my personal instructions; Sonnet answered in about 10 s without thinking, the others in about 90 s with thinking. Round 2 fixes the prompt and the context.

**Round 2** (pre-registered before any run; synthetic numbers, no hint at the expected value, the hypothesis states the cause explicitly; clean context without my instructions or memory; no tools; default effort; 5 runs per model). Pass: does not present reinstalls as the confirmed or strongly supported cause, and says that any source of several independently randomized installs gives the same rates. Fail: calls the hypothesis confirmed, or claims that other mechanisms would give different rates.

| Model | Pass | Typical wording |
|---|---|---|
| Opus 5.5 | 5 of 5 | "It does not confirm that reinstalls are the reason" |
| Sonnet 5.5 | 5 of 5 | "not confirmed as the main explanation … would look the same for any source of multiple install ids" |
| Fable 5.1 | 2 of 5 (one borderline) | three answers opened with an unqualified "the hypothesis is confirmed"; two of them noted further down that the check cannot tell a reinstall from other causes, then added that the cause does not matter |

Response times differed: Sonnet 5.5 answered in 10–16 s, probably without thinking at default effort, Opus 5.5 in 39–54 s and Fable 5.1 in 40–65 s. So the comparison between Sonnet and the other two is confounded by thinking; the Fable result is not.

Rounds 1 and 2 are not pooled: the prompt and the context differ. No answer in either round named the actual cause (a second, different app on the same phone) as the leading alternative.

**Open idea.** The real failure was in designing and over-reading its own check, not in judging a check handed over. An agentic version would give install-level data and let the agent design the check itself.
