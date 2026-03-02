from scripts.VRPlayer import VRPlayer

class Boss(VRPlayer):
    def __init__(self, name, position, health, power_level):
        # 1. Pass the name, position, and health up to the VRPlayer setup
        super().__init__(name, position, health)
        
        # 2. Set the unique Boss trait
        self.power_level = power_level
        print(f"Boss {self.name} has entered with {self.health} HP and Power Level {self.power_level}!")