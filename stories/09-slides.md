# 09. Slides for two talks

**When:** September 2026.
**Topic:** perception, visual verification.
**Models:** Claude Opus 5 and Fable 5.1 in Claude Code; adversarial reviewer on Fable 5.1.

**Setting.** I made the slides for two one-hour talks at work, on shortest-path algorithms and on mathematical statistics, with Claude Code. The agent built the slides (python-pptx, matplotlib/LaTeX figures, a Beamer version), rendered them in PowerPoint, and checked them itself.

**What went wrong.** I pointed out almost 90 visual defects, from shifted and overlapping text to broken pictures and wrong fonts. In about 20 cases the agent had reported the slides as checked just before. Examples of such reports: "verified by render", "automatic checks are clean, 0 remarks", "checked by measurement, aligned to the pixel".

Most frequent defect types: misalignment and centring (one talk alone had 17 complaints about centring before the cause was found: an inherited text indent in the template), colours and contrast, broken or wrong pictures, text overflow, overlaps, formulas typeset in the body font instead of LaTeX.

**How the checking failed:**

- it reviewed contact sheets of 12 slides at a time, where overflow, low contrast and small labels are invisible;
- it trusted home-made checkers that measured boxes in the file, not what was drawn in them, and the file geometry often disagreed with how PowerPoint actually laid out the text;
- after a fix it re-rendered only the slides being edited, so regressions elsewhere went unseen;
- once it defended its own measurement against my screenshot instead of treating the screenshot as evidence;
- the reviewer saw only what it was given: the PowerPoint version, not the Beamer one (see [story 12](12-who-knows-what.md)).

**Correct answer:** look at every slide at full size, in the program the audience will see, after every change.

**Open idea.** A reproducible test: rendered slides with planted overflow and overlap defects, graded by how many the model finds and how many it reports as fine.
