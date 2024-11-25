import pandas as pd
results_23_24 = pd.read_csv('web-scraping-project\data\epl-24-25-results-cleaned.csv')

#Home Record
home_goals_for = results_23_24.groupby("Home")["HxG"].median().reset_index()
home_goals_for.columns = ['Team', 'HxG']
home_goals_aga = results_23_24.groupby("Home")["AxG"].median().reset_index()
home_goals_aga.columns = ['Team', 'HxGA']
home_gf_ga = pd.merge(home_goals_for,home_goals_aga, on='Team', how='outer')

#Away Record
away_goals_for = results_23_24.groupby("Away")["AxG"].median().reset_index()
away_goals_for.columns = ['Team', 'AxG']
away_goals_aga = results_23_24.groupby("Away")["HxG"].median().reset_index()
away_goals_aga.columns = ['Team', 'AxGA']
away_gf_ga = pd.merge(away_goals_for,away_goals_aga, on='Team', how='outer')


teams = pd.merge(home_gf_ga,away_gf_ga,on='Team',how='outer')

teams["HxG"] = round(teams['HxG'], 2)
teams["HxGA"] = round(teams['HxGA'], 2)
teams["AxG"] = round(teams['AxG'], 2)
teams["AxGA"] = round(teams['AxGA'], 2)
print(teams)

teams.to_csv(r'web-scraping-project\data\team-home-away-ratings.csv',index=False)