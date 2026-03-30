# RPG exercises
import random


class Player:
    def __init__(self, name, health=100):

        self.name = name
        self.health = health
        self.level = 1
        self.max_health = 100
        self.inventory = []

    def pick_up_item(self, item_name):
        self.inventory.append(item_name)    

    def use_item(self, item_name):
        if item_name in self.inventory:
            self.inventory.remove(item_name)
            return f"{item_name} used!"
        else:
            return f"{item_name} not found in inventory."

    def show_inventory(self):
        return self.inventory


    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
    
    def heal(self, amount):
        self.health += amount
        
        if self.health > self.max_health:
            self.health = self.max_health
    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    def gain_experience(self, amount):
        if amount >= 100:
            self.gain_level()
            return f"{self.name} gained {amount} experience and leveled up!"
        else:
            return f"{self.name} gained {amount} experience."
    
    def gain_level(self):
        self.level += 1
        self.max_health += 20
        return f"{self.name} level up! You are now level {self.level}. Your max health is now {self.max_health}."
    
    def attack(self, target):
        roll = random.randint(1, 10)
        print(roll)
        self.gain_experience(50)
        if roll == 10:
            damage = 20 * self.level
            target.take_damage(damage)
            return f"{self.name} crits {target.name} for {damage} damage!"
        else:
            damage = 10 * self.level
            target.take_damage(damage)
            return f"{self.name} attacks {target.name} for {damage} damage!"
    

class Mage(Player):
    def __init__(self, name):
        super().__init__(name)
        self.mana = 50
    def cast_spell(self, target):
        self.mana -= 10
        target.take_damage(40)
        return f"{self.name} casts a fireball at {target.name} for 40 damage!" 
    def take_damage(self, amount):
        return super().take_damage(amount) 
    def show_inventory(self):
        return f"Your inventory contains: {super().show_inventory()} and your mana is {self.mana}."
       

class chest:
    def __init__(self):
        self.item = "Gold Sword"
        self.is_open = False

    def open(self, opener):
        if not self.is_open:
            self.is_open = True
            opener.pick_up_item(self.item)
            return f"{opener.name} opens the chest and finds a {self.item}!"
        else:
            return "The chest is already open."
        
    
    
    


    
party_leader = Player ( input("Enter the name of the party leader: "))

p1 = Player("Alice")
p2 = Player("Bob")
m3 = Mage("Gandalf")

print(f"Welcome, {party_leader.name}! Your adventure begins now.")
print(f"{party_leader.name} has {party_leader.health} health and is at level {party_leader.level}.")
target = input("Who would you like to attack? ")

if target.lower() == "alice":
    print(party_leader.attack(p1))
elif target.lower() == "bob":
    print(party_leader.attack(p2))
elif target.lower() == "gandalf":
    print(party_leader.attack(m3))
else:
    print("Invalid target.")    


print(party_leader.gain_level())
print(party_leader.level, party_leader.max_health)  # 2, 120
p1.attack(m3)
print(m3.health, m3.name)  # 60
p1.attack(p2)
print(p2.health, p2.name)  # 30

chest1 = chest()
print(chest1.open(p1))  # "Alice opens the chest and finds a Gold Sword!"
print(p1.show_inventory())  # ["Gold Sword"]

print(chest1.open(p1))  # "Alice opens the chest and finds a Gold Sword!"

print(f"{party_leader.attack(p1)} and then {party_leader.attack(p2)}")  # "Party leader attacks Alice for 10 damage!" "Party leader attacks Bob for 10 damage!"

print(p1.name, p1.health, p2.name, p2.health)  # 110

print(party_leader.gain_experience(150))  # "Party leader gained 150 experience and leveled up!"
print(f"{party_leader.name} is now level {party_leader.level} with {party_leader.max_health} max health.")  # 3,


import random
import math

"""
Project: RPG Logic Core v1.0
Author: Richard
Description: A collection of core mechanics for inventory management, 
combat calculations, and environment requirements.
"""

