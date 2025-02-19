import pandas as pd
import random
from caf_qual_preds import simulate_all_games, get_table_from_predictions
print("Simulating UEFA qualifying...")
#Group A
print(" Simulating Group A...")
groupA = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/uefa/uefa-grpA.csv")
simulate_all_games(groupA)
groupAtable = get_table_from_predictions(groupA)
#print(groupAtable)

#Group B
print(" Simulating Group B...")
groupB = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/uefa/uefa-grpB.csv")
simulate_all_games(groupB)
groupBtable = get_table_from_predictions(groupB)
#print(groupBtable)

#Group C
print(" Simulating Group C...")
groupC = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/uefa/uefa-grpC.csv")
simulate_all_games(groupC)
groupCtable = get_table_from_predictions(groupC)
#print(groupCtable)

#Group D
print(" Simulating Group D...")
groupD = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/uefa/uefa-grpD.csv")
simulate_all_games(groupD)
groupDtable = get_table_from_predictions(groupD)
#print(groupDtable)

#Group E
print(" Simulating Group E...")
groupE = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/uefa/uefa-grpE.csv")
simulate_all_games(groupE)
groupEtable = get_table_from_predictions(groupE)
#print(groupEtable)

#Group F
print(" Simulating Group F...")
groupF = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/uefa/uefa-grpF.csv")
simulate_all_games(groupF)
groupFtable = get_table_from_predictions(groupF)
#print(groupFtable)

#Group G
print(" Simulating Group G...")
groupG = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/uefa/uefa-grpG.csv")
simulate_all_games(groupG)
groupGtable = get_table_from_predictions(groupG)
#print(groupGtable)

#Group H
print(" Simulating Group H...")
groupH = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/uefa/uefa-grpH.csv")
simulate_all_games(groupH)
groupHtable = get_table_from_predictions(groupH)
#print(groupHtable)

#Group I
print(" Simulating Group I...")
groupI = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/uefa/uefa-grpI.csv")
simulate_all_games(groupI)
groupItable = get_table_from_predictions(groupI)
#print(groupItable)

#Group J
print(" Simulating Group J...")
groupJ = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/uefa/uefa-grpJ.csv")
simulate_all_games(groupJ)
groupJtable = get_table_from_predictions(groupJ)
#print(groupJtable)

#Group K
print(" Simulating Group K...")
groupK = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/uefa/uefa-grpK.csv")
simulate_all_games(groupK)
groupKtable = get_table_from_predictions(groupK)
#print(groupKtable)

#Group L
print(" Simulating Group L...")
groupL = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/uefa/uefa-grpL.csv")
simulate_all_games(groupL)
groupLtable = get_table_from_predictions(groupL)
#print(groupLtable)

uefa_qualifiers = [groupAtable['Team'][0],
              groupBtable['Team'][0],
              groupCtable['Team'][0],
              groupDtable['Team'][0],
              groupEtable['Team'][0],
              groupFtable['Team'][0],
              groupGtable['Team'][0],
              groupHtable['Team'][0],
              groupItable['Team'][0],
              groupJtable['Team'][0],
              groupKtable['Team'][0],
              groupLtable['Team'][0],]

playoff_teams = [groupAtable['Team'][1],
              groupBtable['Team'][1],
              groupCtable['Team'][1],
              groupDtable['Team'][1],
              groupEtable['Team'][1],
              groupFtable['Team'][1],
              groupGtable['Team'][1],
              groupHtable['Team'][1],
              groupItable['Team'][1],
              groupJtable['Team'][1],
              groupKtable['Team'][1],
              groupLtable['Team'][1]]

coin1 = random.randint(0,11)
uq1 = playoff_teams[coin1]
playoff_teams.remove(uq1)

coin2 = random.randint(0,10)
uq2 = playoff_teams[coin2]
playoff_teams.remove(uq2)

coin3 = random.randint(0,9)
uq3 = playoff_teams[coin3]
playoff_teams.remove(uq3)

coin4 = random.randint(0,8)
uq4 = playoff_teams[coin4]
playoff_teams.remove(uq4)

uefa_qualifiers.append(uq1)
uefa_qualifiers.append(uq2)
uefa_qualifiers.append(uq3)
uefa_qualifiers.append(uq4)