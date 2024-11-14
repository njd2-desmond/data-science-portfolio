import random
from scipy.stats import poisson

MAX_OVERS = 50
BALLS_PER_OVER = 6
RUNS_PER_BALL = [0,1,2,4]
WICKET_PROBABILITY = 0.025
TEAMS = ['Afghanistan', 'Australia','Bangladesh','England','India','New Zealand','Pakistan','South Africa','Sri Lanka','West Indies']
HOME_TEAM = random.choice(TEAMS)
TEAMS.remove(HOME_TEAM)
AWAY_TEAM = random.choice(TEAMS)
print(HOME_TEAM,"vs",AWAY_TEAM)
print("----------------------")
def bowl_ball():
    if random.random() < WICKET_PROBABILITY:
        return "OUT"
    else:
        return random.choice(RUNS_PER_BALL)
    
def play_innings():
    runs = 0
    wickets = 0
    balls = 0
    while balls < (MAX_OVERS*BALLS_PER_OVER) and wickets < 10:
        result = bowl_ball()
        balls+=1
        if result == "OUT":
            wickets += 1
        else:
            runs += result
    return runs, wickets, balls

def simulate_match():
    team1_runs, team1_wickets , team1_balls= play_innings()
    print(f"{HOME_TEAM} finished {team1_runs}-{team1_wickets} after {int(team1_balls/6)} overs")
    print(f"{AWAY_TEAM} to chase, require {team1_runs+1}")
    team2_runs, team2_wickets , team2_balls= play_innings()
    print(f"{AWAY_TEAM} finished {team2_runs}-{team2_wickets} after {int(team2_balls/6)} overs")

simulate_match()