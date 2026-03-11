
import random

class Star:
    def __init__(self, color, points=100):
        self.color = color
        self.points = points


    def get_reward(self):
        return self.points

    def strike(self, hand_color):
        if hand_color == self.color:
            return True
        else:
            return False

    def spread_dust(self, velocity):
        particles = velocity * 10
        print(f"✨ Success! You released {particles} stardust particles! ✨")
        return particles


class BlackHole(Star):
    def __init__(self,color = "Void"):        # All black holes are 'Void' color and take away 500 points
        super().__init__("Void", -500)

    def strike(self, hand_color):
        # You can't match a black hole! Any contact is a penalty.
        print("⚠️ CRITICAL ERROR: Absorbed by the Void! ⚠️")
        return False
    
class Supernova(Star):
    def __init__(self, color):
        # We pass the color in, but hardcode the 1000 points
        super().__init__(color, 1000)

    def explode(self):
        print(f"💥 SUPERNOVA EXPLOSION! {self.color} dust everywhere! 💥")


def generate_galaxy(size=10, current_score=0):
    new_galaxy = []
    colors = ["Gold", "Cyan", "Red", "Emerald", "Violet"]

    # Calculate "Danger Level"
    # Every 200 points, we'll increase the chance of a Black Hole by 5%
    danger_bonus = current_score // 200 * 5 
    
    # We'll cap the danger so it's never 100% Black Holes (that's no fun!)
    black_hole_threshold = min(10 + danger_bonus, 40) 

    for _ in range(size):
        roll = random.randint(1, 100)
        color = random.choice(colors)

        # The higher the score, the easier it is to roll into the Black Hole bucket
        if roll <= black_hole_threshold:
            new_galaxy.append(BlackHole(color))
        elif roll <= black_hole_threshold + 20:
            new_galaxy.append(Supernova(color))
        else:
            new_galaxy.append(Star(color))
            
    return new_galaxy

    

