from caf_qual_preds import caf_qualifiers, caf_icp_rep
from conmebol_qual_preds import conmebol_qualifiers, conmebol_icp_rep
from ofc_qual_preds import ofc_qualifier, ofc_icp_rep
from concacaf_qual_preds import concacaf_qualifiers, concacaf_icp_reps
from uefa_qual_preds import uefa_qualifiers
from afc_qual_preds import afc_qualifiers, afc_icp_rep
import pandas as pd
import random

icp_qualifiers = [afc_icp_rep,
                  caf_icp_rep,
                  ofc_icp_rep,
                  conmebol_icp_rep,
                  concacaf_icp_reps[0],
                  concacaf_icp_reps[1]]

coin1 = random.randint(0,5)
icpw1 = icp_qualifiers[coin1]
icp_qualifiers.remove(icpw1)

coin2 = random.randint(0,4)
icpw2 = icp_qualifiers[coin2]
icp_qualifiers.remove(icpw2)

icp_winners = [icpw1,
               icpw2]

all_wc_teams = caf_qualifiers + afc_qualifiers + uefa_qualifiers + concacaf_qualifiers + conmebol_qualifiers + icp_winners
all_wc_teams.append(ofc_qualifier)

rankings = pd.read_csv(r"C:\Users\nickd\data-science-portfolio\wc-qual-preds\world_rankings.csv")
def lookup(team,rankings):
    rank = rankings.loc[rankings['Team'] == team, 'Ranking'].iloc[0]
    return team,rank

team_rankings = []
for team in all_wc_teams:
    team,ranking = lookup(team, rankings)
    team_rankings.append([team,ranking])
    #print(lookup(team,rankings))
team_rankings_sorted = sorted(team_rankings, key=lambda x: (x[1]))
#print(team_rankings_sorted)

potA = [team_rankings_sorted[0][0],
        team_rankings_sorted[1][0],
        team_rankings_sorted[2][0],
        team_rankings_sorted[3][0],
        team_rankings_sorted[4][0],
        team_rankings_sorted[5][0],
        team_rankings_sorted[6][0],
        team_rankings_sorted[7][0],
        team_rankings_sorted[8][0],
        ]
#print("Pot A:",potA)

potB = [team_rankings_sorted[9][0],
        team_rankings_sorted[10][0],
        team_rankings_sorted[11][0],
        team_rankings_sorted[12][0],
        team_rankings_sorted[13][0],
        team_rankings_sorted[14][0],
        team_rankings_sorted[15][0],
        team_rankings_sorted[16][0],
        team_rankings_sorted[17][0],
        team_rankings_sorted[18][0],
        team_rankings_sorted[19][0],
        team_rankings_sorted[20][0]]
#print("Pot B:",potB)

potC = [team_rankings_sorted[21][0],
        team_rankings_sorted[22][0],
        team_rankings_sorted[23][0],
        team_rankings_sorted[24][0],
        team_rankings_sorted[25][0],
        team_rankings_sorted[26][0],
        team_rankings_sorted[27][0],
        team_rankings_sorted[28][0],
        team_rankings_sorted[29][0],
        team_rankings_sorted[30][0],
        team_rankings_sorted[31][0],
        team_rankings_sorted[32][0]]
#print("Pot C:",potC)

potD = [team_rankings_sorted[33][0],
        team_rankings_sorted[34][0],
        team_rankings_sorted[35][0],
        team_rankings_sorted[36][0],
        team_rankings_sorted[37][0],
        team_rankings_sorted[38][0],
        team_rankings_sorted[39][0],
        team_rankings_sorted[40][0],
        team_rankings_sorted[41][0],
        team_rankings_sorted[42][0],
        team_rankings_sorted[43][0],
        team_rankings_sorted[44][0]]
#print("Pot D:",potD)
########################################
print("Group A...")
coin1 = random.randint(0,len(potB)-1)
a1 = potB[coin1]
potB.remove(a1)

coin2 = random.randint(0,len(potC)-1)
a2 = potC[coin2]
potC.remove(a2)

coin3 = random.randint(0,len(potD)-1)
a3 = potD[coin3]
potD.remove(a3)
print(" A1: Mexico")
print(" A2:",a1)
print(" A3:",a2)
print(" A4:",a3)
########################################
print("Group B...")
coin1 = random.randint(0,len(potB)-1)
b1 = potB[coin1]
potB.remove(b1)

coin2 = random.randint(0,len(potC)-1)
b2 = potC[coin2]
potC.remove(b2)

coin3 = random.randint(0,len(potD)-1)
b3 = potD[coin3]
potD.remove(b3)
print(" B1: Canada")
print(" B2:",b1)
print(" B3:",b2)
print(" B4:",b3)
########################################
print("Group C...")
coin4 = random.randint(0,len(potA)-1)
c4 = potA[coin4]
potA.remove(c4)

coin1 = random.randint(0,len(potB)-1)
c1 = potB[coin1]
potB.remove(c1)

coin2 = random.randint(0,len(potC)-1)
c2 = potC[coin2]
potC.remove(c2)

