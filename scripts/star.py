
import random

class Star:
    def __init__(self, color, points=100):
        self.color = color
        self.points = points

    def strike(self, hand_color):
        if hand_color == self.color:
            return True
        else:
            return False

    def spread_dust(self, velocity):
        particles = velocity * 10
        print(f"✨ Success! You released {particles} stardust particles! ✨")


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


def generate_galaxy(size=10):
    new_galaxy = []
    colors = ["Gold", "Cyan", "Red", "Emerald", "Violet"]

    for _ in range(size):
        roll = random.randint(1, 100) # Our 1-100 "dice"
        color = random.choice(colors)

        if roll <= 70:
            # 70% chance
            new_galaxy.append(Star(color))
        elif roll <= 90:
            # 20% chance (71 to 90)
            new_galaxy.append(Supernova(color))
        else:
            # 10% chance (91 to 100)
            new_galaxy.append(BlackHole(color))
            
    return new_galaxy

    

