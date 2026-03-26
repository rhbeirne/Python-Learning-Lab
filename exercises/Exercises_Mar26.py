#Exercises

# ---------------------------------------------------------
# PYTHON PRO TECHNIQUES: LAMBDAS & COMPREHENSIONS
# Practice Session - Exercises from Today
# ---------------------------------------------------------

# --- SECTION 1: BASIC LAMBDAS ---

# 1. Squaring a number
square = lambda n: n * n
print(f"Square of 5: {square(5)}")

# 2. Multi-variable: Total Weight
total_weight = lambda body, armor: body + armor
print(f"Total Weight: {total_weight(150, 45)}")

# 3. Logic: Status Check (Ternary Operator)
check_status = lambda hp: "Active" if hp > 0 else "Defeated"
print(f"Status (HP 10): {check_status(10)}")

# 4. Mana Check Logic
use_spell = lambda cost, current: "Spell Cast!" if current >= cost else "Out of Mana!"
print(f"Mana Check (Cost 50, Have 30): {use_spell(50, 30)}")


# --- SECTION 2: FILTER, MAP, & SORT ---

weights = [15, 50, 5, 20, 100]
prices = [10, 20, 30, 40]
shop_items = [
    {"item": "Potion", "price": 50},
    {"item": "Sword", "price": 150},
    {"item": "Bread", "price": 5}
]

# 5. Filtering: Finding heavy items (> 30)
heavy_items = list(filter(lambda w: w > 30, weights))
print(f"Heavy Items: {heavy_items}")

# 6. Mapping: Adding a flat tax (+ 5)
flat_tax = list(map(lambda p: p + 5, prices))
print(f"Taxed Prices: {flat_tax}")

# 7. Sorting: Cheapest items first
sorted_price = sorted(shop_items, key=lambda i: i["price"])
print(f"Sorted Shop: {sorted_price}")


# --- SECTION 3: LIST COMPREHENSIONS ---

base_damages = [5, 10, 15]
xp_rewards = [10, 150, 20, 300, 45]

# 8. Basic Transformation: Double damage
boosted_damages = [x * 2 for x in base_damages]
print(f"Boosted Damages: {boosted_damages}")

# 9. Comprehension with Filter: High XP only (> 100)
major_rewards = [xp for xp in xp_rewards if xp > 100]
print(f"Major Rewards: {major_rewards}")


# --- SECTION 4: PRACTICAL APPLICATION (STAR CLASS) ---
# Using what we learned to analyze complex objects in the "Galaxy" code.

# (Assuming my_galaxy is a list of Star objects)
# void_stars = [s for s in my_galaxy if s.color == "Void"]
# all_points = [s.points for s in my_galaxy]

print("\nAll exercises completed successfully.")