import pandas as pd
import random
from caf_qual_preds import simulate_all_games, get_table_from_predictions
print("Simulating AFC qualifying...")
#Group A
print(" Simulating Group A...")
groupA = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/afc/afc-grp3-A.csv")
simulate_all_games(groupA)
groupAtable = get_table_from_predictions(groupA)
#print(groupAtable)

#Group B
print(" Simulating Group B...")
groupB = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/afc/afc-grp3-B.csv")
simulate_all_games(groupB)
groupBtable = get_table_from_predictions(groupB)
#print(groupBtable)

#Group C
print(" Simulating Group C...")
groupC = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/afc/afc-grp3-C.csv")
simulate_all_games(groupC)
groupCtable = get_table_from_predictions(groupC)
#print(groupCtable)

afc_qualifiers = [groupAtable['Team'][0],
                  groupAtable['Team'][1],
                  groupBtable['Team'][0],
                  groupBtable['Team'][1],
                  groupCtable['Team'][0],
                  groupCtable['Team'][1]]
#print(afc_qualifiers)

fourth_round_qualifiers = [groupAtable['Team'][2],
                           groupAtable['Team'][3],
                           groupBtable['Team'][2],
                           groupBtable['Team'][3],
                           groupCtable['Team'][2],
                           groupCtable['Team'][3]]
#print(fourth_round_qualifiers)

coin1 = random.randint(0,5)
frw1 = fourth_round_qualifiers[coin1]
fourth_round_qualifiers.remove(frw1)
#print(frw1)
coin2 = random.randint(0,4)
frw2 = fourth_round_qualifiers[coin2]
fourth_round_qualifiers.remove(frw2)
#print(frw2)
afc_qualifiers.append(frw1)
afc_qualifiers.append(frw2)

coin3 = random.randint(0,3)
afc_icp_rep = fourth_round_qualifiers[coin3]
fourth_round_qualifiers.remove(afc_icp_rep)

#print(afc_qualifiers)