We ran an A/B test of a new checkout screen in our mobile app. Users were randomized 50/50 into control and test by a hash of user_id.

The data are in `experiment_users.csv`: one row per user in the experiment, with columns user_id, group (control/test), platform, app_version, sessions, converted (1 if the user placed an order during the test).

Did the new checkout screen increase order conversion? Write the conclusion for the product manager: the estimated effect with a p-value or confidence interval, and a recommendation (ship or don't ship).
