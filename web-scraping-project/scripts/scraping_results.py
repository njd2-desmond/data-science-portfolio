import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
sys.stdout.reconfigure(encoding='utf-8')

#This page takes the Seasons Fixtures from Fbref.com and scrapes them, turning them into a dataset

#Take URL from fbref.com
url2 = 'https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures'
page = requests.get(url2)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table')
table_titles = (table.find_all('th')[1:14]) #Finds Column Headings of the Data
world_table_titles = [title.text.strip() for title in table_titles] #Removes unnecessary data from the Column Heading names
df = pd.DataFrame(columns = world_table_titles) #Transforms Column Heading data into a Dataframe for ease of use
column_data = table.find_all('tr') #Finds data in the columns to insert into the Df

for row in column_data[1:]: #Ignores first column. This is a 'Week' number that causes formatting issues because it is only written once every game week.
    row_data = row.find_all('td') #Finds all the data from the current row.
    individual_row_data = [data.text.strip() for data in row_data] #Strips unnecessary data.
    length = len(df)
    df.loc[length] = individual_row_data #Inputs the Row data into the Dataframe, making sure the length is appropriate for the dataframe

df['Score'] = df['Score'].replace({'–': '-', '—': '-', 'NaN': None, 'invalid': None}, regex=True) #Cleans 'Score' column...
df[['HG', 'AG']] = df['Score'].str.split('-', expand=True) #...and transforms it into two variables: Home Score and Away Score
df = df.drop(columns=['Score','Day','Time', "Venue","Attendance","Referee","Match Report","Notes"]) #Removes the Score column as it is now unnecessary
df.columns = ['Date','Home','HxG','AxG','Away','HG','AG']
df.to_csv(r'web-scraping-project\data\epl-24-25-results-cleaned.csv',index=False) #Saves the Dataframe as a CSV. This will make it easier to explore in Python.
print("Data scraped from",url2,"and cleaned")