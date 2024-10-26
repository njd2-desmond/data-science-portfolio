import pandas as pd
results_23_24 = pd.read_csv('web-scraping-project\data\epl-24-25-results-cleaned.csv')
print(results_23_24)

#Home Record
home_goals_for = results_23_24.groupby("Home")["xG"].median().reset_index()
home_goals_for.columns = ['Team', 'xG']
home_goals_aga = results_23_24.groupby("Home")["xG.1"].median().reset_index()
home_goals_aga.columns = ['Team', 'xGA']
home_gf_ga = pd.merge(home_goals_for,home_goals_aga, on='Team', how='outer')

#Away Record
away_goals_for = results_23_24.groupby("Away")["xG.1"].median().reset_index()
away_goals_for.columns = ['Team', 'xG']
away_goals_aga = results_23_24.groupby("Away")["xG"].median().reset_index()
away_goals_aga.columns = ['Team', 'xGA']
away_gf_ga = pd.merge(away_goals_for,away_goals_aga, on='Team', how='outer')

#print(home_gf_ga)
#print(away_gf_ga)

teams = pd.merge(home_gf_ga,away_gf_ga,on='Team',how='outer')
print(teams)

#teams["xG_x"] = teams['xG_x'] / (results_23_24['Home'].nunique())
#teams["xGA_x"] = teams['xGA_x'] / (results_23_24['Home'].nunique())
#teams["xG_y"] = teams['xG_y'] / (results_23_24['Away'].nunique())
#teams["xGA_y"] = teams['xGA_y'] / (results_23_24['Away'].nunique())
#print(teams)

#teams["xG_x"] = teams['xG_x'] / 4
#teams["xGA_x"] = teams['xGA_x'] / 4
#teams["xG_y"] = teams['xG_y'] / 4
#teams["xGA_y"] = teams['xGA_y'] / 4
#print(teams)

teams["xG_x"] = teams['xG_x'] / teams['xG_x'].median()
teams["xGA_x"] = teams['xGA_x'] / teams['xGA_x'].median()
teams["xG_y"] = teams['xG_y'] / teams['xG_y'].median()
teams["xGA_y"] = teams['xGA_y'] / teams['xGA_y'].median()
print(teams)

teams.to_csv(r'web-scraping-project\data\team-home-away-ratings.csv',index=False)