# --- 1. Character & Environment Setup ---
player_name = "evander"
formatted_name = player_name.capitalize()
level = 12
has_key = False
inventory = ["Sword", "Shield", "Potion", "Fire Shield"]

# --- 2. Requirements Check (The Dragon Lair) ---
# Check for both Level and specific Item requirements
if level >= 10 and "Fire Shield" in inventory:
    print(f"Welcome, {formatted_name}. You may enter the Lair!")
else:
    print("The heat is too intense. You are not prepared.")

# --- 3. Combat & Damage Logic ---
# Generate a random damage roll between 15 and 25
base_damage = random.randint(15, 25)
critical_multiplier = 1.5

# Calculate crit and use math.floor to round down to a whole number
total_damage = math.floor(base_damage * critical_multiplier)
print(f"CRITICAL HIT! You dealt {total_damage} damage.")

# --- 4. Health & Overheal Management ---
health = 45
max_health = 100
potion_heal = 60

# Use min() to ensure health never exceeds the cap
health = min(health + potion_heal, max_health)
print(f"Health restored to: {health}/{max_health}")

# --- 5. Inventory Management ---
# Check if inventory is full (Limit: 5)
if len(inventory) >= 5:
    print("Inventory Full! Drop an item to make room.")

# Example of swapping items
if "Potion" in inventory:
    inventory.remove("Potion")
    inventory.append("Dragon Egg")
    print(f"Updated Inventory: {inventory}")

# --- 6. Security & Edge Case Handling ---
# Prevent negative gold (The Professional 'Standard')
player_gold = 50
item_price = 100

if player_gold >= item_price:
    player_gold -= item_price
else:
    # Use max() to ensure gold never accidentally drops below 0
    player_gold = max(0, player_gold)
    print("Transaction Cancelled: Insufficient Gold.")


 DAY 3: DATA STRUCTURING & COMBO MOVES
# ---------------------------------------------------------

# ... (Previous Exercises 16-22 kept for reference)

# --- EXERCISE 23: THE CHARACTER MANIFEST (COMBO) ---
crew_data = [
    {"name": "Evander", "role": "Pilot", "rank": 5},
    {"name": "Cassia", "role": "Engineer", "rank": 8},
    {"name": "Grog", "role": "Security", "rank": 3}
]

# SOLUTION: { KEY : (TUPLE_VALUE) for item in list }
crew_manifest = {n["name"]: (n["role"], n["rank"]) for n in crew_data}
print(f"Cassia's Stats: {crew_manifest['Cassia']}") 


# --- EXERCISE 24: THE FINAL BOSS (COMBO + FILTER) ---

raw_intel = [
    {"name": "Evander", "rank": 5, "traitor": False},
    {"name": "Cassia", "rank": 8, "traitor": False},
    {"name": "Mole", "rank": 1, "traitor": True}
]

# THE CORRECTED SOLUTION:
# 1. Use {Key: Value} for a dictionary
# 2. Access the keys correctly (t["name"], t["rank"])
# 3. Filter at the end
loyal_manifest = {t["name"]: t["rank"] for t in raw_intel if t["traitor"] == False}

print(f"Loyal Crew: {loyal_manifest}")
# Output: {'Evander': 5, 'Cassia': 8}


# ---------------------------------------------------------
# MONDAY SUMMARY FOR GITHUB EXPORT
# ---------------------------------------------------------
"""
PRACTICE LOG: MARCH 30, 2026
TOPICS: SETS, DICTIONARIES, TUPLES, AND IMMUTABILITY

1. Exercise 16: Set Comprehensions {item for item in list}
   - Purpose: Automatic duplicate removal.
2. Exercise 17/18: Dictionary Comprehensions {k:v for item in list}
   - Purpose: Quick lookup tables and budget filtering.
3. Exercise 19: Dictionary If-Else Flip
   - Purpose: Tagging data (Elite vs Standard) inside a dictionary.
4. Exercise 20/21/22: Tuples and Immutability
   - Purpose: Locking coordinates and fixed star colors using tuple().
5. Exercise 23/24: Complex Data Structures
   - Purpose: Building manifests that map names to rank/role tuples.
"""

