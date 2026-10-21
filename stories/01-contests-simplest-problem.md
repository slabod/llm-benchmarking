# 01. Contests: the simplest problem a top model cannot solve

**When:** 31 May 2025 and 5 July 2025; re-test in October 2026.
**Topic:** mathematics and puzzles.
**Models:** OpenAI o1 (2025), DeepSeek R1 (2025); Claude Haiku 5.5, Sonnet 5.5, Opus 5.5, Fable 5.1 (re-test, 2026).

## The game

Twice I ran a team game: invent the simplest school olympiad problem with a numeric answer that a top model cannot solve.

1. [Yandex meetup for mathematicians](https://events.yandex.ru/events/ya-math-and-analytics-31-05-2025/index), 31 May 2025, about mathematics in search analytics. The model to break was OpenAI o1.
2. [CS Space meetup "LLM in mathematics and algorithms"](https://csspace.io/meetup/2025summer-LLM), 5 July 2025 ([announcement](https://t.me/csspace/110)). I opened the meetup; the game "A hard problem for an LLM" ran in the practical part. 15 teams played against DeepSeek R1.

Rules of the first game:

- Teams of participants, each with a curator.
- Goal: the simplest school olympiad problem in mathematics that an advanced LLM (OpenAI o1) cannot solve.
- The answer must be a number (no existence problems dressed up with a numeric answer). The statement must be unambiguous; the curator checks this. Only school terminology is allowed: "Euler cycle" is fine, "weak sequential closure" is not.
- The prompt is sent as "Solve the problem: {statement}". 40 minutes for the task; the number of attempts is not limited.
- The jury picks the simplest problem the model failed. Extra criteria: does the model solve it on a second attempt or with a hint, and do other models solve it.

## Winning problems

Both games produced the same families of winners:

- **Arithmetic with repeated digits:** 1+1+1+1+11+1+1+1+1. The answer is 19; o1 answered 20.
- **Irrelevant details:** "Masha had 10 apples, Misha had 7 apples. Masha gave Misha 5 apples. How many apples did Masha have?" The answer, 10, is in the first clause, and the rest is noise; o1 subtracted and answered 5.
- **Geometric riddles** rather than textbook geometry: "Connect the entrance and the exit of the maze in the picture with a line. How long is the line?", moving one matchstick to fix an equation, the most triangles from k matches.
- **Wrapping arithmetic in a socially sensitive frame**, so that the safety behaviour takes over and the model refuses or answers a different question (o1 only).

## Re-test, October 2026

Claude wrote similar problems at my request, and current Claude models answered them without tools (no code execution, no search). Answer key computed by script:

| # | Problem | Answer | Result |
|---|---|---|---|
| 1 | A long sum of 30 terms: 25 ones, three 11s, two 111s | 280 | all correct |
| 2 | Shortest path through an ASCII maze | 28 moves | all correct |
| 3 | Wolf, goat and cabbage, but the boat takes the farmer and all three | 1 crossing | all correct |
| 4 | Monty Fall: the host does not know where the car is and opens a goat door by chance | 1/2 | all correct |
| 5 | Day of the week of 29 February 1900 | no such date | all correct |
| 6 | Matchsticks: 9 + 5 = 9, move one | 3 + 5 = 8 or 3 + 6 = 9 | all correct |
| 7 | Count the letter "e" in a sentence | 16 | all correct |
| 8 | The apples problem above (in Russian, with "было", "had") | 10 | Sonnet 5.5 answered 5; Opus 5.5 and Fable 5.1 answered 10 and noted that 5 remain after the gift |
| 9 | 1+1+1+1+11+1+1+1+1 | 19 | all correct |

Models: Haiku 5.5 (default effort), Sonnet 5.5 (high), Opus 5.5 (low and high), Fable 5.1 (high), one run each. Ten more geometric riddles and five short trap questions are in [story 13](13-puzzle-retests.md).

**Context of the runs:** my personal Claude Code instructions were loaded, and the prompt framed the set as simple questions that frontier agents still get wrong, which primes a model to look for traps. The results are an upper bound.

**Conclusion:** Claude Opus 5.5 and Fable 5.1 now solve these winning problems. Sonnet 5.5 answered 5 to the apples question; the question does not say whether it asks about before or after the gift, so 5 is a defensible reading and this is a weak failure.
