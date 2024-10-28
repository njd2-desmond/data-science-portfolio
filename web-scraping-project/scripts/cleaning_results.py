import pandas as pd

df = pd.read_csv('web-scraping-project\data\epl-24-25-results.csv')
df_columns_removed = df.drop(columns = ["Day","Time","xG","xG.1","Venue","Attendance","Referee","Match Report","Notes"])
df_nulls_and_cols_removed = df_columns_removed.dropna(subset=['Home'])
print(df_nulls_and_cols_removed)

df_nulls_and_cols_removed.to_csv(r'web-scraping-project\data\epl-24-25-results-cleaned.csv',index=False)