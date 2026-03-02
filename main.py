# We tell Python: "Go into the scripts folder and look for the VRPlayer file"
from scripts.VRPlayer import VRPlayer

# Now we use that blueprint to create you as a player
p1 = VRPlayer("Richard")

# Let's test if it's working
print(f"Current Player: {p1.name}")
p1.show_inventory()
