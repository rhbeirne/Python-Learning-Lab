class Star:
    def __init__(self, color, points):
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


# --- Testing the Logic ---
# Create a Gold Star
my_star = Star("Gold", 100)

# Simulate a hit
player_hand = "Gold"
if my_star.strike(player_hand):
    my_star.spread_dust(velocity=15)
else:
    print("Missed the rhythm!")