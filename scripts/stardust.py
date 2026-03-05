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