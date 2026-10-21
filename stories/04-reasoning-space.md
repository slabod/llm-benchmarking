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

## The problem I co-authored (Math Cup 2026 final)

> A simple graph G on n vertices has a Hamiltonian path. Find (a) a simple path of length Ω(log n) in polynomial time; (b) a simple path of length ω(log n) in expected polynomial time.

What the models did:

- none of 10 models solved (b);
- six models (Claude Fable 5, Claude Opus 5, GPT-5.6 Sol, Gemini 3.1 Pro, DeepSeek V4 Pro, Kimi K3) solved only (a);
- for (b), four of them, including Fable 5, replaced the proof with a literature citation;
- Gemini 3.1 Pro cited a paper that does not contain the claimed statement.

**Correct answer:**

- (a) the DFS tree of a graph with a Hamiltonian path has depth at least log₂ n, so its deepest root-to-leaf path works;
- (b) color coding finds, in expected polynomial time, a cycle of length at least log n through a given vertex if one exists; a recursion over three cases (a cut vertex, such a cycle exists, no such cycle exists) glues the pieces into a path of length Ω(log² n / log log n) = ω(log n).

## Overall result

Two of the 17 Math Cup 2026 problems were not fully solved by any model: this one and "Find a common language" from the qualifier (count the words of length 95 in the intersection of two context-free languages over {a, b}; the best score was 3 of 4, by Fable 5 and Opus 5). Per-problem results were read from the Reasoning Space site in October 2026.

**Conclusion:** at the research end of olympiad mathematics the typical failure in May 2026 was not a wrong computation but a missing proof: models cited a theorem instead of proving it, and sometimes cited a paper that does not contain it. These are the models of May 2026; the problems have not been re-run on Opus 5.5 or Fable 5.1.
