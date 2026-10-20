# 10. The sorting barrier for Dijkstra

**When:** September 2026.
**Topic:** algorithms.
**Model:** Claude Fable 5.1 in Claude Code; caught by the adversarial reviewer.

**Setting.** For my talk on speed-ups of Dijkstra's algorithm the agent turned a recording of my lecture into slides and was asked to stay close to the lecture. In the lecture I say, informally, that without extra tricks (information about the graph or fast processor operations) there is little hope of beating heap-based Dijkstra, because Dijkstra sorts.

**What the agent did.** It hardened this into "with a heap it is O(m log n); faster is impossible in general, the output order is a sort", and on another slide wrote that without extra assumptions on the weights one cannot beat sorting. Both statements contradict two slides of the same deck, which correctly give O(m + n log n) with Fibonacci heaps and cite Duan et al. (2025) as a way around the barrier. It also invented "Dial's algorithm is thousands of times worse than a heap", which is not in the lecture.

The folk claim partly comes from my own informal wording, and the model knew the correct facts. So the failure is a claim hardened in prose and not reconciled with the deck's own correct material; asked directly, a frontier model would likely answer correctly.

**Question:** Dijkstra's algorithm outputs vertices in sorted order of distance, so sorting reduces to it. Does it follow that single-source shortest paths with non-negative weights cannot be solved faster than O(m log n) or O(n log n) in the comparison-addition model?

**Correct answer:** no.

- The reduction gives Ω(n log n) comparisons only for algorithms that output the vertices in nondecreasing order of distance, and only with enough distinct weights: with k ≤ n distinct values the bound is Ω(n log k).
- Dijkstra itself runs in O(m + n log n) with Fibonacci heaps.
- Duan, Mao, Mao, Shu and Yin (2025) solve directed SSSP with real non-negative weights deterministically in O(m log^{2/3} n) in the comparison-addition model, which beats n log n when m = o(n log^{1/3} n).
- In other models, Thorup (1999) solves undirected SSSP with positive integer weights in O(m) on a word RAM.

**Backup question (Dial).** With integer weights in [1, C], Dial's algorithm runs in O(m + nC). Is that tight, and what instance-dependent bound holds? Tight in the worst case (a path of weight-C edges gives maximum distance D = (n − 1)C); on a given instance the cost is O(m + n + D), because the cyclic bucket pointer only moves forward. The ratio to a heap depends on C and on the instance, so a fixed "thousands of times" has no basis.
