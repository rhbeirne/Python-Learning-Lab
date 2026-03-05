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
    def __init__(self):
        # All black holes are 'Void' color and take away 500 points
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

    

