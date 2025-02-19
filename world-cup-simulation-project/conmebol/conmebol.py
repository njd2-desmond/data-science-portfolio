import pandas as pd
from scipy.stats import poisson
import random
#pd.options.display.max_columns = 100
ratings  = pd.read_csv("world-cup-simulation-project\conmebol\conmebol-home-away-ratings.csv")
calendar = pd.read_csv("world-cup-simulation-project\conmebol\conmebol-qual-calendar.csv")

def calculate_xg_values(home_team,away_team,game_ratings):
    home_xg = (game_ratings[game_ratings['Team']==home_team]['HG']).iloc[0]
    home_xga = (game_ratings[game_ratings['Team']==home_team]['HGA']).iloc[0]
    away_xg = (game_ratings[game_ratings['Team']==away_team]['AG']).iloc[0]
    away_xga = (game_ratings[game_ratings['Team']==away_team]['AGA']).iloc[0]
    #print(home_xg, home_xga, away_xg, away_xga)
    home_goals_pred = (home_xg * away_xga).round(2)
    away_goals_pred = (away_xg * home_xga).round(2)
    #print(home_goals_pred,away_goals_pred)
    return home_goals_pred, away_goals_pred

def simulate_match(home_goals_pred,away_goals_pred, num_sims=10000):
    home_team_goals_sim = poisson.rvs(home_goals_pred,size=num_sims)
    away_team_goals_sim = poisson.rvs(away_goals_pred,size=num_sims)
    #print("Simulating",home_team,"vs",away_team,"...")
    return home_team_goals_sim, away_team_goals_sim

def choose_random_sim(home_team_goals_sim,away_team_goals_sim):
    results_df = pd.DataFrame({
        'Team1 Goals': home_team_goals_sim,
        'Team2 Goals': away_team_goals_sim
    })
    results_df['Scoreline'] = results_df['Team1 Goals'].astype(str) + '-' + results_df['Team2 Goals'].astype(str)
    result_count = results_df['Scoreline'].value_counts()
    top_10_scorelines = result_count.head(5).index.tolist()
    #print("Top 5 Scorelines:",top_10_scorelines)
    selected_scoreline = random.choice(top_10_scorelines)
    #print(selected_scoreline)
    hg, ag = map(int, selected_scoreline.split('-'))
    return hg,ag


#must import calendar and team ratings
for index, row in calendar.iterrows():
    if pd.isnull(row['HG']) or pd.isnull(row['AG']):
        home_team = calendar.at[index, 'Home']
        away_team = calendar.at[index, 'Away']
        game_ratings = ratings[ratings['Team'].isin([home_team,away_team])]
        #print(game_ratings)
        home_goals_pred,away_goals_pred = calculate_xg_values(home_team,away_team,game_ratings)
        #print(home_goals_pred,away_goals_pred)
        home_score, away_score = simulate_match(home_goals_pred,away_goals_pred,1000)
        hg, ag = random_sim_game = choose_random_sim(home_score,away_score)
        calendar.at[index, 'HG'] = (hg)
        calendar.at[index, 'AG'] = (ag)

calendar.to_csv(r'world-cup-simulation-project\conmebol\conmebol_last_sim.csv',index=False)

df = pd.read_csv('world-cup-simulation-project\conmebol\conmebol_last_sim.csv')

team_stats = {}

for index, row in df.iterrows():
    home_team = row['Home']
    away_team = row['Away']
    home_goals = row['HG']
    away_goals = row['AG']
    if home_team not in team_stats:
        team_stats[home_team] = {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'GS': 0, 'GA': 0, 'GD': 0, 'Pts': 0}
    team_stats[home_team]['MP'] += 1
    team_stats[home_team]['GS'] += home_goals
    team_stats[home_team]['GA'] += away_goals

    if away_team not in team_stats:
        team_stats[away_team] = {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'GS': 0, 'GA': 0, 'GD': 0, 'Pts': 0}
    team_stats[away_team]['MP'] += 1
    team_stats[away_team]['GS'] += away_goals
    team_stats[away_team]['GA'] += home_goals

    # Determine wins, draws, losses
    if home_goals > away_goals:
        team_stats[home_team]['W'] += 1
        team_stats[away_team]['L'] += 1
    elif home_goals < away_goals:
        team_stats[home_team]['L'] += 1
        team_stats[away_team]['W'] += 1
    else:
        team_stats[home_team]['D'] += 1
        team_stats[away_team]['D'] += 1

summary_df = pd.DataFrame.from_dict(team_stats, orient='index')
# Reset the index to have 'Team' as a column instead of the index
summary_df.reset_index(inplace=True)
summary_df.rename(columns={'index': 'Team'}, inplace=True)

import numpy as np
# Calculate Points
summary_df['GD'] = (summary_df['GS']) - (summary_df['GA'])
summary_df['Pts'] = (summary_df['W'] * 3) + summary_df['D']
summary_df['Pts'] = np.where(summary_df['Team'] == 'Ecuador', summary_df['Pts']-3, summary_df['Pts'])
# Sort the DataFrame first by Points, then by Goals Scored
summary_df.sort_values(by=['Pts', 'GD'], ascending=False, inplace=True)
summary_df = summary_df.reset_index(drop=True)  # Reset index
summary_df.insert(0,'Position',summary_df.index + 1)
print("Final Table:\n",summary_df)

qualifiers = [summary_df['Team'].iloc[0],
              summary_df['Team'].iloc[1],
              summary_df['Team'].iloc[2],
              summary_df['Team'].iloc[3],
              summary_df['Team'].iloc[4],
              summary_df['Team'].iloc[5]]
playoff_team = summary_df['Team'].iloc[6]


print("Qualifying Teams:",qualifiers)
print("To Intercontinental Playoff:",playoff_team)
#must return a list of 6 teams (qualifiers) and 1 playoff team