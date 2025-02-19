import pandas as pd
from scipy.stats import poisson
import random
qual_calendar = pd.read_csv(r"world-cup-simulation-project\cleaned-results\uefa-qual-results-cleaned.csv")
calendar = pd.read_csv(r"world-cup-simulation-project/uefa/uefa-qual-calendar.csv")
def results_to_ratings(results_file):
    
    #Home Record
    home_goals_for = results_file.groupby("Home")["HG"].mean().reset_index()
    home_goals_for.columns = ['Team', 'HG']
    home_goals_aga = results_file.groupby("Home")["AG"].mean().reset_index()
    home_goals_aga.columns = ['Team', 'HGA']
    home_gf_ga = pd.merge(home_goals_for,home_goals_aga, on='Team', how='outer')

    #Away Record
    away_goals_for = results_file.groupby("Away")["AG"].mean().reset_index()
    away_goals_for.columns = ['Team', 'AG']
    away_goals_aga = results_file.groupby("Away")["HG"].mean().reset_index()
    away_goals_aga.columns = ['Team', 'AGA']
    away_gf_ga = pd.merge(away_goals_for,away_goals_aga, on='Team', how='outer')

    team_ratings = pd.merge(home_gf_ga,away_gf_ga,on='Team',how='outer')

    team_ratings["HG"] = round(team_ratings['HG'], 2)
    team_ratings["HGA"] = round(team_ratings['HGA'], 2)
    team_ratings["AG"] = round(team_ratings['AG'], 2)
    team_ratings["AGA"] = round(team_ratings['AGA'], 2)
    #team_ratings["GF"] = round((team_ratings['HG'] + team_ratings['AG']) / 2, 2)
    #team_ratings["GA"] = round((team_ratings['HGA'] + team_ratings['AGA']) / 2, 2)
    return team_ratings

def calculate_xg_values(home_team,away_team,game_ratings):
    home_xg = (game_ratings[game_ratings['Team']==home_team]['HG']).iloc[0]
    home_xga = (game_ratings[game_ratings['Team']==home_team]['HGA']).iloc[0]
    away_xg = (game_ratings[game_ratings['Team']==away_team]['AG']).iloc[0]
    away_xga = (game_ratings[game_ratings['Team']==away_team]['AGA']).iloc[0]
    home_goals_pred = ((home_xg * away_xga)/2).round(2)
    away_goals_pred = ((away_xg * home_xga)/2).round(2)
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
    result_count = results_df['Scoreline'].value_counts()
    top_10_scorelines = result_count.head(5).index.tolist()
    coin = random.randint(0,4)
    #print("Top 5 Scorelines:",top_10_scorelines)
    selected_scoreline = top_10_scorelines[coin]
    print(selected_scoreline)
    hg, ag = map(int, selected_scoreline.split('-'))
    return hg,ag

team_ratings = results_to_ratings(qual_calendar)

print(team_ratings)

for index, row in calendar.iterrows():
    if pd.isnull(row['HG']) or pd.isnull(row['AG']):
        home_team = calendar.at[index, 'Home']
        away_team = calendar.at[index, 'Away']
        game_ratings = team_ratings[team_ratings['Team'].isin([home_team,away_team])]
        home_goals_pred,away_goals_pred = calculate_xg_values(home_team,away_team,game_ratings)
        home_score, away_score = simulate_match(home_goals_pred,away_goals_pred,10000)
        hg, ag = random_sim_game = choose_random_sim(home_score,away_score)
        calendar.at[index, 'HG'] = (hg)
        calendar.at[index, 'AG'] = (ag)

team_stats = {}
for index, row in calendar.iterrows():
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

#Top8
print("ROUND OF 16 -------")
print(summary_df['Team'][16],"/",summary_df['Team'][14],"vs",summary_df['Team'][0])
print(summary_df['Team'][22],"/",summary_df['Team'][8],"vs",summary_df['Team'][1])
print(summary_df['Team'][20],"/",summary_df['Team'][10],"vs",summary_df['Team'][2])
print(summary_df['Team'][18],"/",summary_df['Team'][12],"vs",summary_df['Team'][3])
print(summary_df['Team'][19],"/",summary_df['Team'][13],"vs",summary_df['Team'][4])
print(summary_df['Team'][21],"/",summary_df['Team'][11],"vs",summary_df['Team'][5])
print(summary_df['Team'][23],"/",summary_df['Team'][9],"vs",summary_df['Team'][6])
print(summary_df['Team'][17],"/",summary_df['Team'][15],"vs",summary_df['Team'][7])
print("QUARTER FINALS ----")
print(summary_df['Team'][16],"/",summary_df['Team'][14],"/",summary_df['Team'][0],"vs",
      summary_df['Team'][22],"/",summary_df['Team'][8],"/",summary_df['Team'][1])
print(summary_df['Team'][20],"/",summary_df['Team'][10],"/",summary_df['Team'][2],"vs",
      summary_df['Team'][18],"/",summary_df['Team'][12],"/",summary_df['Team'][3])
print(summary_df['Team'][19],"/",summary_df['Team'][13],"/",summary_df['Team'][4],"vs",
      summary_df['Team'][21],"/",summary_df['Team'][11],"/",summary_df['Team'][5])
print(summary_df['Team'][23],"/",summary_df['Team'][9],"/",summary_df['Team'][6],"vs",
      summary_df['Team'][17],"/",summary_df['Team'][15],"/",summary_df['Team'][7])