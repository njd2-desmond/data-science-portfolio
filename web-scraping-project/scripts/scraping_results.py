import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
sys.stdout.reconfigure(encoding='utf-8')

url = 'https://fbref.com/en/comps/9/2023-2024/schedule/2023-2024-Premier-League-Scores-and-Fixtures'
url2 = 'https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures'
page = requests.get(url2)

soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table')
world_titles = (table.find_all('th')[1:14])
world_table_titles = [title.text.strip() for title in world_titles]
df = pd.DataFrame(columns = world_table_titles)
print(df)
column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data

print(df)

df['Score'] = df['Score'].replace({'–': '-', '—': '-', 'NaN': None, 'invalid': None}, regex=True)
df[['HG', 'AG']] = df['Score'].str.split('-', expand=True)
df = df.drop(columns=['Score'])
df.to_csv(r'web-scraping-project\data\epl-24-25-results.csv',index=False)