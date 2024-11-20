def uefa_make_draw(seeded_teams_list, unseeded_teams_list):
    print("Making the UEFA Draw...")
    #Take List of Teams competing in UEFA
    #Return Fixture List Dataframe and Empty Group List
    pass



def play_match(team_1,team_2,neutral):
    print(team_1,"vs",team_2, "at a Neutral Venue" if neutral == True else "")
    #return scoreline (randomly picked from 10 most common scorelines)
    pass

def uefa_first_round():
    print("Running UEFA First Round...")
    for home_team in seeded_teams_list:
        for away_team in seeded_teams_list:
            if home_team == away_team:
                pass #dont simulate a team playing against each other
            else:
                play_match(home_team,away_team,False)

def uefa_playoffs():
    print("Running UEFA Playoff Rounds...")
    #Takes list of 16 teams into 4 playoffs. Return list of 4 Teams.
    pass

seeded_teams_list = ['Spain', 'Portugal', 'Germany',
                     'France', 'Italy', 'Netherlands',
                     'Croatia', 'Denmark', 'England',
                     'Belgium','Austria','Switzerland'] # Must contain 12 Teams
unseeded_teams_list = []

uefa_make_draw(seeded_teams_list, unseeded_teams_list)
uefa_first_round()
uefa_playoffs()