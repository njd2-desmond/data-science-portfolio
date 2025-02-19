import random
import pandas as pd
from scipy.stats import poisson

class WorldCup:

    def __init__(self,teams_df):
        self.teams_list = teams_df

    def get_random_team(self):
        num = random.randint(0,len(teams_df)-1)
        random_team1 = teams_df.loc[num,'Team']
        num = random.randint(0,len(teams_df)-1)
        random_team2 = teams_df.loc[num,'Team']
        return random_team1,random_team2

    def simulate_match(self,home_team,away_team):
        print("Simulating",home_team,"vs",away_team)
        h_xg = teams_df[teams_df['Team']==home_team]['HG'].iloc[0]
        h_xga = teams_df[teams_df['Team']==home_team]['AG'].iloc[0]
        a_xg = teams_df[teams_df['Team']==away_team]['HG'].iloc[0]
        a_xga = teams_df[teams_df['Team']==away_team]['AG'].iloc[0]
        match_h_xg = round(h_xg * a_xga,1)
        match_a_xg = round(a_xg * h_xga,1)
        home_team_goals_sim = poisson.rvs(match_h_xg,size=1000)
        away_team_goals_sim = poisson.rvs(match_a_xg,size=1000)
        results_df = pd.DataFrame({'Team1 Goals': home_team_goals_sim,'Team2 Goals': away_team_goals_sim})
        results_df['Scoreline'] = results_df['Team1 Goals'].astype(str) + '-' + results_df['Team2 Goals'].astype(str)
        result_count = results_df['Scoreline'].value_counts()
        top_5_scorelines = result_count.head(4).index.tolist()
        selected_scoreline = random.choice(top_5_scorelines)
        selected_scoreline = match_h_xg.astype(str) + "-" + match_a_xg.astype(str)
        print(top_5_scorelines)
        #print("Prediction",selected_scoreline)
        return selected_scoreline
    
teams_list = []

concacaf_teams_list = [["Canada",(2/6),(12/6)],
                       ["Mexico",(62/60),(101/60)]
                       ]

uefa_teams_list = [["England",104/74,68/74]]

conmebol_teams_list = [["Argentina",152/88,101/88]]

caf_teams_list = [["Algeria",13/13,19/13]]

afc_teams_list = [["Japan",25/25,33/25],
                  ["Saudi Arabia",14/19,44/19],
                  ["South Korea",39/38, 78/38]]

ofc_teams_list = [["New Zealand",4/6,14/6]]

teams_list = concacaf_teams_list + uefa_teams_list + conmebol_teams_list + caf_teams_list + afc_teams_list + ofc_teams_list

teams_df = pd.DataFrame(teams_list, columns=['Team','HG','AG'])

my_wc_sim = WorldCup(teams_df)

my_wc_sim.simulate_match("England","Argentina")
my_wc_sim.simulate_match("England","New Zealand")
my_wc_sim.simulate_match("England","Algeria")