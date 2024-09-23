import pandas as pd

# Example data
data = {
    'team': ['Wolves', 'Newcastle'],
    'recent_wins': [0, 2],
    'recent_goals_scored': [5, 4],
    'recent_goals_conceded': [7, 3]
}

df = pd.DataFrame(data)

# Function to calculate team strength
def calculate_team_strength(recent_wins, recent_goals_scored, recent_goals_conceded):
    return ((recent_wins * 1.5) + (recent_goals_scored - recent_goals_conceded) * 0.5) * 10

# Apply the function to the dataframe
df['team_strength'] = df.apply(
    lambda row: calculate_team_strength(row['recent_wins'], row['recent_goals_scored'], row['recent_goals_conceded']),
    axis=1
)

print(df)
