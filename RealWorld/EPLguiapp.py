import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import classification_report, mean_squared_error
from sklearn.model_selection import train_test_split
import tkinter as tk
from tkinter import messagebox, ttk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Sample Data for Initial Training
data = {
    'team': ['Wolves', 'Newcastle', 'Wolves', 'Newcastle', 'Wolves', 'Newcastle'],
    'recent_wins': [0, 2, 0, 0, 1, 0],
    'recent_goals_scored': [5, 4, 4, 5, 4, 6],
    'recent_goals_conceded': [3, 7, 1, 3, 2, 4],
    'opponent_recent_wins': [2, 3, 2, 4, 1, 2],
    'home_away': [1, 0, 1, 0, 1, 0],  # 1 for home, 0 for away
    'team_strength': [-10, 35, 11, 7, 12, 8],  # Simplified metric for team strength
    'match_result': [2, 0, 2, 0, 2, 1],  # 0 = Loss, 1 = Draw, 2 = Win
    'goals_for': [2, 1, 3, 1, 3, 1],
    'goals_against': [0, 2, 1, 3, 2, 4]
}

df = pd.DataFrame(data)

# Feature and target variables
X = df[['recent_wins', 'recent_goals_scored', 'recent_goals_conceded', 'opponent_recent_wins', 'home_away', 'team_strength']]
y = df['match_result']
goals_for = df['goals_for']
goals_against = df['goals_against']

# Train-test split
X_train, X_test, y_train, y_test, goals_for_train, goals_for_test, goals_against_train, goals_against_test = train_test_split(
    X, y, goals_for, goals_against, test_size=0.3, random_state=42)

# Train models
match_model = RandomForestClassifier(n_estimators=100, random_state=42)
match_model.fit(X_train, y_train)

goals_for_model = RandomForestRegressor(n_estimators=100, random_state=42)
goals_for_model.fit(X_train, goals_for_train)

goals_against_model = RandomForestRegressor(n_estimators=100, random_state=42)
goals_against_model.fit(X_train, goals_against_train)

# Evaluate models
y_pred = match_model.predict(X_test)
goals_for_pred = goals_for_model.predict(X_test)
goals_against_pred = goals_against_model.predict(X_test)

print("Match Result Classification Report:")
print(classification_report(y_test, y_pred))

print(f"Goals For Mean Squared Error: {mean_squared_error(goals_for_test, goals_for_pred)}")
print(f"Goals Against Mean Squared Error: {mean_squared_error(goals_against_test, goals_against_pred)}")

