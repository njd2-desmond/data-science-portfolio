import pandas as pd
results_23_24 = pd.read_csv('web-scraping-project\data\epl-24-25-results-cleaned.csv')
print(results_23_24)

#Home Record
home_goals_for = results_23_24.groupby("Home")["HG"].mean().reset_index()
home_goals_for.columns = ['Team', 'xG']
home_goals_aga = results_23_24.groupby("Home")["AG"].mean().reset_index()
home_goals_aga.columns = ['Team', 'xGA']
home_gf_ga = pd.merge(home_goals_for,home_goals_aga, on='Team', how='outer')

#Away Record
away_goals_for = results_23_24.groupby("Away")["AG"].mean().reset_index()
away_goals_for.columns = ['Team', 'xG']
away_goals_aga = results_23_24.groupby("Away")["HG"].mean().reset_index()
away_goals_aga.columns = ['Team', 'xGA']
away_gf_ga = pd.merge(away_goals_for,away_goals_aga, on='Team', how='outer')


teams = pd.merge(home_gf_ga,away_gf_ga,on='Team',how='outer')

teams["xG_x"] = teams['xG_x'] / 1.2
teams["xGA_x"] = teams['xGA_x'] / 1
teams["xG_y"] = teams['xG_y'] / 1.2
teams["xGA_y"] = teams['xGA_y'] / 1
print(teams)

teams.to_csv(r'web-scraping-project\data\team-home-away-ratings.csv',index=False)