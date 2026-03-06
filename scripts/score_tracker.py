# scripts/score_tracker.py
import json

import json # <--- New import at the top

class ScoreTracker:
    def __init__(self):
        self.total_score = 0
        self.history = []

    def add_score(self, amount):
        self.total_score += amount
        self.history.append(amount)

    def save_to_file(self, filename="highscore.json"):
        # We create a dictionary to hold our data
        save_data = {
            "total_score": self.total_score,
            "history": self.history
        }
        
        # Now we "dump" that dictionary into a file
        with open(filename, "w") as f:
            json.dump(save_data, f)
        print(f"--- Data saved to {filename} ---")
