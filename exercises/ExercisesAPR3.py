# =========================================================
# PYTHON EXERCISES - LISTS, METHODS, AND CLASSES
# =========================================================

print("--- EXERCISE 1: INVENTORY CHECK ---")
inventory_1 = ["Medkit", "Plasma Grenade", "Rations"]
chest_loot = "Plasma Grenade"

print(f"Current Inventory: {inventory_1}")
print(f"You opened a chest and found a {chest_loot}!")

# Check if item exists before adding
if chest_loot in inventory_1:
    print("You already have this item")
else:
    inventory_1.append(chest_loot)

print(f"Final Inventory: {inventory_1}\n")


print("--- EXERCISE 2: USING AN ITEM ---")
inventory_2 = ["Medkit", "Plasma Grenade", "Rations", "Medkit"]
print(f"Starting Inventory: {inventory_2}")
print("You took 20 damage! You need to use a Medkit.")

# Remove exactly one instance of an item
inventory_2.remove("Medkit")

print(f"Remaining Inventory: {inventory_2}\n")


print("--- EXERCISE 3: COUNTING ITEMS ---")
ammo_pouch = ["Laser Cell", "Plasma Shell", "Laser Cell", "Laser Cell", "Missile"]
print(f"Current Pouch: {ammo_pouch}")

# Count specific items in a list
laser_count = ammo_pouch.count("Laser Cell")

print(f"You have {laser_count} Laser Cells remaining.\n")


print("--- EXERCISE 4: HIGH SCORES ---")
scores = [450, 920, 150, 780, 500]
print(f"Unordered Scores: {scores}")

# Sort the list in descending order
scores.sort(reverse=True)

print(f"Ranked Scores: {scores}\n")


print("--- EXERCISE 5: DRAWING THE TOP CARD ---")
action_deck = ["Defend", "Heal", "Strike", "Dodge"]
print(f"Deck before drawing: {action_deck}")

# Remove and return the last item in a list
drawn_card = action_deck.pop()

print(f"You drew: {drawn_card}")
print(f"Remaining Deck: {action_deck}\n")


print("--- EXERCISE 6: INVENTORY SIZE ---")
backpack = ["Rations", "Water", "Flares", "Rope", "Compass", "Map"]
print(f"Items in backpack: {backpack}")

# Check the total length/size of a list
item_total = len(backpack)

print(f"You are carrying {item_total} items.\n")


print("--- EXERCISE 7: CLASSES & INSTANTIATION ---")
# Define a template for Asteroids
class Asteroid:
    def __init__(self, size, speed):
        self.size = size
        self.speed = speed

    def show_stats(self):
        print(f"Asteroid Stats -> Size: {self.size} | Speed: {self.speed}")

print("Asteroid Class defined!")

# Create a specific asteroid object
incoming_asteroid = Asteroid("Massive", 120)
incoming_asteroid.show_stats()
print("\nSimulation Complete.")