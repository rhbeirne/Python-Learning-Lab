# scripts/score_tracker.py
import json

class ScoreTracker:
    def __init__(self):
        self.total_score = 0
        self.history = []

    def add_score(self, amount):
        self.total_score += amount
        self.history.append(amount)

    def save_to_file(self, filename="highscore.json"):
        save_data = {
            "total_score": self.total_score,
            "history": self.history
        }
        with open(filename, "w") as f:
            json.dump(save_data, f)
        print(f"--- Data saved to {filename} ---")

    def load_from_file(self, filename="highscore.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.total_score = data["total_score"]
                self.history = data["history"]
            print(f"--- Welcome Back! Loaded score: {self.total_score} ---")
        except FileNotFoundError:
            print("--- No save file found. Starting fresh! ---")

    def get_final_report(self):
        print(f"Final Score: {self.total_score}")
        print(f"History: {self.history}")