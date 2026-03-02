from scripts.VRPlayer import VRPlayer

class Boss(VRPlayer):
    def __init__(self, name, power_level):
        # Run the standard Player setup
        super().__init__(name) 
        # Add the unique Boss traits
        self.power_level = power_level
        self.health = 500
        print(f"Boss {self.name} has entered the game with {self.health} HP!")