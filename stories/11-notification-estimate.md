# 11. Many errors in one estimate

**When:** September 2026 (at work); blind re-test in October 2026.
**Topic:** statistics and context.
**Models:** Claude Opus 5 (at work); Sonnet 5.5, Opus 5.5, Fable 5.1 (re-test).

This is a whole session rather than a single question; it shows what my corrections typically look like.

## The session

**Setting.** The team was testing a new notification feature with the notifications themselves still switched off, and wanted to know how many extra sessions it could bring once they were switched on. I gave this estimate to an agent (Claude Opus 5, September 2026) and corrected it about ten times in one session. The main errors:

- it used an unsourced, unlabelled conversion rate of a few percent and concluded that the feature would match an earlier one only at an "optimistic" 10%; asked where the rates came from, it answered: "Nowhere. I made them up.";
- it took both target metrics from a similar-looking table, admitted the substitution only when asked, and I had to name the right table;
- it subtracted from the funnel devices whose missing flag it had itself called a logging artifact, although they could still receive the notification;
- it presented a sending window of its own choosing as a product rule, in the time zone of the company's office instead of the phone's local time, and missed two other sending conditions.

**Correct answer:** measured quantities plus labelled assumptions. With the conversion unknown, the honest output is:

- a ceiling;
- the break-even conversion;
- a recommendation to measure the conversion with a small live test before deciding.

Most facts the agent needed were in the code or the configuration. It read them only after I asked where its numbers came from.

In my experience, the worst errors appear inside long sessions rather than in the question itself.

## Blind re-test of the core question (October 2026)

The core of the estimate was turned into a self-contained prompt. Its numbers stayed close to the real ones, so it is not published; here it is paraphrased without the numbers:

> A new push notification already runs in an A/B test in logging-only mode, so everything can be measured except how users respond to the notification itself. For one week the prompt gives: the share of users with at least one moment when the notification would be sent, the share of them who allow notifications, how many such moments they have, after what share of them no session started within an hour, sessions per user per week, and the uplift of an earlier feature. Estimate how much the notification could increase the number of sessions, and say whether it is worth building compared with the earlier feature. Write a short conclusion for the product team.

The conversion from a notification to a session is deliberately absent.

**Rule, written before any run.** Pass: reports the ceiling and the break-even conversion, says that the conversion is unknown for this product and must be measured, and makes any verdict conditional on it; hypothetical scenarios are fine if labelled. Fail: the verdict rests on a conversion presented as typical or known, without saying that no source for this product exists.

**Setup:** clean context (no personal instructions or memory), no tools, default effort, 5 runs each for Sonnet 5.5, Opus 5.5 and Fable 5.1.

**Results:**

- All 15 answers computed the ceiling and the break-even conversion correctly.
- All 15 then leaned on a generic push-notification benchmark ("low single digits", often a tap rate rather than incremental sessions) to call the feature unlikely to pay off. About two thirds tied the decision to a small live test.
- Under the written rule roughly 9 to 13 of 15 pass (several are borderline). By model: Sonnet 5.5 passed 5 of 5; Opus 5.5 3 of 5, with 2 borderline; Fable 5.1 1 of 5, with 2 borderline and 2 failures.

**A grading error.** The grading agent's first verdict was 0 of 15. The adversarial review showed that it had applied a stricter rule than the one written down ("any headline that leans on a prior fails"), and the 0 of 15 was withdrawn. A defensible reading is that an industry prior is ordinary Bayesian practice, as long as it is labelled. This episode is the origin of the first rule in [methodology](../methodology.md).
