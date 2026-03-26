#Star.py

import random

class Star:
    def __init__(self, color, points=100):
        self.color = color
        self.points = points

    def get_reward(self):
        return self.points

    def strike(self, hand_color):
        return hand_color == self.color

    def spread_dust(self, velocity):
        particles = velocity * 10
        print(f"✨ Success! You released {particles} stardust particles! ✨")
        return particles

class BlackHole(Star):
    def __init__(self, color="Void"):
        super().__init__("Void", -500)

    def strike(self, hand_color):
        print("⚠️ CRITICAL ERROR: Absorbed by the Void! ⚠️")
        return False
    
class Supernova(Star):
    def __init__(self, color):
        super().__init__(color, 1000)

    def explode(self):
        print(f"💥 SUPERNOVA EXPLOSION! {self.color} dust everywhere! 💥")

def generate_galaxy(size=10, current_score=0):
    new_galaxy = []
    colors = ["Gold", "Cyan", "Red", "Emerald", "Violet"]
    danger_bonus = current_score // 200 * 5 
    black_hole_threshold = min(10 + danger_bonus, 40) 

    for _ in range(size):
        roll = random.randint(1, 100)
        color = random.choice(colors)

        if roll <= black_hole_threshold:
            new_galaxy.append(BlackHole(color))
        elif roll <= black_hole_threshold + 20:
            new_galaxy.append(Supernova(color))
        else:
            new_galaxy.append(Star(color))
            
    return new_galaxy

# --- PRO ANALYSIS SECTION ---

# 1. Generate a galaxy
my_galaxy = generate_galaxy(size=15, current_score=500)

# 2. Use a List Comprehension to find all Black Holes (Filtering)
# "Give me the star if its color is 'Void'"
void_stars = [s for s in my_galaxy if s.color == "Void"]

# 3. Use a List Comprehension to get a list of all point values (Mapping/Transforming)
# "Give me the points for every star in the galaxy"
all_points = [s.points for s in my_galaxy]

print(f"Galaxy generated with {len(void_stars)} black holes.")
