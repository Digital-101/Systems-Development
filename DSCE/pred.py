
# Soccer Prediction

def get_team_names():
    home_team = input("Enter home team name: ").strip()
    away_team = input("Enter away team name: ").strip()
    return home_team, away_team

def get_team_stats():
    stats = {}
    stats['home_goals'] = int(input("Enter home team's average goals per game: "))
    stats['away_goals'] = int(input("Enter away team's average goals per game: "))
    stats['home_corners'] = int(input("Enter home team's corners: "))
    stats['away_corners'] = int(input("Enter away team's corners: "))
    stats['home_possession'] = int(input("Enter home team's average possession percentage: "))
    stats['away_possession'] = int(input("Enter away team's average possession percentage: "))
    stats['home_shots'] = int(input("Enter home team's shots: "))
    stats['away_shots'] = int(input("Enter away team's shots: "))
    return stats

def choose_statistic():
    choices = {
        1: 'goals',
        2: 'corners',
        3: 'possession',
        4: 'shots'
    }
    print("---Choose a statistic to predict the match result:---")
    for key, value in choices.items():
        print(f"{key}. {value.capitalize()}")
    print("-----------------------------------------------------")
        
    while True:
        try:
            choice = int(input("Enter the number corresponding to your choice: "))
            if choice in choices:
                return choices[choice]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def predict_result(statistic, stats):
    home_stat = stats[f'home_{statistic}']
    away_stat = stats[f'away_{statistic}']
    
    if home_stat > away_stat:
        return "Home Win"
    elif home_stat < away_stat:
        return "Away Win"
    else:
        return "Draw"

def main():
    home_team, away_team = get_team_names()
    stats = get_team_stats()
    while True:
        statistic = choose_statistic()
        result = predict_result(statistic, stats)
        print('Given Stats: ',stats)
        print(f"The predicted result for the match between {home_team} and {away_team} is: {result}")
        useInp = input('Type "stop" to exit the programs and press "Enter" to continue').strip()
        if useInp == 'stop':
            break
main()