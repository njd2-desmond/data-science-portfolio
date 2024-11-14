import random

# Define constants for scoring
TRY_POINTS = 5
CONVERSION_POINTS = 2
PENALTY_POINTS = 3
DROP_GOAL_POINTS = 3

# Define the length of the match
MATCH_DURATION = 80  # 80 minutes for a rugby union match
HALF_DURATION = 40   # Each half is 40 minutes

# Function to simulate a rugby match event
def simulate_event():
    event = random.choice(['try', 'penalty', 'drop_goal', 'conversion', 'miss'])
    return event

# Function to simulate a try being scored (and the possibility of a conversion)
def score_try():
    try_scored = True
    # Simulate whether the conversion is successful (e.g., 75% chance of success)
    conversion_successful = random.random() < 0.75
    return TRY_POINTS + (CONVERSION_POINTS if conversion_successful else 0)

# Function to simulate a penalty
def score_penalty():
    return PENALTY_POINTS

# Function to simulate a drop goal
def score_drop_goal():
    return DROP_GOAL_POINTS

# Function to simulate an entire game
def simulate_match():
    # Scores for both teams
    team1_score = 0
    team2_score = 0

    # Track possession and game progress
    current_time = 0
    team_with_possession = random.choice([1, 2])  # Randomly start with either team

    while current_time < MATCH_DURATION:
        event = simulate_event()
        
        if event == 'try':
            if team_with_possession == 1:
                team1_score += score_try()
            else:
                team2_score += score_try()
        elif event == 'penalty':
            if team_with_possession == 1:
                team1_score += score_penalty()
            else:
                team2_score += score_penalty()
        elif event == 'drop_goal':
            if team_with_possession == 1:
                team1_score += score_drop_goal()
            else:
                team2_score += score_drop_goal()
        # "conversion" event doesn't occur unless a try is scored, so it's handled within the try scoring function.
        
        # Randomly decide whether possession switches (just a simple random factor here for simplicity)
        if random.random() < 0.1:  # 10% chance possession switches
            team_with_possession = 3 - team_with_possession  # Switch between team 1 and team 2
        
        # Increment time by 1 minute per event for simplicity
        current_time += 1

    return team1_score, team2_score

# Function to run the simulation
def rugby_simulation():
    print("Welcome to Twickenham for todays Test between England and Australia...\n")
    
    # Simulate the match
    team1_score, team2_score = simulate_match()
    
    # Display results
    print(f"Final Score:")
    print(f"Team 1: {team1_score} - Team 2: {team2_score}")
    
    # Determine the winner
    if team1_score > team2_score:
        print("\nTeam 1 wins!")
    elif team2_score > team1_score:
        print("\nTeam 2 wins!")
    else:
        print("\nIt's a draw!")

# Run the simulation
rugby_simulation()
