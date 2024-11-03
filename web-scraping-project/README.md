#project-2

This is a data scraping project, where I scrape this years results/fixtures from the Premier League and use them to simulate the rest of the season.

Teams Goals-per-Game and Goals-Conceded-per-Game are calculated for both Home and Away games, and results of matches are simulated using a Poisson Distribution.

A random choice is taken from the 10 most likely results so to account for the random nature of Football without simulating outrageous scorelines, like 10-8.

HOW TO RUN:
    1. Run scraping_results.py - this will scrape the fixtures and results from the internet and turn them into a Dataframe.
    2. Run creating_team_ratings.py - this will create a table showing how many goals teams score/concede both home and away.
    3. Run match_simulation.py - this will simulate the remaining games in the season using Poisson ditribution and output 2 csv files: the simulated fixtures and the final table.