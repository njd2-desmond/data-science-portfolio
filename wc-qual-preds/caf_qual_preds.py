
from wcq_ratings import teams
import pandas as pd
import random
from scipy.stats import poisson
print("Simulating African Qualifying...")
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
    if home_goals_pred == "":
        home_goals_pred = 0.1
    if away_goals_pred == "":
        away_goals_pred = 2.0
    home_team_goals_sim = poisson.rvs(home_goals_pred,size=num_sims)
    away_team_goals_sim = poisson.rvs(away_goals_pred,size=num_sims)
    #print(home_goals_pred,"-",away_goals_pred)
    return home_team_goals_sim, away_team_goals_sim

def choose_random_sim(home_team_goals_sim,away_team_goals_sim):
    results_df = pd.DataFrame({
        'Team1 Goals': home_team_goals_sim,
        'Team2 Goals': away_team_goals_sim
    })
    results_df['Scoreline'] = results_df['Team1 Goals'].astype(str) + '-' + results_df['Team2 Goals'].astype(str)
    result_count = results_df['Scoreline'].value_counts()
    top_10_scorelines = result_count.head(5).index.tolist()
    #print("Top 3 Scorelines:",top_10_scorelines)
    selected_scoreline = random.choice(top_10_scorelines)
    #print(selected_scoreline)
    hg, ag = map(int, selected_scoreline.split('-'))
    return hg,ag

def simulate_all_games(groupA):
    for index, row in groupA.iterrows():
        if pd.isnull(row['HomeScore']) or pd.isnull(row['AwayScore']):
            home_team = groupA.at[index, 'Home']
            away_team = groupA.at[index, 'Away']
            #print("Simulating",home_team,"vs",away_team,"...")
            game_ratings = teams[teams['Team'].isin([home_team,away_team])]
            home_goals_pred,away_goals_pred = calculate_xg_values(home_team,away_team,game_ratings)
            home_score, away_score = simulate_match(home_goals_pred,away_goals_pred,10000)
            hg, ag = choose_random_sim(home_score,away_score)
            groupA.at[index, 'HomeScore'] = (hg)
            groupA.at[index, 'AwayScore'] = (ag)
            #print(hg,"-",ag)

def get_table_from_predictions(groupApreds):
    team_stats = {}
    for index, row in groupApreds.iterrows():
        home_team = row['Home']
        away_team = row['Away']
        home_goals = row['HomeScore']
        away_goals = row['AwayScore']
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
    #print(summary_df)
    return summary_df


#Group A
print("  Simulating Group A...")
groupA = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/caf/caf-grpA.csv")
simulate_all_games(groupA)
groupAtable = get_table_from_predictions(groupA)

#Group B
print("  Simulating Group B...")
groupB = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/caf/caf-grpB.csv")
simulate_all_games(groupB)
groupBtable = get_table_from_predictions(groupB)

#Group C
print("  Simulating Group C...")
groupC = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/caf/caf-grpC.csv")
simulate_all_games(groupC)
groupCtable = get_table_from_predictions(groupC)

#Group D
print("  Simulating Group D...")
groupD = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/caf/caf-grpD.csv")
simulate_all_games(groupD)
groupDtable = get_table_from_predictions(groupD)

#Group E
print("  Simulating Group E...")
groupE = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/caf/caf-grpE.csv")
simulate_all_games(groupE)
groupEtable = get_table_from_predictions(groupE)

#Group F
print("  Simulating Group F...")
groupF = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/caf/caf-grpF.csv")
simulate_all_games(groupF)
groupFtable = get_table_from_predictions(groupF)

#Group G
print("  Simulating Group G...")
groupG = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/caf/caf-grpG.csv")
simulate_all_games(groupG)
groupGtable = get_table_from_predictions(groupG)

#Group H
print("  Simulating Group H...")
groupH = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/caf/caf-grpH.csv")
simulate_all_games(groupH)
groupHtable = get_table_from_predictions(groupH)

