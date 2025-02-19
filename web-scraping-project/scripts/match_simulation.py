import pandas as pd
from scipy.stats import poisson
import random
results_23_24 = pd.read_csv(r'web-scraping-project\data\epl-24-25-results-cleaned.csv').dropna(subset=['Home']) #If no entry for home side, assume game is not in this row
team_ratings = pd.read_csv(r'web-scraping-project\data\team-home-away-ratings.csv') #Read in csv from creating_team_ratings

def calculate_xg_values(home_team,away_team,game_ratings):
    home_xg = (game_ratings[game_ratings['Team']==home_team]['HxG']).iloc[0]
    home_xga = (game_ratings[game_ratings['Team']==home_team]['HxGA']).iloc[0]
    away_xg = (game_ratings[game_ratings['Team']==away_team]['AxG']).iloc[0]
    away_xga = (game_ratings[game_ratings['Team']==away_team]['AxGA']).iloc[0]
    home_goals_pred = (home_xg * away_xga).round(2)
    away_goals_pred = (away_xg * home_xga).round(2)
    home_goals_pred = ((home_xg + away_xga)/2).round(2)
    away_goals_pred = ((away_xg + home_xga)/2).round(2)
    return home_goals_pred, away_goals_pred

def simulate_match(home_goals_pred,away_goals_pred, num_sims=10000):
    home_team_goals_sim = poisson.rvs(home_goals_pred,size=num_sims)
    away_team_goals_sim = poisson.rvs(away_goals_pred,size=num_sims)
    print("Simulating",home_team,"vs",away_team,"...")
    print(home_goals_pred,"-",away_goals_pred)
    return home_team_goals_sim, away_team_goals_sim

def choose_random_sim(home_team_goals_sim,away_team_goals_sim):
    results_df = pd.DataFrame({
        'Team1 Goals': home_team_goals_sim,
        'Team2 Goals': away_team_goals_sim
    })
    results_df['Scoreline'] = results_df['Team1 Goals'].astype(str) + '-' + results_df['Team2 Goals'].astype(str)
    result_count = results_df['Scoreline'].value_counts()
    top_10_scorelines = result_count.head(7).index.tolist()
    print("Top 3 Scorelines:",top_10_scorelines)
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
summary_df = summary_df.reset_index(drop=True)  # Reset index
summary_df.insert(0,'Position',summary_df.index + 1)
print(summary_df)

summary_df.to_csv(r'web-scraping-project\data\season_simulation_table.csv',index=False)
#os.startfile(r'web-scraping-project\data\season_simulation_table.csv')
#os.startfile(r'web-scraping-project\data\season_simulation.csv')