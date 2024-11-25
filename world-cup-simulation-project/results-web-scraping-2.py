import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

#This page takes the Seasons Fixtures from Fbref.com and scrapes them, turning them into a dataset

# BE CAREFUL TO NOT SCRAPE DATA TOO FREQUENTLY, THIS CAN LEAD TO THE PROGRAM NOT WORKING.
#Take URL from fbref.com

def scrape_and_clean(url,columns):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    print(url)
    table = soup.find('table')
    if table is None:
        print("Table not found on this page")
    else:
        table_titles = (table.find_all('th')[1:columns]) #Finds Column Headings of the Data
        world_table_titles = [title.text.strip() for title in table_titles] #Removes unnecessary data from the Column Heading names
        df = pd.DataFrame(columns = world_table_titles) #Transforms Column Heading data into a Dataframe for ease of use
        column_data = table.find_all('tr') #Finds data in the columns to insert into the Df
        for row in column_data[1:]: #Ignores row.
            row_data = row.find_all('td') #Finds all the data from the current row.
            individual_row_data = [data.text.strip() for data in row_data] #Strips unnecessary data.
            #print("DATA:",individual_row_data)
            if not row_data:
                continue
            length = len(df)
            #print(df)
            df.loc[length] = individual_row_data #Inputs the Row data into the Dataframe, making sure the length is appropriate for the dataframe

        df['Score'] = df['Score'].replace({'–': '-', '—': '-', 'NaN': None, 'invalid': None}, regex=True) #Cleans 'Score' column...
        df['Score'] = df['Score'].apply(lambda x: re.sub(r'\(\d+\)', '', x).strip())
        df['Home'] = df['Home'].apply(lambda team_name: " ".join(word for word in team_name.split() if not word.islower()))
        df['Away'] = df['Away'].apply(lambda team_name: " ".join(word for word in team_name.split() if not word.islower()))
        df[['HG', 'AG']] = df['Score'].str.split('-', expand=True) #...and transforms it into two variables: Home Score and Away Score
        #df['HG'] = df['HG'].replace({})
        df = df.drop(columns=['Score','Day','Time', "Venue","Attendance","Referee","Match Report","Notes"]) #Removes the Score column as it is now unnecessary
        #print(df)
    return df

def scrape_all_sites(sites,columns):
    final_df = pd.DataFrame()
    for site in sites:
        df = scrape_and_clean(site,columns)
        final_df = pd.concat([final_df, df])
    return final_df

all_uefa_sites = ['https://fbref.com/en/comps/6/2014/schedule/2014-WCQ----UEFA-M-Scores-and-Fixtures',
                  'https://fbref.com/en/comps/6/2018/schedule/2018-WCQ----UEFA-M-Scores-and-Fixtures',
                  'https://fbref.com/en/comps/6/schedule/WCQ----UEFA-M-Scores-and-Fixtures']
uefa_final_df = scrape_all_sites(all_uefa_sites,13)

all_conmebol_sites =['https://fbref.com/en/comps/4/2018/schedule/2018-WCQ----CONMEBOL-M-Scores-and-Fixtures',
                     'https://fbref.com/en/comps/4/2022/schedule/2022-WCQ----CONMEBOL-M-Scores-and-Fixtures',
                     'https://fbref.com/en/comps/4/schedule/WCQ----CONMEBOL-M-Scores-and-Fixtures']
conmebol_final_df = scrape_all_sites(all_conmebol_sites,12)

all_caf_sites = ['https://fbref.com/en/comps/2/2018/schedule/2018-WCQ----CAF-M-Scores-and-Fixtures',
                 'https://fbref.com/en/comps/2/2022/schedule/2022-WCQ----CAF-M-Scores-and-Fixtures',
                 'https://fbref.com/en/comps/2/schedule/WCQ----CAF-M-Scores-and-Fixtures']
caf_final_df = scrape_all_sites(all_caf_sites,13)

uefa_final_df.to_csv(r'world-cup-simulation-project\cleaned-results\uefa-qual-results-cleaned.csv',index=False) #Saves the Dataframe as a CSV. This will make it easier to explore in Python.
conmebol_final_df.to_csv(r'world-cup-simulation-project\cleaned-results\conmebol-qual-results-cleaned.csv',index=False) #Saves the Dataframe as a CSV. This will make it easier to explore in Python.
caf_final_df.to_csv(r'world-cup-simulation-project\cleaned-results\caf-qual-results-cleaned.csv',index=False) #Saves the Dataframe as a CSV. This will make it easier to explore in Python.

print("Data scraped and cleaned")

print(uefa_final_df)
print(conmebol_final_df)
print(caf_final_df)