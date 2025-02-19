import pandas as pd

#African Qualifying
df = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/results.csv")
wcq_form = df[df['tournament'] == "FIFA World Cup qualification"]
wcq_form = wcq_form[wcq_form['date'] > "2016-01-01"]

#Home Record
home_goals_for = wcq_form.groupby("home_team")["home_score"].mean().reset_index()
home_goals_for.columns = ['Team', 'HxG']
home_goals_aga = wcq_form.groupby("home_team")["away_score"].mean().reset_index()
home_goals_aga.columns = ['Team', 'HxGA']
home_gf_ga = pd.merge(home_goals_for,home_goals_aga, on='Team', how='outer')

#Away Record
away_goals_for = wcq_form.groupby("away_team")["away_score"].mean().reset_index()
away_goals_for.columns = ['Team', 'AxG']
away_goals_aga = wcq_form.groupby("away_team")["home_score"].mean().reset_index()
away_goals_aga.columns = ['Team', 'AxGA']
away_gf_ga = pd.merge(away_goals_for,away_goals_aga, on='Team', how='outer')


teams = pd.merge(home_gf_ga,away_gf_ga,on='Team',how='outer')

teams["HxG"] = round(teams['HxG'], 2)
teams["HxGA"] = round(teams['HxGA'], 2)
teams["AxG"] = round(teams['AxG'], 2)
teams["AxGA"] = round(teams['AxGA'], 2)

teams.to_csv("wc-qual-preds/teams.csv")