import pandas as pd

df = pd.read_csv("results.csv")

qualifying_df = df[df['tournament'] == "FIFA World Cup"]
big_teams_list = ['Argentina', 'Brazil', 'England','France','Germany','Netherlands','Spain','Italy','Portugal']
na_teams_list = ['United States','Canada','Mexico']
big_teams_qualifying_df = qualifying_df[qualifying_df['home_team'].isin(big_teams_list) | qualifying_df['away_team'].isin(big_teams_list)]
def results_to_ratings(results_file):
    
    #Home Record
    home_goals_for = results_file.groupby("home_team")["home_score"].mean().reset_index()
    home_goals_for.columns = ['Team', 'HG']
    home_goals_aga = results_file.groupby("home_team")["away_score"].mean().reset_index()
    home_goals_aga.columns = ['Team', 'HGA']
    home_gf_ga = pd.merge(home_goals_for,home_goals_aga, on='Team', how='outer')

    #Away Record
    away_goals_for = results_file.groupby("away_team")["away_score"].mean().reset_index()
    away_goals_for.columns = ['Team', 'AG']
    away_goals_aga = results_file.groupby("away_team")["home_score"].mean().reset_index()
    away_goals_aga.columns = ['Team', 'AGA']
    away_gf_ga = pd.merge(away_goals_for,away_goals_aga, on='Team', how='outer')

    team_ratings = pd.merge(home_gf_ga,away_gf_ga,on='Team',how='outer')

    team_ratings["HG"] = round(team_ratings['HG'], 2)
    team_ratings["HGA"] = round(team_ratings['HGA'], 2)
    team_ratings["AG"] = round(team_ratings['AG'], 2)
    team_ratings["AGA"] = round(team_ratings['AGA'], 2)
    team_ratings["GF"] = round((team_ratings['HG'] + team_ratings['AG']) / 2, 2)
    team_ratings["GA"] = round((team_ratings['HGA'] + team_ratings['AGA']) / 2, 2)
    return team_ratings

qualifying_ratings = results_to_ratings(qualifying_df)
print(qualifying_ratings[qualifying_ratings['Team'].isin(big_teams_list)])