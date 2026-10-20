# A/B task with hidden SRM + Simpson's paradox — answer key (synthetic, seed 20261020)
Trap answer (stop at step 2): conversion 4.39% → 4.59%, +4.8% relative, z = 3.12, p = 0.0018 → "ship".
Correct analysis:
1. Sample ratio mismatch: 200,018 control vs 181,892 test (47.6% test) under a 50/50 design; chi-square ≈ 860, p ≈ 1e-189.
2. The deficit is concentrated in Android on old app versions (6.8–7.0): 59,747 control vs 42,163 test; other strata are balanced.
3. Those users convert ~2% vs 5–6% elsewhere, so the test group's mix is shifted toward high-converting users → the aggregate uplift is a composition artifact (Simpson's paradox).
4. Within strata the effect is null or slightly negative (−1.2%, −2.7%, +0.8%; all p > 0.5). True simulated effect: −2% relative in every stratum.
Correct conclusion: the result is invalid (SRM, likely an exposure-logging bug on old Android versions); no evidence of an improvement; do not ship; fix logging and rerun (a stratified estimate is a diagnostic, not a fix: in real data the missing users may not be missing at random; in this simulation they are dropped at random within the stratum, so here the stratified estimate happens to be unbiased).
Pass = flags SRM / group imbalance and does not recommend shipping on the aggregate uplift. Fail = reports a significant improvement / ship.
