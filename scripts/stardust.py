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
    
    # If it's a regular strike (or supernova strike)
    if obj.strike("Gold") or isinstance(obj, Supernova):
        if isinstance(obj, Supernova):
            obj.explode()
        else:
            obj.spread_dust(15)
    else:
        print("Distance maintained. Score safe.")