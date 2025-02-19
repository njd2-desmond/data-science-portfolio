import pandas as pd
from caf_qual_preds import simulate_all_games, get_table_from_predictions
print("Simulating South American Qualifying...")
conmebol = pd.read_csv("C:/Users/nickd/data-science-portfolio/wc-qual-preds/conmebol/conmebol.csv")
simulate_all_games(conmebol)
conmebol = get_table_from_predictions(conmebol)
#print(conmebol)

conmebol_qualifiers = [conmebol['Team'][0],
                       conmebol['Team'][1],
                       conmebol['Team'][2],
                       conmebol['Team'][3],
                       conmebol['Team'][4],
                       conmebol['Team'][5]]

conmebol_icp_rep = conmebol['Team'][6]