# Create the main GUI window
class PredictionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Match Prediction App")

        # Frame for user inputs
        input_frame = ttk.Frame(root, padding="10")
        input_frame.grid(row=0, column=0, sticky="nsew")

        tk.Label(input_frame, text="Select Team:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.team_var = tk.StringVar(value='Wolves')
        self.team_menu = ttk.Combobox(input_frame, textvariable=self.team_var, values=['Wolves', 'Newcastle'])
        self.team_menu.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        tk.Label(input_frame, text="Recent Wins:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.recent_wins_entry = ttk.Entry(input_frame)
        self.recent_wins_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        tk.Label(input_frame, text="Recent Goals Scored:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.recent_goals_scored_entry = ttk.Entry(input_frame)
        self.recent_goals_scored_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        tk.Label(input_frame, text="Recent Goals Conceded:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.recent_goals_conceded_entry = ttk.Entry(input_frame)
        self.recent_goals_conceded_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        tk.Label(input_frame, text="Opponent Recent Wins:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.opponent_recent_wins_entry = ttk.Entry(input_frame)
        self.opponent_recent_wins_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

        tk.Label(input_frame, text="Home/Away (1 for Home, 0 for Away):").grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.home_away_entry = ttk.Entry(input_frame)
        self.home_away_entry.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

        ttk.Button(input_frame, text="Predict Match Result & Goals", command=self.make_prediction).grid(row=6, column=0, columnspan=2, pady=10)

        # Frame for history and visualization
        history_frame = ttk.Frame(root, padding="10")
        history_frame.grid(row=1, column=0, sticky="nsew")

        # History DataFrame
        self.history = pd.DataFrame(columns=['Team', 'Recent Wins', 'Goals Scored', 'Goals Conceded', 'Opponent Wins', 'Home/Away', 'Prediction', 'Goals For', 'Goals Against'])

        # Display history
        self.history_tree = ttk.Treeview(history_frame, columns=('Team', 'Recent Wins', 'Goals Scored', 'Goals Conceded', 'Opponent Wins', 'Home/Away', 'Prediction', 'Goals For', 'Goals Against'), show='headings')
        self.history_tree.grid(row=0, column=0, sticky="nsew")

        for col in self.history_tree['columns']:
            self.history_tree.heading(col, text=col)

        # Add a scrollbar
        self.scrollbar = ttk.Scrollbar(history_frame, orient=tk.VERTICAL, command=self.history_tree.yview)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.history_tree.configure(yscrollcommand=self.scrollbar.set)

        # Placeholder for visualizations
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=history_frame)
        self.canvas.get_tk_widget().grid(row=1, column=0, sticky="nsew")
        self.canvas.draw()

        # Configure row and column weights for resizing
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        history_frame.grid_rowconfigure(0, weight=1)
        history_frame.grid_rowconfigure(1, weight=2)  # Make the plot area expandable
        history_frame.grid_columnconfigure(0, weight=1)

    def make_prediction(self):
        try:
            team = self.team_var.get()
            recent_wins = int(self.recent_wins_entry.get())
            recent_goals_scored = int(self.recent_goals_scored_entry.get())
            recent_goals_conceded = int(self.recent_goals_conceded_entry.get())
            opponent_recent_wins = int(self.opponent_recent_wins_entry.get())
            home_away = int(self.home_away_entry.get())

            # Prepare data for prediction
            new_data = pd.DataFrame({
                'recent_wins': [recent_wins],
                'recent_goals_scored': [recent_goals_scored],
                'recent_goals_conceded': [recent_goals_conceded],
                'opponent_recent_wins': [opponent_recent_wins],
                'home_away': [home_away],
                'team_strength': [recent_wins * 1.5 + recent_goals_scored - recent_goals_conceded]
            })

            # Predict match result
            result = match_model.predict(new_data)
            prediction_classes = ['Loss', 'Draw', 'Win']
            match_result = prediction_classes[result[0]]

            # Predict goals for and against
            goals_for_prediction = goals_for_model.predict(new_data)[0]
            goals_against_prediction = goals_against_model.predict(new_data)[0]

            # Record the prediction
            new_entry = pd.DataFrame({
                'Team': [team],
                'Recent Wins': [recent_wins],
                'Goals Scored': [recent_goals_scored],
                'Goals Conceded': [recent_goals_conceded],
                'Opponent Wins': [opponent_recent_wins],
                'Home/Away': [home_away],
                'Prediction': [match_result],
                'Goals For': [goals_for_prediction],
                'Goals Against': [goals_against_prediction]
            })

            self.history = pd.concat([self.history, new_entry], ignore_index=True)

            # Update the history treeview
            self.update_history_tree()

            # Visualization
            self.visualize_predictions()

            messagebox.showinfo("Prediction Result", f"Prediction for {team}: {match_result}\nGoals For: {goals_for_prediction:.2f}\nGoals Against: {goals_against_prediction:.2f}")

        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")

    def update_history_tree(self):
        # Clear the treeview
        self.history_tree.delete(*self.history_tree.get_children())

        # Insert updated history
        for _, row in self.history.iterrows():
            self.history_tree.insert('', 'end', values=row.tolist())

    def visualize_predictions(self):
        self.ax.clear()

        # Plot true vs predicted results
        indices = list(range(len(y_test)))
        self.ax.plot(indices, y_test.values, 'bo', label='True Results')
        self.ax.plot(indices, y_pred, 'r*', label='Predicted Results')

        # Set axis labels and title
        self.ax.set_title('True vs Predicted Results')
        self.ax.set_xlabel('Sample Index')
        self.ax.set_ylabel('Match Result')
        self.ax.legend()
        self.ax.grid(True)

        self.canvas.draw()

# Create and run the application
root = tk.Tk()
app = PredictionApp(root)
root.mainloop()
