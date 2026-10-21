# Reproducible task

The synthetic A/B task from [story 14](../stories/14-synthetic-analysis-tasks.md). To get the data, run `cd ab-srm && python3 generate.py` (needs numpy and pandas); then give the model only [prompt.md](ab-srm/prompt.md) and the generated `experiment_users.csv` in an empty folder, and check its conclusion against [answer_key.md](ab-srm/answer_key.md).