coin3 = random.randint(0,len(potD)-1)
c3 = potD[coin3]
potD.remove(c3)
print(" C1:",c4)
print(" C2:",c1)
print(" C3:",c2)
print(" C4:",c3)
########################################
print("Group D...")
coin1 = random.randint(0,len(potB)-1)
d1 = potB[coin1]
potB.remove(d1)

coin2 = random.randint(0,len(potC)-1)
d2 = potC[coin2]
potC.remove(d2)

coin3 = random.randint(0,len(potD)-1)
d3 = potD[coin3]
potD.remove(d3)
print(" D1: United States")
print(" D2:",d1)
print(" D3:",d2)
print(" D4:",d3)
########################################
print("Group E...")
coin4 = random.randint(0,len(potA)-1)
e4 = potA[coin4]
potA.remove(e4)

coin1 = random.randint(0,len(potB)-1)
e1 = potB[coin1]
potB.remove(e1)

coin2 = random.randint(0,len(potC)-1)
e2 = potC[coin2]
potC.remove(e2)

coin3 = random.randint(0,len(potD)-1)
e3 = potD[coin3]
potD.remove(e3)
print(" E1:",e4)
print(" E2:",e1)
print(" E3:",e2)
print(" E4:",e3)

########################################
print("Group F...")
coin4 = random.randint(0,len(potA)-1)
f4 = potA[coin4]
potA.remove(f4)

coin1 = random.randint(0,len(potB)-1)
f1 = potB[coin1]
potB.remove(f1)

coin2 = random.randint(0,len(potC)-1)
f2 = potC[coin2]
potC.remove(f2)

coin3 = random.randint(0,len(potD)-1)
f3 = potD[coin3]
potD.remove(f3)
print(" F1:",f4)
print(" F2:",f1)
print(" F3:",f2)
print(" F4:",f3)

########################################
print("Group G...")
coin4 = random.randint(0,len(potA)-1)
g4 = potA[coin4]
potA.remove(g4)

coin1 = random.randint(0,len(potB)-1)
g1 = potB[coin1]
potB.remove(g1)

coin2 = random.randint(0,len(potC)-1)
g2 = potC[coin2]
potC.remove(g2)

coin3 = random.randint(0,len(potD)-1)
g3 = potD[coin3]
potD.remove(g3)
print(" G1:",g4)
print(" G2:",g1)
print(" G3:",g2)
print(" G4:",g3)

########################################
print("Group H...")
coin4 = random.randint(0,len(potA)-1)
h4 = potA[coin4]
potA.remove(h4)

coin1 = random.randint(0,len(potB)-1)
h1 = potB[coin1]
potB.remove(h1)

coin2 = random.randint(0,len(potC)-1)
h2 = potC[coin2]
potC.remove(h2)

coin3 = random.randint(0,len(potD)-1)
h3 = potD[coin3]
potD.remove(h3)
print(" H1:",h4)
print(" H2:",h1)
print(" H3:",h2)
print(" H4:",h3)

########################################
print("Group I...")
coin4 = random.randint(0,len(potA)-1)
i4 = potA[coin4]
potA.remove(i4)

coin1 = random.randint(0,len(potB)-1)
i1 = potB[coin1]
potB.remove(i1)

coin2 = random.randint(0,len(potC)-1)
i2 = potC[coin2]
potC.remove(i2)

coin3 = random.randint(0,len(potD)-1)
i3 = potD[coin3]
potD.remove(i3)
print(" I1:",i4)
print(" I2:",i1)
print(" I3:",i2)
print(" I4:",i3)

########################################
print("Group J...")
coin4 = random.randint(0,len(potA)-1)
j4 = potA[coin4]
potA.remove(j4)

coin1 = random.randint(0,len(potB)-1)
j1 = potB[coin1]
potB.remove(j1)

coin2 = random.randint(0,len(potC)-1)
j2 = potC[coin2]
potC.remove(j2)

coin3 = random.randint(0,len(potD)-1)
j3 = potD[coin3]
potD.remove(j3)
print(" J1:",j4)
print(" J2:",j1)
print(" J3:",j2)
print(" J4:",j3)

########################################
print("Group K...")
coin4 = random.randint(0,len(potA)-1)
k4 = potA[coin4]
potA.remove(k4)

coin1 = random.randint(0,len(potB)-1)
k1 = potB[coin1]
potB.remove(k1)

coin2 = random.randint(0,len(potC)-1)
k2 = potC[coin2]
potC.remove(k2)

coin3 = random.randint(0,len(potD)-1)
k3 = potD[coin3]
potD.remove(k3)
print(" K1:",k4)
print(" K2:",k1)
print(" K3:",k2)
print(" K4:",k3)

########################################
print("Group L...")
coin4 = random.randint(0,len(potA)-1)
l4 = potA[coin4]
potA.remove(l4)

coin1 = random.randint(0,len(potB)-1)
l1 = potB[coin1]
potB.remove(l1)

coin2 = random.randint(0,len(potC)-1)
l2 = potC[coin2]
potC.remove(l2)

coin3 = random.randint(0,len(potD)-1)
l3 = potD[coin3]
potD.remove(l3)
print(" L1:",l4)
print(" L2:",l1)
print(" L3:",l2)
print(" L4:",l3)