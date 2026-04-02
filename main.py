
import time
import random

# =========================================================
# FILE 1: vr_core.py
# =========================================================
class VRFlightBrain:
    def __init__(self, player_height=1.7):
        self.baseline_height = player_height
        self.state = {
            "altitude": "Cruising",
            "steering": "Center",
            "left_gun": False,
            "right_gun": False,
            "score": 0,
            "level": 1,
            "speed": 100,
            "weapon_damage": 1,          
            "weapon_spread": 1,           
            "weapon_type": "Single Laser",
            
            # ---> NEW: Pause State <---
            "paused": False,
            "awaiting_choice": False
            # --------------------------
        }

    def process_input(self, head_y, left_y, right_y, left_trigger, right_trigger):
        # ---> NEW: The Pause Menu Logic <---
        # If the game is paused, normal flying/shooting is locked out.
        if self.state["paused"]:
            if self.state["awaiting_choice"]:
                # The triggers now act as "Menu Buttons" instead of guns
                if left_trigger:
                    self.state["weapon_type"] = "Plasma Ball"
                    self.state["weapon_damage"] = 5  # Huge damage!
                    self.state["paused"] = False     # Unpause the game
                    self.state["awaiting_choice"] = False
                    print("\n🔵 UPGRADE CHOSEN: PLASMA BALL! Game Resumed. 🔵")
                elif right_trigger:
                    self.state["weapon_type"] = "Rapid Fire"
                    self.state["weapon_spread"] = 5  # Huge spread/speed!
                    self.state["paused"] = False     # Unpause the game
                    self.state["awaiting_choice"] = False
                    print("\n⚡ UPGRADE CHOSEN: RAPID FIRE! Game Resumed. ⚡")
            
            # We use 'return' to STOP the rest of the function from running
            # so the ship doesn't move or score points while paused.
            return 
        # -----------------------------------

        # 1. Squat Logic
        if head_y < (self.baseline_height - 0.4):
            self.state["altitude"] = "Diving"
        else:
            self.state["altitude"] = "Cruising"

        # 2. Steering Logic
        if left_y > (right_y + 0.2):
            self.state["steering"] = "Turning Right"
        elif right_y > (left_y + 0.2):
            self.state["steering"] = "Turning Left"
        else:
            self.state["steering"] = "Center"

        # 3. Shooting & Scoring Logic
        self.state["left_gun"] = left_trigger
        self.state["right_gun"] = right_trigger

        points_per_shot = 10 * self.state["weapon_damage"] * self.state["weapon_spread"]
        
        if left_trigger:
            self.state["score"] += points_per_shot
        if right_trigger:
            self.state["score"] += points_per_shot

        # 4. RPG Leveling Logic
        if self.state["score"] >= self.state["level"] * 100:
            self.state["level"] += 1
            self.state["speed"] += 50
            
            print(f"\n🌟 LEVEL UP! You are now Level {self.state['level']}! 🌟")

            # Apply specific upgrades based on the new level
            if self.state["level"] == 2:
                self.state["weapon_damage"] = 2
                print("💥 UPGRADE: Weapons now deal DOUBLE DAMAGE! 💥")
            elif self.state["level"] == 3:
                self.state["weapon_type"] = "Spread Shot"
                self.state["weapon_spread"] = 3
                print("☄️ UPGRADE: SPREAD SHOT! You now hit 3 targets at once! ☄️")
            
            # ---> NEW: Level 4 Pause Trigger <---
            elif self.state["level"] == 4:
                self.state["paused"] = True
                self.state["awaiting_choice"] = True
                print("⏸️ LEVEL 4 REACHED! GAME PAUSED. ⏸️")
                print("Shoot LEFT button for Plasma Ball. Shoot RIGHT button for Rapid Fire.")
            # ------------------------------------

    def get_ship_status(self):
        return self.state


# =========================================================
# FILE 2: input_handler.py
# =========================================================
def get_simulated_vr_data():
    """Simulates the data coming from a VR Headset."""
    head_y = random.choice([1.7, 1.2]) 
    left_y = random.uniform(1.0, 1.5)
    right_y = random.uniform(1.0, 1.5)
    
    # Increased chance to shoot so we hit Level 4 faster
    left_trigger = random.choice([True, True, True, False])
    right_trigger = random.choice([True, True, True, False])
    return head_y, left_y, right_y, left_trigger, right_trigger


# =========================================================
# FILE 3: main.py
# =========================================================
print("🚀 Launching VR Flight Simulator...")
brain = VRFlightBrain(player_height=1.7)

active_frames = 30 # Increased so we have time to hit level 4
current_frame = 1

while current_frame <= active_frames:
    print(f"\n--- Frame {current_frame} ---")
    
    h_y, l_y, r_y, l_trig, r_trig = get_simulated_vr_data()
    brain.process_input(h_y, l_y, r_y, l_trig, r_trig)
    ship = brain.get_ship_status()
    
    # ---> NEW: Print Paused Status <---
    if ship["paused"]:
        print("⏸️ [GAME IS PAUSED - WAITING FOR PLAYER CHOICE] ⏸️")
    else:
        print(f"Lvl: {ship['level']} | Score: {ship['score']} | Speed: {ship['speed']}")
        print(f"Weapon: {ship['weapon_type']} (Damage: {ship['weapon_damage']}, Spread: {ship['weapon_spread']})")
        print(f"Altitude: {ship['altitude']} | Steering: {ship['steering']}")
    # ----------------------------------
    
    current_frame += 1
    
    # Reduced sleep time to prevent the web compiler from timing out
    time.sleep(0.1) 

print("\n🛬 Simulation Complete.")