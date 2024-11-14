import random
from scipy.stats import poisson

MAX_OVERS = 50
BALLS_PER_OVER = 6
RUNS_PER_BALL = [0, 1, 2, 3, 4, 5, 6,"OUT"]
RUN_OUTCOMES = [0.30, 0.40, 0.10, 0.01, 0.10, 0.01, 0.05, 0.03]
WICKET_PROBABILITY = 0.03
TEAMS = ['Afghanistan', 'Australia','Bangladesh','England','India','New Zealand','Pakistan','South Africa','Sri Lanka','West Indies',
         'Ireland', 'Scotland', 'Zimbabwe', 'Netherlands', 'Canada', 'Oman', 'USA', 'Nepal', 'Namibia', 'UAE']

def choose_teams(TEAMS):
    HOME_TEAM = random.choice(TEAMS)
    TEAMS.remove(HOME_TEAM)
    AWAY_TEAM = random.choice(TEAMS)
    print("Simulating",HOME_TEAM,"vs",AWAY_TEAM)
    print("----------------------")
    return HOME_TEAM,AWAY_TEAM

def the_toss(HOME_TEAM, AWAY_TEAM):
    coin_toss = random.choice([HOME_TEAM,AWAY_TEAM])
    bowl_bat_choice = random.choice(['Bat','Bowl'])
    print(f"{coin_toss} have won the the toss.")
    if coin_toss == HOME_TEAM and bowl_bat_choice == 'Bat':
        bowling_team = AWAY_TEAM
        batting_team = HOME_TEAM
    elif coin_toss == HOME_TEAM and bowl_bat_choice == 'Bowl':
        bowling_team = HOME_TEAM
        batting_team = AWAY_TEAM
    elif coin_toss == AWAY_TEAM and bowl_bat_choice == 'Bat':
        bowling_team = HOME_TEAM
        batting_team = AWAY_TEAM
    elif coin_toss == AWAY_TEAM and bowl_bat_choice == 'Bowl':
        bowling_team = AWAY_TEAM
        batting_team = HOME_TEAM
    return batting_team,bowling_team

def bowl_ball():
    outcome = random.choices(RUNS_PER_BALL,RUN_OUTCOMES)[0]
    return outcome

def the_set(team_to_set,team_to_chase):
    print(f"First Innings. {team_to_chase} to bowl to {team_to_set}")
    runs = 0
    wickets = 0
    overs = 0
    while wickets < 10 and overs <= MAX_OVERS:
        balls = 1
        over_list = []
        while balls <= BALLS_PER_OVER:
            result = bowl_ball() #Bowl the ball...
            if result == "OUT":
                wickets += 1
                over_list.append(result)
            else:
                runs = runs + result
                over_list.append(result)
            balls += 1
        #print(f"{overs}  {over_list}")
        overs += 1
    return runs, wickets

def the_chase(team_to_bat,team_to_bowl,score_to_match):
    print(f"Second Innings. {team_to_bowl} to bowl to {team_to_bat}. {team_to_bat} require {score_to_match}")
    runs = 0
    wickets = 0
    overs = 0
    caught = False
    while wickets < 10 and overs <= MAX_OVERS:
        balls = 1
        over_list = []
        while balls <= BALLS_PER_OVER and score_to_match > runs:
            result = bowl_ball() #Bowl the ball...
            if result == "OUT":
                wickets += 1
                over_list.append(result)
            else:
                runs = runs + result
                over_list.append(result)
            balls += 1
        #print(f"{overs}  {over_list}")
        overs += 1
    return runs, wickets

def play_the_game(HOME_TEAM, AWAY_TEAM):
    team_to_set,team_to_chase = the_toss(HOME_TEAM, AWAY_TEAM)
    print(f"{team_to_set} will bat first, {team_to_chase} will chase.")
    print("----------------------")
    team1_runs, team1_wickets = the_set(team_to_set,team_to_chase)
    print(f"{team_to_set} scored {team1_runs}-{team1_wickets}")
    print("----------------------")
    team2_runs, team2_wickets = the_chase(team_to_chase,team_to_set,team1_runs+1)
    print(f"{team_to_chase} scored {team2_runs}-{team2_wickets}")
    print("----------------------")
    print(f"{team_to_set } {team1_runs}-{team1_wickets} : {team_to_chase} {team2_runs}-{team2_wickets}")
    print("----------------------")
    if team1_runs > team2_runs:
        print(f"{team_to_set} wins by {team1_runs - team2_runs} runs")
    elif team2_runs >= team1_runs:
        print(f"{team_to_chase} wins by {10 - team2_wickets} wickets")

HOME_TEAM, AWAY_TEAM = choose_teams(TEAMS)
play_the_game(HOME_TEAM, AWAY_TEAM)