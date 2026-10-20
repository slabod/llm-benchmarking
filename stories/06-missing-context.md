# 06. Missing context

**When:** July–September 2026.
**Topic:** context in agentic work.
**Models:** Claude Opus 4.8 and Opus 5.

The failures I correct most often are about context that an analyst with a few years in the team has and the agent lacks:

- it takes a number from the wrong one of two disagreeing sources and labels it "verified";
- it infers a log field's meaning from its name;
- it replaces the requested metric with a proxy of its own.

In each case the right answer is a check against the code or a question to the team, not a confident guess.

## Case 1. Two sources disagree; the wrong one is "verified"

**What happened** (Claude Opus 5, September 2026). Two sources disagreed about an experiment's traffic share: the request form showed a constant value, while my own dated status note in the ticket said the share had been raised several-fold in the middle of the period. The agent had read the note, took the structured field anyway and wrote that the share was "verified in the change history". The change history did contain entries on the ramp dates; they just did not show the values. The adversarial reviewer caught the error, and the agent conceded it.

**Correct answer.** The summary field of a request does not reflect rollout changes, and a dated status note from the experiment's owner outranks it. The true schedule is in each sample's configuration history; sample size and power must use the piecewise schedule. Never write "verified" about a source that cannot record the thing being verified.

Self-contained version (it puts both sources side by side and so gives the answer away; the failure reproduces only as an agentic task):

> An A/B experiment's request form shows "traffic: 10%". Its change log has entries on day 9 and day 16 of a 30-day run that don't display values. A status comment from the experiment owner, dated day 9, says "raised to 30% today". At what traffic share did the experiment run over the 30 days, and how would you confirm it?

## Case 2. Meanings inferred from names

1. **Event prefixes** (Opus 5, July 2026). In data documentation the agent wrote that an old event prefix belongs to one app and the new prefix to the other. I asked whether it had made this up. The data showed both names in both apps, split strictly by client version: older builds keep the old name. The prefix encodes the client version, not the app.
2. **Table fields documented from their names** (Opus 5, September 2026). Asked where the field meanings came from, the agent said that part of them were "derived from the names, not verified". The official description later corrected one field. I already had a "fill in only what you are at least 90–95% sure of, otherwise leave it blank" rule in another project; the agent repeated the failure in a new place.
3. **A trigger read as the warning itself** (Opus 4.8, July 2026). The agent analysed an event as if it measured a warning that users hear and drew product recommendations from it. The adversarial reviewer questioned this, and the event's owner explained that the event marks the trigger, not the warning that users actually hear.

## Case 3. A self-invented proxy

**What happened** (Opus 5, September 2026). I asked for the potential gain in a specific platform metric. The agent substituted its own proxy, built from a different table that happens to have similarly named flags, and mentioned this only as a caveat. I had to ask what the table was and why it was used, and then name the right source.

**Correct answer.** Find the metric's definition in the experimentation platform's code and use that source and unit. If a proxy is unavoidable, say so in the headline, not in a footnote.

## What would help

These are failures of missing knowledge rather than of reasoning, so much of this can probably be solved by a well-built knowledge base for agents:

- table schemas with the meaning of each field;
- one declared source of truth for each number;
- worked query examples.

I maintain one for our team's data, so that the agent looks answers up instead of guessing.
