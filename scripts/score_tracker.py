# scripts/score_tracker.py

class ScoreTracker:
    def __init__(self):
        self.total_score = 0
        self.history = []  # A list to record every point change

    def add_score(self, amount):
        self.total_score += amount
        self.history.append(amount)
        
        # 2. Append 'amount' to the self.history list
        
        print(f"💰 Score Update: {amount} | Total: {self.total_score}")

    def get_final_report(self):
        print("\n--- FINAL MISSION REPORT ---")
        print(f"Total Stardust Collected: {self.total_score}")
        print(f"Number of successful hits: {len(self.history)}")