import pandas as pd
import random
from scipy.stats import poisson
df = pd.read_csv("world-cup-simulation-project/results.csv")
df = pd.read_csv("world-cup-simulation-project/ucl-fixtures.csv")
df = df.drop(['Referee','Attendance','Venue','Match Report','Notes','Score','Day','Wk'],axis=1)

pd.options.display.max_columns = 100

#qualifying_df = df[df['tournament'] == "FIFA World Cup"]
#big_teams_list = ['Argentina', 'Brazil', 'England','France','Germany','Netherlands','Spain','Italy','Portugal']
#na_teams_list = ['United States','Canada','Mexico']
#big_teams_qualifying_df = qualifying_df[qualifying_df['home_team'].isin(big_teams_list) | qualifying_df['away_team'].isin(big_teams_list)]

def results_to_ratings(results_file):
    
    #Home Record
    home_goals_for = results_file.groupby("Home")["xG"].mean().reset_index()
    home_goals_for.columns = ['Team', 'HG']
    home_goals_aga = results_file.groupby("Home")["xGA"].mean().reset_index()
    home_goals_aga.columns = ['Team', 'HGA']
    home_gf_ga = pd.merge(home_goals_for,home_goals_aga, on='Team', how='outer')

    #Away Record
    away_goals_for = results_file.groupby("Away")["xGA"].mean().reset_index()
    away_goals_for.columns = ['Team', 'AG']
    away_goals_aga = results_file.groupby("Away")["xG"].mean().reset_index()
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


teams_list_24_25 = ['RB Salzburg','Sturm Graz',
                    'Club Brugge',
                    'Young Boys',
                    'Sparta Prague',
                    'Bayern Munich','Dortmund','Leverkusen','RB Leipzig','Stuttgart',
                    'Arsenal','Aston Villa','Liverpool','Manchester City',
                    'Atletico Madrid','Barcelona','Girona','Real Madrid',
                    'Brest','Lille','Monaco','Paris S-G',
                    'Dinamo Zagreb',
                    'Atalanta','Bologna','Inter','Juventus','Milan',
                    'Feyenoord','PSV Eindhoven',
                    'Benfica','Sporting CP'
                    'Red Star',
                    'Celtic',
                    'Slovan Bratislava',
                    'Shakhtar']
qualifying_ratings = results_to_ratings(df)
this_years_ratings = qualifying_ratings[qualifying_ratings['Team'].isin(teams_list_24_25)]
print(this_years_ratings)

paris_df = df[(df['Home'] == 'Paris S-G') | (df['Away'] == 'Paris S-G')]
#print(paris_df)

def simulate_match(home_goals_pred,away_goals_pred, num_sims=10000):
    home_team_goals_sim = poisson.rvs(home_goals_pred,size=num_sims)
    away_team_goals_sim = poisson.rvs(away_goals_pred,size=num_sims)
    #print("Simulating",home_team,"vs",away_team,"...")
    return home_team_goals_sim, away_team_goals_sim

def choose_random_sim(home_team_goals_sim,away_team_goals_sim):
    results_df = pd.DataFrame({
        'Team1 Goals': home_team_goals_sim,
        'Team2 Goals': away_team_goals_sim
    })
    results_df['Scoreline'] = results_df['Team1 Goals'].astype(str) + '-' + results_df['Team2 Goals'].astype(str)
    result_count = results_df['Scoreline'].value_counts()
    top_10_scorelines = result_count.head(5).index.tolist()
    print("Top 5 Scorelines:",top_10_scorelines)
    selected_scoreline = random.choice(top_10_scorelines)
    print(selected_scoreline)
    hg, ag = map(int, selected_scoreline.split('-'))
    return hg,ag

home_score, away_score = simulate_match(1.66,2.61,1000)
hg, ag = random_sim_game = choose_random_sim(home_score,away_score)
