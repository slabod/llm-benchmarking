# 07. Drawing a route on a map

**When:** July 2026.
**Topic:** perception, everyday life.
**Model:** Claude Fable 5 (mobile app).

I remembered this as August; the dates of the festival point to July, and Fable 5 is the model that was current then.

**Setting.** I was in a park and wanted to get to the open-air stage of a jazz festival. I asked Claude Fable 5 on my phone to draw me the way: to mark with arrows where to go, on a screenshot of the map or on a drawing of it.

**What it did.** It produced a primitive illustration of four or five geometric shapes, and the route drawn on it was wrong.

**Correct answer.** The same map with arrows along the actual paths from where I stood to the stage. A person does this with a pen in a minute; the drawing lost the map's layout entirely.

**Context.** A similar weakness shows up in benchmarks: on spatial tasks given as pictures (cube nets, tangrams) the models evaluated in STARE ([arXiv 2506.04633](https://arxiv.org/abs/2506.04633), models of 2025) stay close to chance. Text versions of geometric riddles, by contrast, are solved (see [story 13](13-puzzle-retests.md)). I have not re-tested the map task on current models.

**Open idea.** A reproducible version: a fixed map screenshot, a start and a target, and a grading rule that checks whether the drawn arrows follow existing paths.
