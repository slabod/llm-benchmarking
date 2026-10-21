# 04. Reasoning Space and the Hamiltonian-path problem

**When:** May 2026.
**Topic:** mathematics, olympiad benchmark.
**Models:** 10 models, including Claude Fable 5, Claude Opus 5, GPT-5.6 Sol, Gemini 3.1 Pro, DeepSeek V4 Pro, Kimi K3.

## The benchmark

[Reasoning Space](https://reasoning.csspace.io/) ([announcement](https://t.me/csspace/322)) grades models on olympiad problems before they are published, so the problems should not be in the training data. Rules from the site and the announcement:

- every model gets the same statement and the same system prompt;
- text only: no search, tools, code execution or calculator;
- one run per problem and model, maximum reasoning mode where the API allows, a budget of up to 256,000 output tokens;
- organizers and independent experts grade the solutions by the original olympiad criteria;
- the site publishes scores, full solution texts, token counts and the cost of each run.

The first competition was Math Cup 2026: 10 models solved the qualifier and final problems.

## The Hamiltonian-path problem (Math Cup 2026 final, a competition I organized)

The problem was proposed by D. G. Sagunov.

> A simple graph $`G`$ on $`n`$ vertices has a Hamiltonian path. Find (a) a simple path of length $`\Omega(\log n)`$ in polynomial time; (b) a simple path of length $`\omega(\log n)`$ in expected polynomial time. The length of a path is its number of edges.

Original statement (in Russian), the official solution and all model solutions: [Reasoning Space, Math Cup 2026 final, problem 6](https://reasoning.csspace.io/problems/math-cup-2026-final/task6).

What the models did:

- none of 10 models solved (b);
- six models (Claude Fable 5, Claude Opus 5, GPT-5.6 Sol, Gemini 3.1 Pro, DeepSeek V4 Pro, Kimi K3) solved only (a);
- for (b), four of them, including Fable 5, replaced the proof with a literature citation;
- Gemini 3.1 Pro cited a paper that does not contain the claimed statement.

**Correct answer:**

- (a) the DFS tree of a graph with a Hamiltonian path has depth at least $`\log_2 n`$, so its deepest root-to-leaf path works;
- (b) color coding finds, in expected polynomial time, a cycle of length at least $`\log n`$ through a given vertex if one exists; a recursion over three cases (a cut vertex, such a cycle exists, no such cycle exists) glues the pieces into a path of length $`\Omega(\log^2 n / \log\log n) = \omega(\log n)`$.

**Background.** The problem is a special case of a known line of results, summarised in the related-work section of [Fomin, Golovach, Sagunov, Simonov, "Approximating Long Cycle Above Dirac's Guarantee"](https://arxiv.org/abs/2305.02011) (page 2). If a graph has a simple path of length $`L`$, a polynomial-time algorithm can find, in chronological order of the results:

- a path of length $`\Omega(\log L / \log\log L)`$, from the parameterized algorithms of Monien and of Bodlaender;
- a path of length $`\Omega(\log L)`$, by color coding (Alon, Yuster and Zwick);
- a path of length $`\Omega((\log L / \log\log L)^2)`$ (Björklund and Husfeldt);
- a cycle of length $`2^{\Omega(\sqrt{\log L / \log\log L})}`$ in a graph with a cycle of length $`L`$ (Gabow);
- a cycle of length $`2^{\Omega(\sqrt{\log L})}`$ (Gabow and Nie), the best known bound as far as the problem's author knows.

Whether a path of length $`L^{\varepsilon}`$ for some fixed $`\varepsilon > 0`$ can be found in polynomial time is an open question in theoretical computer science: $`2^{\Omega(\sqrt{\log L})}`$ beats every power of $`\log L`$ but not $`L^{\varepsilon}`$, and the gap to the known hardness results is still large.

So part (a) is the color-coding level, and part (b) asks to go beyond it in the special case $`L = n - 1`$.

## Overall result

Two of the 17 Math Cup 2026 problems were not fully solved by any model: the Hamiltonian-path problem above and "Find a common language" from the qualifier. Per-problem results were read from the Reasoning Space site in October 2026.

## "Find a common language" (Math Cup 2026 qualifier)

> Two context-free grammars over the alphabet $`\{a, b\}`$ are given. Grammar $`G_1`$ with start symbol $`S`$: $`S \to \varepsilon \mid aS \mid aSbSaSaS \mid aSaSbSaS`$. Grammar $`G_2`$ with start symbol $`T`$: $`T \to \varepsilon \mid aTa \mid bTbTbTbTb`$. Find the number of words of length 95 in $`L(G_1) \cap L(G_2)`$.

Translated from Russian. Original statement, the official solution and all model solutions: [Reasoning Space, Math Cup 2026 qualifier, problem 8](https://reasoning.csspace.io/problems/math-cup-2026-qualifying/task8).

**Answer:** 71 024 813 194. The official solution first shows that a non-empty word is in $`L(G_1)`$ exactly when it starts and ends with $`a`$, has no factor $`bb`$ and satisfies $`|w|_a \ge 3|w|_b`$. Then $`|w|_b \in \{5, 15\}`$; the case of 5 letters $`b`$ gives $`\binom{44}{4} = 135\,751`$ words, and the case of 15 gives 71 024 677 443, counted by inclusion–exclusion over generating functions.

**Result:** the best score was 3 of 4, by Claude Fable 5 and Opus 5; no model got full marks.

**Conclusion:** at the research end of olympiad mathematics the typical failure in May 2026 was not a wrong computation but a missing proof: models cited a theorem instead of proving it, and sometimes cited a paper that does not contain it. These are the models of May 2026; the problems have not been re-run on Opus 5.5 or Fable 5.1.
