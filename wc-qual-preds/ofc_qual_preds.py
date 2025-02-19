from caf_qual_preds import calculate_xg_values, simulate_match,choose_random_sim
from wcq_ratings import teams
import random
print("Simulating OFC qualifying...")
#print("Semi Final 1:",playoff_teams[0],"vs",playoff_teams[3])
home_goals_pred,away_goals_pred = calculate_xg_values("New Caledonia","Tahiti",teams)
home_score, away_score = simulate_match(home_goals_pred,away_goals_pred,10000)
hg, ag = choose_random_sim(home_score,away_score)
#print(hg,ag)
if hg > ag:
    sf1_winner = "New Caledonia"
elif ag > hg:
    sf1_winner = "Tahiti"
else:
    coin = random.randint(1,2)
    if coin == 1:
        sf1_winner = "New Caledonia"
    elif coin == 2:
        sf1_winner = "Tahiti"

#print("Semi Final 2:",playoff_teams[1],"vs",playoff_teams[2])
home_goals_pred,away_goals_pred = calculate_xg_values("New Zealand","Fiji",teams)
home_score, away_score = simulate_match(home_goals_pred,away_goals_pred,10000)
hg, ag = choose_random_sim(home_score,away_score)
#print(hg,ag)
if hg > ag:
    sf2_winner = "New Zealand"
elif ag > hg:
    sf2_winner = "Fiji"
else:
    coin = random.randint(1,2)
    if coin == 1:
        sf2_winner = "New Zealand"
    elif coin == 2:
        sf2_winner = "Fiji"

#print("Final:",sf1_winner,"vs",sf2_winner)
home_goals_pred,away_goals_pred = calculate_xg_values(sf1_winner,sf2_winner,teams)
home_score, away_score = simulate_match(home_goals_pred,away_goals_pred,10000)
hg, ag = choose_random_sim(home_score,away_score)
#print(hg,ag)
if hg > ag:
    ofc_qualifier = sf1_winner
    ofc_icp_rep = sf2_winner
elif ag > hg:
    ofc_qualifier = sf2_winner
    ofc_icp_rep = sf1_winner
else:
    coin = random.randint(1,2)
    if coin == 1:
        ofc_qualifier = sf1_winner
        ofc_icp_rep = sf2_winner
    elif coin == 2:
        ofc_qualifier = sf2_winner
        ofc_icp_rep = sf1_winner