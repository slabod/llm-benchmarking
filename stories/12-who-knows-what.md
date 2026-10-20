# 12. Who knows what

**When:** cases from July–October 2026; review of my sessions in October 2026.
**Topic:** context and communication in agentic work.
**Models:** Claude Opus 4.8, Opus 5, Opus 5.5, Fable 5, Fable 5.1.

This is a limitation of the current paradigm rather than a single question, the mirror image of [missing context](06-missing-context.md). The agent writes as if the reader knew everything the agent knows. It treats each fact as simply known or unknown, without asking who knows it: a fact the agent learned an hour ago may be completely unknown to the reader.

So its ticket comments, instructions, code comments and prompts to other agents lean on words it coined, files it opened, iterations it went through and its own machine, none of which the reader has. A good text works for someone who has only the text.

The idea came from a friend's remark that language models track facts as "known or unknown", not as "known to X but not to Y". Claude subagents then reviewed my Claude Code sessions for cases where I had to ask what a text meant or order it rewritten.

**What the review found.** In texts for people there were 13 cases, 6 of them clean: words the agent coined for its own intermediate results, private shorthand, instructions that worked only on the agent's machine, traces of its own review rounds left in finished texts, and a headline that used a word in a sense only the agent had in mind. In prompts to other agents the thesis held only partly: about 30 prompts were read in full and about 100 scanned, and one clean case turned up, the reviewer of a deck that was not given the version I had asked for (see [story 09](09-slides.md)).

A glossary helps only with the "team term or invented term" subset. For the rest the missing piece is a check of each text against what this particular reader knows.

**Open idea.** A test in which the agent writes a prompt or a README for a reader with a stated, limited context, graded by what that reader cannot resolve.
