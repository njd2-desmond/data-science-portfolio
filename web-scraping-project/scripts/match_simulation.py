import pandas as pd
from scipy.stats import poisson
import random
results_23_24 = pd.read_csv('web-scraping-project\data\epl-24-25-results-cleaned.csv').dropna(subset=['Home']) #If no entry for home side, assume game is not in this row
team_ratings = pd.read_csv(r'web-scraping-project\data\team-home-away-ratings.csv') #Read in csv from creating_team_ratings
from scipy import stats
import os

def calculate_xg_values(home_team,away_team,game_ratings):
    home_xg = (game_ratings[game_ratings['Team']==home_team]['xG_x']).iloc[0]
    home_xga = (game_ratings[game_ratings['Team']==home_team]['xGA_x']).iloc[0]
    away_xg = (game_ratings[game_ratings['Team']==away_team]['xG_y']).iloc[0]
    away_xga = (game_ratings[game_ratings['Team']==away_team]['xGA_y']).iloc[0]
    home_goals_pred = (home_xg * away_xga).round(2)
    away_goals_pred = (away_xg * home_xga).round(2)
    return home_goals_pred, away_goals_pred

def simulate_match(home_goals_pred,away_goals_pred, num_sims=10000):
    home_team_goals_sim = poisson.rvs(home_goals_pred,size=num_sims)
    away_team_goals_sim = poisson.rvs(away_goals_pred,size=num_sims)
    print("Simulating",home_team,"vs",away_team,"...")
    return home_team_goals_sim, away_team_goals_sim

def choose_random_sim(home_team_goals_sim,away_team_goals_sim):
    results_df = pd.DataFrame({
        'Team1 Goals': home_team_goals_sim,
        'Team2 Goals': away_team_goals_sim
    })
    results_df['Scoreline'] = results_df['Team1 Goals'].astype(str) + '-' + results_df['Team2 Goals'].astype(str)
    #print(results_df)
    result_count = results_df['Scoreline'].value_counts()
    top_10_scorelines = result_count.head(10).index.tolist()
    print(top_10_scorelines)
    selected_scoreline = random.choice(top_10_scorelines)
    print(selected_scoreline)
    hg, ag = map(int, selected_scoreline.split('-'))
    return hg,ag

num_sims = 10000

for index, row in results_23_24.iterrows():
    if pd.isnull(row['HG']) or pd.isnull(row['AG']):
        home_team = results_23_24.at[index, 'Home']
        away_team = results_23_24.at[index, 'Away']
        game_ratings = team_ratings[team_ratings['Team'].isin([home_team,away_team])]
        home_goals_pred,away_goals_pred = calculate_xg_values(home_team,away_team,game_ratings)
        home_score, away_score = simulate_match(home_goals_pred,away_goals_pred,num_sims)
        hg, ag = random_sim_game = choose_random_sim(home_score,away_score)
        results_23_24.at[index, 'HG'] = (hg)
        results_23_24.at[index, 'AG'] = (ag)

# Print the updated DataFrame to verify
#print(results_23_24)
results_23_24.to_csv(r'web-scraping-project\data\season_simulation.csv',index=False)

df = pd.read_csv('web-scraping-project\data\season_simulation.csv')

team_stats = {}

for index, row in df.iterrows():
    home_team = row['Home']
    away_team = row['Away']
    home_goals = row['HG']
    away_goals = row['AG']
    if home_team not in team_stats:
        team_stats[home_team] = {'Matches Played': 0, 'Wins': 0, 'Draws': 0, 'Losses': 0, 'Goals Scored': 0, 'Goals Against': 0}
    team_stats[home_team]['Matches Played'] += 1
    team_stats[home_team]['Goals Scored'] += home_goals
    team_stats[home_team]['Goals Against'] += away_goals

    if away_team not in team_stats:
        team_stats[away_team] = {'Matches Played': 0, 'Wins': 0, 'Draws': 0, 'Losses': 0, 'Goals Scored': 0, 'Goals Against': 0}
    team_stats[away_team]['Matches Played'] += 1
    team_stats[away_team]['Goals Scored'] += away_goals
    team_stats[away_team]['Goals Against'] += home_goals

    # Determine wins, draws, losses
    if home_goals > away_goals:
        team_stats[home_team]['Wins'] += 1
        team_stats[away_team]['Losses'] += 1
    elif home_goals < away_goals:
        team_stats[home_team]['Losses'] += 1
        team_stats[away_team]['Wins'] += 1
    else:
        team_stats[home_team]['Draws'] += 1
        team_stats[away_team]['Draws'] += 1

summary_df = pd.DataFrame.from_dict(team_stats, orient='index')

# Reset the index to have 'Team' as a column instead of the index
summary_df.reset_index(inplace=True)
summary_df.rename(columns={'index': 'Team'}, inplace=True)

# Calculate Points
summary_df['Goal Difference'] = (summary_df['Goals Scored']) - (summary_df['Goals Against'])
summary_df['Points'] = (summary_df['Wins'] * 3) + summary_df['Draws']
# Sort the DataFrame first by Points, then by Goals Scored
summary_df.sort_values(by=['Points', 'Goal Difference'], ascending=False, inplace=True)

# Print the summary table
print("1.",summary_df.iloc[0,0],summary_df.iloc[0,8])
print("######################")
print("2.",summary_df.iloc[1,0],summary_df.iloc[1,8])
print("3.",summary_df.iloc[2,0],summary_df.iloc[2,8])
print("4.",summary_df.iloc[3,0],summary_df.iloc[3,8])
print("5.",summary_df.iloc[4,0],summary_df.iloc[4,8])
print("6.",summary_df.iloc[5,0],summary_df.iloc[5,8])
print("7.",summary_df.iloc[6,0],summary_df.iloc[6,8])
print("8.",summary_df.iloc[7,0],summary_df.iloc[7,8])
print("9.",summary_df.iloc[8,0],summary_df.iloc[8,8])
print("10.",summary_df.iloc[9,0],summary_df.iloc[9,8])
print("11.",summary_df.iloc[10,0],summary_df.iloc[10,8])
print("12.",summary_df.iloc[11,0],summary_df.iloc[11,8])
print("13.",summary_df.iloc[12,0],summary_df.iloc[12,8])
print("14.",summary_df.iloc[13,0],summary_df.iloc[13,8])
print("15.",summary_df.iloc[14,0],summary_df.iloc[14,8])
print("16.",summary_df.iloc[15,0],summary_df.iloc[15,8])
print("17.",summary_df.iloc[16,0],summary_df.iloc[16,8])
print("18.",summary_df.iloc[17,0],summary_df.iloc[17,8])
print("19.",summary_df.iloc[18,0],summary_df.iloc[18,8])
print("20.",summary_df.iloc[19,0],summary_df.iloc[19,8])

summary_df.to_csv(r'web-scraping-project\data\season_simulation_table.csv',index=False)
os.startfile(r'web-scraping-project\data\season_simulation_table.csv')
os.startfile(r'web-scraping-project\data\season_simulation.csv')