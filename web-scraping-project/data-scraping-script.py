import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
sys.stdout.reconfigure(encoding='utf-8')

url = 'https://en.wikipedia.org/wiki/Premier_League_records_and_statistics'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find_all('table')[6]

world_titles = (table.find_all('th'))

world_table_tiles = [title.text.strip() for title in world_titles]

df = pd.DataFrame(columns = world_table_tiles)

column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data

df.to_csv(r'web-scraping-project\data\epl-alltime-data.csv',index=False)