#March27

# ---------------------------------------------------------
# PYTHON PRO TECHNIQUES: DAY 2
# Dictionary Access, Filtering, and the If-Else Flip
# ---------------------------------------------------------

# --- EXERCISE 10: THE INVENTORY FILTER ---
# Filtering names from a list of dictionaries based on durability.
cache = [
    {"name": "Stinger Pistol", "durability": 50},
    {"name": "Rusted Pipe", "durability": 0},
    {"name": "Combat Vest", "durability": 100},
    {"name": "Empty Canteen", "durability": 0}
]

usable_items = [u["name"] for u in cache if u["durability"] > 0]
print(f"Usable Items: {usable_items}")


# --- EXERCISE 11: REPETITION ROUND ---
# Extracting IDs for high-charge energy cells.
cells = [
    {"id": "A1", "charge": 95},
    {"id": "B2", "charge": 40},
    {"id": "C3", "charge": 88},
    {"id": "D4", "charge": 10}
]

high_charge_ids = [c["id"] for c in cells if c["charge"] > 80]
print(f"High Charge IDs: {high_charge_ids}")


# --- EXERCISE 12: STATUS SCANNER ---
# Simple string matching filter.
drones = [
    {"name": "Seeker-1", "status": "Online"},
    {"name": "Seeker-2", "status": "Offline"},
    {"name": "Ghost-Alpha", "status": "Online"},
    {"name": "Ghost-Beta", "status": "Damaged"}
]

active_drones = [d["name"] for d in drones if d["status"] == "Online"]
print(f"Active Drones: {active_drones}")


# --- EXERCISE 13: THE LOOT CATEGORIZER ---
# Mastering the "If-Else Flip" (Logic moves to the front).
gold_piles = [5, 120, 30, 500, 15]
pile_labels = ["Hoard" if g > 50 else "Scrap" for g in gold_piles]
print(f"Loot Labels: {pile_labels}")


# --- EXERCISE 14: SPEED ROUND ---
# Quick logic check for engine temperatures.
core_temps = [80, 115, 90, 150]
core_status = ["Overheating" if c > 100 else "Stable" for c in core_temps]
print(f"Core Status: {core_status}")


# --- EXERCISE 15: THE XP MULTIPLIER (BOSS LEVEL) ---
# Combining dictionary access, math, and the If-Else Flip.
missions = [
    {"task": "Scavenge", "base_xp": 100, "bonus": True},
    {"task": "Scout", "base_xp": 50, "bonus": False},
    {"task": "Repair", "base_xp": 200, "bonus": True}
]

final_xp_totals = [m["base_xp"] * 2 if m["bonus"] else m["base_xp"] for m in missions]
print(f"Final XP Totals: {final_xp_totals}")
