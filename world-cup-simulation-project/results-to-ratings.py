import pandas as pd

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
    return team_ratings

conmebol_results_file = pd.read_csv(r'world-cup-simulation-project\cleaned-results\conmebol-qual-results-cleaned.csv',
                            encoding='latin-1')
conmebol_team_ratings = results_to_ratings(conmebol_results_file)
print(conmebol_team_ratings)
conmebol_team_ratings.to_csv(r'world-cup-simulation-project\home-away-ratings\conmebol-home-away-ratings.csv',index=False)


uefa_results_file = pd.read_csv(r'world-cup-simulation-project\cleaned-results\uefa-qual-results-cleaned.csv',
                            encoding='latin-1')
uefa_team_ratings = results_to_ratings(uefa_results_file)
print(uefa_team_ratings)
uefa_team_ratings.to_csv(r'world-cup-simulation-project\home-away-ratings\uefa-home-away-ratings.csv',index=False)

caf_results_file = pd.read_csv(r'world-cup-simulation-project\cleaned-results\caf-qual-results-cleaned.csv',
                            encoding='latin-1')
caf_team_ratings = results_to_ratings(caf_results_file)
print(caf_team_ratings)
caf_team_ratings.to_csv(r'world-cup-simulation-project\home-away-ratings\caf-home-away-ratings.csv',index=False)