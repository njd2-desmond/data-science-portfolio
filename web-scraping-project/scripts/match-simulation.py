import pandas as pd
from scipy.stats import poisson
import random

team_ratings = pd.read_csv(r'web-scraping-project\data\team-home-away-ratings.csv')
home_team = "Brighton"
away_team = "Wolves"
game_ratings = team_ratings[team_ratings['Team'].isin([home_team,away_team])]

home_xg = (game_ratings[game_ratings['Team']==home_team]['xG_x']).iloc[0]
home_xga = (game_ratings[game_ratings['Team']==home_team]['xGA_x']).iloc[0]
away_xg = (game_ratings[game_ratings['Team']==away_team]['xG_y']).iloc[0]
away_xga = (game_ratings[game_ratings['Team']==away_team]['xGA_y']).iloc[0]

home_goals_pred = (home_xg * away_xga).round(2)
away_goals_pred = (away_xg * home_xga).round(2)

print(home_goals_pred,away_goals_pred)

def simulate_match(home_goals_pred,away_goals_pred, num_sims=10000):
    home_team_goals_sim = poisson.rvs(home_goals_pred,size=num_sims)
    away_team_goals_sim = poisson.rvs(away_goals_pred,size=num_sims)
    return home_team_goals_sim, away_team_goals_sim

def choose_random_sim(home_team_goals_sim,away_team_goals_sim):
    results_df = pd.DataFrame({
        'Team1 Goals': home_team_goals_sim,
        'Team2 Goals': away_team_goals_sim
    })
    print(results_df.value_counts()[:10])
    random_sim_num = random.randint(0,num_sims)
    random_sim_game = results_df.iloc[random_sim_num]
    return random_sim_game

num_sims = 10000
home_team_goals_sim, away_team_goals_sim = simulate_match(home_goals_pred,away_goals_pred,num_sims)

random_sim_game = choose_random_sim(home_team_goals_sim,away_team_goals_sim)
print(home_team,random_sim_game.iloc[0],away_team,random_sim_game.iloc[1])
