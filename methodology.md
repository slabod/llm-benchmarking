# How I run blind tests

Rules learned the hard way in October 2026, mostly from mistakes in my own test pipeline: Claude Code agents wrote the prompts, ran and graded the tests, and an adversarial reviewer found the errors.

1. **Write the grading rule before any run, and never apply a stricter unwritten rule afterwards.** The grading agent's first verdict on the notification question was 0 of 15; under the rule actually written down, 9 to 13 of 15 pass. The 0 of 15 was withdrawn ([story 11](stories/11-notification-estimate.md)).
2. **Use a clean context.** Agents that load my personal instructions get my strict statistics rules for free, which inflates pass rates. Workflow and general-purpose agents in Claude Code load those instructions and the list of my tools, and a workflow can relay the triggering message (with the source of the problem) to the solvers. Only two of my October tests met this rule; every story states the context of its runs.
3. **Do not lead in the prompt.** No "3/4 is expected", and no hypothesis phrased so cautiously that "confirmed" becomes literally true. The first round of the reinstall test broke both rules and is reported separately ([story 08](stories/08-confirmation-that-does-not-discriminate.md)).
4. **Report the model, the effort or thinking setting and n.** Sonnet at default effort often answers without thinking, which is a confound when it is compared with models that think. Never pool rounds with different prompts or contexts into a rate. With n = 2 a result shows that a failure reproduces, not its rate.
5. **Review every conclusion adversarially.** A second model (Claude Opus at effort xhigh, prompted to refute rather than to edit) reviews each conclusion, and the key claims are checked against the transcripts. The reviewer caught the over-strict grading, the leading prompt and the contaminated contexts described above.
6. **In mathematics, correctness means a proof.** A brute-force check is only an extra safeguard after the proof, never the justification.

## The quiz version and the agentic version

In most work cases the model would likely answer the quiz version correctly: asked "does significant versus not significant imply a difference?", any frontier model says no. It commits the same error unprompted, while writing a summary, a slide or a ticket comment inside a long agentic task, and sometimes defends it when asked an open question ("why do you think so?"). So the strongest tests are open-ended task prompts ("here are the results; write the conclusion"), and the correct answer often lies in what the model must not claim. Even so, some judgment errors reproduce in short open-ended prompts ([story 05](stories/05-where-is-the-effect.md), [story 08](stories/08-confirmation-that-does-not-discriminate.md)).
