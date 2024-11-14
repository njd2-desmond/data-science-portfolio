import pandas as pd
from scipy import stats
from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv(r"rugby-prediction/data/premiership_fixtures.csv")

#Creating Team Ratings

home_stats = df[['H-Team','H-Score', 'H-Tries','H-Cons','H-Pens','H-Drops','H-PenTry','A-Score','A-Tries','A-Cons','A-Pens','A-Drops','A-PenTry']]
away_stats = df[['A-Team','A-Score', 'A-Tries','A-Cons','A-Pens','A-Drops','A-PenTry','H-Score','H-Tries','H-Cons','H-Pens','H-Drops','H-PenTry']]
home_stats.columns = ['Team', 'Score', 'Tries', 'Cons', 'Pens', 'Drops', 'Penalty Tries','ScoreA','TriesA','ConsA','PensA','DropsA','Penalty Tries A']
away_stats.columns = ['Team', 'Score', 'Tries', 'Cons', 'Pens', 'Drops', 'Penalty Tries','ScoreA','TriesA','ConsA','PensA','DropsA','Penalty Tries A']

all_stats = pd.concat([home_stats,away_stats])
team_stats = all_stats.groupby('Team').mean().reset_index()
#print(team_stats)
home_team = "Newcastle"
away_team = "Saracens"

#Home Attack & Away Defense
home_x_tries = (team_stats[team_stats['Team']==home_team]['Tries']).iloc[0]
home_x_cons = (team_stats[team_stats['Team']==home_team]['Cons']).iloc[0]
home_x_pens = (team_stats[team_stats['Team']==home_team]['Pens']).iloc[0]
home_x_drops = (team_stats[team_stats['Team']==home_team]['Drops']).iloc[0]
home_x_pentries = (team_stats[team_stats['Team']==home_team]['Penalty Tries']).iloc[0]

away_x_tries_con = (team_stats[team_stats['Team']==away_team]['TriesA']).iloc[0]
away_x_cons_con = (team_stats[team_stats['Team']==away_team]['ConsA']).iloc[0]
away_x_pens_con = (team_stats[team_stats['Team']==away_team]['PensA']).iloc[0]
away_x_drops_con = (team_stats[team_stats['Team']==away_team]['DropsA']).iloc[0]
away_x_pentries_con = (team_stats[team_stats['Team']==away_team]['Penalty Tries A']).iloc[0]

#Home Defense & Away Attack
home_x_tries_con = (team_stats[team_stats['Team']==home_team]['TriesA']).iloc[0]
home_x_cons_con = (team_stats[team_stats['Team']==home_team]['ConsA']).iloc[0]
home_x_pens_con = (team_stats[team_stats['Team']==home_team]['PensA']).iloc[0]
home_x_drops_con = (team_stats[team_stats['Team']==home_team]['DropsA']).iloc[0]
home_x_pentries_con = (team_stats[team_stats['Team']==home_team]['Penalty Tries A']).iloc[0]

away_x_tries = (team_stats[team_stats['Team']==away_team]['Tries']).iloc[0]
away_x_cons = (team_stats[team_stats['Team']==away_team]['Cons']).iloc[0]
away_x_pens = (team_stats[team_stats['Team']==away_team]['Pens']).iloc[0]
away_x_drops = (team_stats[team_stats['Team']==away_team]['Drops']).iloc[0]
away_x_pentries = (team_stats[team_stats['Team']==away_team]['Penalty Tries']).iloc[0]

home_score_list = []
away_score_list = []
for x in range(0,1000):
    #Home Prediction
    home_tries_pred = (home_x_tries + away_x_tries_con) / 2
    home_cons_pred = (home_x_cons + away_x_cons_con) / 2
    home_pens_pred = (home_x_pens + away_x_pens_con) / 2
    home_drops_pred = (home_x_drops + away_x_drops_con) / 2
    home_pentries_pred = (home_x_pentries + away_x_pentries_con) / 2
    #Away Prediction
    away_tries_pred = (home_x_tries_con + away_x_tries) / 2
    away_cons_pred = (home_x_cons_con + away_x_cons) / 2
    away_pens_pred = (home_x_pens_con + away_x_pens) / 2
    away_drops_pred = (home_x_drops_con + away_x_drops) / 2
    away_pentries_pred = (home_x_pentries_con + away_x_pentries) / 2
    #Simulations
    home_tries_pred_sim = poisson.rvs(home_tries_pred,size=10000)[0]
    home_cons_pred_sim = poisson.rvs(home_cons_pred,size=10000)[0]
    home_pens_pred_sim = poisson.rvs(home_pens_pred,size=10000)[0]
    home_drops_pred_sim = poisson.rvs(home_drops_pred,size=10000)[0]
    home_pentries_pred_sim = poisson.rvs(home_pentries_pred,size=10000)[0]

    away_tries_pred_sim = poisson.rvs(away_tries_pred,size=10000)[0]
    away_cons_pred_sim = poisson.rvs(away_cons_pred,size=10000)[0]
    away_pens_pred_sim = poisson.rvs(away_pens_pred,size=10000)[0]
    away_drops_pred_sim = poisson.rvs(away_drops_pred,size=10000)[0]
    away_pentries_pred_sim = poisson.rvs(away_pentries_pred,size=10000)[0]

    if home_cons_pred_sim > home_tries_pred_sim:
        home_cons_pred_sim = home_tries_pred_sim
    if away_cons_pred_sim > away_tries_pred_sim:
        away_cons_pred_sim = away_tries_pred_sim

    home_exp_points_for = (home_tries_pred_sim*5)+(home_cons_pred_sim*2)+(home_pens_pred_sim*3)+(home_drops_pred_sim*2)+(home_pentries_pred_sim*7)
    away_exp_points_for = (away_tries_pred_sim*5)+(away_cons_pred_sim*2)+(away_pens_pred_sim*3)+(away_drops_pred_sim*2)+(away_pentries_pred_sim*7)
    home_score_list.append(home_exp_points_for)
    away_score_list.append(away_exp_points_for)

home_counts = pd.Series(home_score_list).value_counts()
away_counts = pd.Series(away_score_list).value_counts()

home_q1 = pd.Series(home_score_list).quantile(0.375)
home_q3 = pd.Series(home_score_list).quantile(0.625)
print(home_q1,home_q3)
away_q1 = pd.Series(away_score_list).quantile(0.375)
away_q3 = pd.Series(away_score_list).quantile(0.625)
print(away_q1,away_q3)

combined_counts = pd.DataFrame({'Home':home_counts,'Away':away_counts}).fillna(0)
combined_counts = combined_counts.sort_index()
#print(home_score_list)
combined_counts.plot(kind='bar', color=['darkgreen','darkblue'])
plt.show()