#Group I
print("  Simulating Group I...")
groupI = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/caf/caf-grpI.csv")
simulate_all_games(groupI)
groupItable = get_table_from_predictions(groupI)

caf_qualifiers = [groupAtable['Team'][0],
              groupBtable['Team'][0],
              groupCtable['Team'][0],
              groupDtable['Team'][0],
              groupEtable['Team'][0],
              groupFtable['Team'][0],
              groupGtable['Team'][0],
              groupHtable['Team'][0],
              groupItable['Team'][0]]

second_places = [[groupAtable['Team'][1],groupAtable['Points'][1],groupAtable['Goal Difference'][1]],
                 [groupBtable['Team'][1],groupBtable['Points'][1],groupBtable['Goal Difference'][1]],
                 [groupCtable['Team'][1],groupCtable['Points'][1],groupCtable['Goal Difference'][1]],
                 [groupDtable['Team'][1],groupDtable['Points'][1],groupDtable['Goal Difference'][1]],
                 [groupEtable['Team'][1],groupEtable['Points'][1],groupEtable['Goal Difference'][1]],
                 [groupFtable['Team'][1],groupFtable['Points'][1],groupFtable['Goal Difference'][1]],
                 [groupGtable['Team'][1],groupGtable['Points'][1],groupGtable['Goal Difference'][1]],
                 [groupHtable['Team'][1],groupHtable['Points'][1],groupHtable['Goal Difference'][1]],
                 [groupItable['Team'][1],groupItable['Points'][1],groupItable['Goal Difference'][1]]]

second_places_sorted = sorted(second_places, key=lambda x: (x[1], x[2]),reverse=True)

playoff_teams = [second_places_sorted[0][0],
                 second_places_sorted[1][0],
                 second_places_sorted[2][0],
                 second_places_sorted[3][0]]

#print(caf_qualifiers)
print("  Simulating Playoffs...")
#print("Semi Final 1:",playoff_teams[0],"vs",playoff_teams[3])
home_goals_pred,away_goals_pred = calculate_xg_values(playoff_teams[0],playoff_teams[3],teams)
home_score, away_score = simulate_match(home_goals_pred,away_goals_pred,10000)
hg, ag = choose_random_sim(home_score,away_score)
#print(hg,ag)
if hg > ag:
    sf1_winner = playoff_teams[0]
elif ag > hg:
    sf1_winner = playoff_teams[3]
else:
    coin = random.randint(1,2)
    if coin == 1:
        sf1_winner = playoff_teams[0]
    elif coin == 2:
        sf1_winner = playoff_teams[3]

#print("Semi Final 2:",playoff_teams[1],"vs",playoff_teams[2])
home_goals_pred,away_goals_pred = calculate_xg_values(playoff_teams[1],playoff_teams[2],teams)
home_score, away_score = simulate_match(home_goals_pred,away_goals_pred,10000)
hg, ag = choose_random_sim(home_score,away_score)
#print(hg,ag)
if hg > ag:
    sf2_winner = playoff_teams[1]
elif ag > hg:
    sf2_winner = playoff_teams[2]
else:
    coin = random.randint(1,2)
    if coin == 1:
        sf2_winner = playoff_teams[1]
    elif coin == 2:
        sf2_winner = playoff_teams[2]

#print("Final:",sf1_winner,"vs",sf2_winner)
home_goals_pred,away_goals_pred = calculate_xg_values(sf1_winner,sf2_winner,teams)
home_score, away_score = simulate_match(home_goals_pred,away_goals_pred,10000)
hg, ag = choose_random_sim(home_score,away_score)
#print(hg,ag)
if hg > ag:
    caf_icp_rep = sf1_winner
elif ag > hg:
    caf_icp_rep = sf2_winner
else:
    coin = random.randint(1,2)
    if coin == 1:
        caf_icp_rep = sf1_winner
    elif coin == 2:
        caf_icp_rep = sf2_winner

#print(caf_icp_rep)