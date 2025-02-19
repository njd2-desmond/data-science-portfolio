import pandas as pd
import random
from caf_qual_preds import simulate_all_games, get_table_from_predictions
print("Simulating CONCACAF qualifying...")
#Group A
print(" Simulating Group A...")
groupA = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/concacaf/concacaf-grp2-A.csv")
simulate_all_games(groupA)
groupAtable = get_table_from_predictions(groupA)
#print(groupAtable)

print(" Simulating Group B...")
groupB = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/concacaf/concacaf-grp2-B.csv")
simulate_all_games(groupB)
groupBtable = get_table_from_predictions(groupB)
#print(groupBtable)

print(" Simulating Group C...")
groupC = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/concacaf/concacaf-grp2-C.csv")
simulate_all_games(groupC)
groupCtable = get_table_from_predictions(groupC)
#print(groupCtable)

print(" Simulating Group D...")
groupD = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/concacaf/concacaf-grp2-D.csv")
simulate_all_games(groupD)
groupDtable = get_table_from_predictions(groupD)
#print(groupDtable)

print(" Simulating Group E...")
groupE = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/concacaf/concacaf-grp2-E.csv")
simulate_all_games(groupE)
groupEtable = get_table_from_predictions(groupE)
#print(groupEtable)

print(" Simulating Group F...")
groupF = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/concacaf/concacaf-grp2-F.csv")
simulate_all_games(groupF)
groupFtable = get_table_from_predictions(groupF)
#print(groupFtable)

third_round_qualifiers = [groupAtable['Team'][0],
                          groupAtable['Team'][1],
                          groupBtable['Team'][0],
                          groupBtable['Team'][1],
                          groupCtable['Team'][0],
                          groupCtable['Team'][1],
                          groupDtable['Team'][0],
                          groupDtable['Team'][1],
                          groupEtable['Team'][0],
                          groupEtable['Team'][1],
                          groupFtable['Team'][0],
                          groupFtable['Team'][1],]

#print(third_round_qualifiers)

coin1 = random.randint(0,11)
cq1 = third_round_qualifiers[coin1]
third_round_qualifiers.remove(cq1)

coin2 = random.randint(0,10)
cq2 = third_round_qualifiers[coin2]
third_round_qualifiers.remove(cq2)

coin3 = random.randint(0,9)
cq3 = third_round_qualifiers[coin3]
third_round_qualifiers.remove(cq3)

coin4 = random.randint(0,8)
cq4 = third_round_qualifiers[coin4]
third_round_qualifiers.remove(cq4)

coin5 = random.randint(0,7)
cq5 = third_round_qualifiers[coin5]
third_round_qualifiers.remove(cq5)

concacaf_qualifiers = [cq1,cq2,cq3]
concacaf_icp_reps = [cq4,cq5]