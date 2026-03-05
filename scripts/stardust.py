# scripts/stardust.py
from star import Star, BlackHole, Supernova

# This list simulates a "level" in your game
galaxy = [
    Star("Gold", 100),
    BlackHole(),
    Supernova("Neon Pink")
]

for obj in galaxy:
    print(f"\nApproaching {obj.color} object...")
    
    # Let the object decide if the strike was successful
    if obj.strike("Gold"):
        # If it's a supernova, do the special effect
        if isinstance(obj, Supernova):
            obj.explode()
        
        # All successful strikes (Stars & Supernovas) release dust
        obj.spread_dust(15)
    else:
        print("Distance maintained. Score safe.")

from star import Star, Supernova, BlackHole
from score_tracker import ScoreTracker  # <--- 1. Import the accountant

# 2. Initialize the tracker
tracker = ScoreTracker()

galaxy = [Star("Gold"), Supernova("Cyan"), BlackHole("Red"), Star("Gold")]

for obj in galaxy:
    print(f"\nApproaching {obj.color} object...")
    
    if obj.strike("Gold"):
        if isinstance(obj, Supernova):
            obj.explode()
        
        obj.spread_dust(15)
        
        # 3. RECORD THE POINTS!
        tracker.add_score(10) # We'll start with 10 points per hit
    else:
        print("Distance maintained. Score safe.")

# 4. Show the final mission report
tracker.get_final_report()