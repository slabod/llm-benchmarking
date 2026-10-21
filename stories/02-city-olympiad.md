# 02. St. Petersburg city olympiad through reasoning models

**When:** 2025; May 2026.
**Topic:** mathematics, olympiad problems.
**Models:** DeepSeek R1, Gemini, ChatGPT in their best reasoning modes of the time (2025); Claude Opus (May 2026).

## 2025: reasoning models still fail school problems

I have been on the organizing team of the [St. Petersburg City Mathematical Olympiad](https://www.pdmi.ras.ru/~olymp/) since 2008. About a year before this write-up I ran problems of the city olympiad through the best reasoning models of the time (DeepSeek R1, Gemini, ChatGPT). They still failed some problems, including ones for grades 6–8.

One of them, from the 2025 grade 10 paper (round II, problem 1; [all 2025 statements](https://www.pdmi.ras.ru/~olymp/2025/problems.html)):

> 39 identical-looking coins lie in a row. Some 10 consecutive coins are counterfeit. All genuine coins weigh the same, all counterfeit coins weigh the same and are lighter than the genuine ones. How can one find 6 counterfeit coins with two weighings on a balance scale?

**Solution.** Any 10 consecutive numbers contain exactly two multiples of 5, and these are consecutive multiples. So the counterfeit block contains coins $`5k`$ and $`5k + 5`$ for some $`k \in \{1, \dots, 6\}`$ and, being an interval, all six coins from $`5k`$ to $`5k + 5`$. It remains to find $`k`$:

- first weighing: coin 10 against coin 30. They are 20 apart, so at most one of them is counterfeit. If coin 10 is lighter, $`k \in \{1, 2\}`$; if coin 30 is lighter, $`k \in \{5, 6\}`$; if they balance, both are genuine and $`k \in \{3, 4\}`$;
- second weighing: 5 against 15 if $`k \in \{1, 2\}`$, 15 against 25 if $`k \in \{3, 4\}`$, 25 against 35 if $`k \in \{5, 6\}`$. Since the block contains exactly two multiples of 5, exactly one of the two coins is counterfeit, and the lighter one gives $`k`$.

The olympiad site publishes statements only. The solution above was found with Claude in October 2026; the argument is complete on its own, and a brute-force check over all 30 positions of the block agrees with it.

## May 2026: Claude Opus solves full papers

In May 2026 Claude Opus solved every problem of the city olympiad for grades 7 and 11. The statements are on the olympiad site by year, for example [2026](https://www.pdmi.ras.ru/~olymp/2026/problems.html).

In October 2026 Claude Fable 5.1 also wrote a different, complete solution of the coins problem: the first weighing compares coins 1–10 with coins 30–39 and locates the block start in a decade, the second splits the decade 3 + 4 + 3, and a lemma shows that any set of possible block starts with spread at most 4 shares at least 6 coins.

**Conclusion:** school olympiad problems moved from "sometimes failed" to "solved" within about a year.
