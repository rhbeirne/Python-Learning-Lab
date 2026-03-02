import numpy as np

class VRPlayer:
    def __init__(self, name, position, health):
        """The 'Birth' of the player: Sets up all starting data."""
        self.name = name
        self.position = np.array(position)  # Uses NumPy for 3D coordinates
        self.health = health
        self.inventory = []

    def move_player(self, direction_vector):
        """Updates position by adding a movement vector."""
        move_vec = np.array(direction_vector)
        self.position += move_vec
        print(f"-> {self.name} moved to {self.position}")

    def take_damage(self, amount):
        """Subtracts health and checks for 'Game Over'."""
        self.health -= amount
        if self.health <= 0:
            print(f"!!! Game over for {self.name}!")
        else:
            print(f"| {self.name} took {amount} damage! HP: {self.health}")

    def pick_up(self, item_name):
        """Adds a new item string to the inventory list."""
        self.inventory.append(item_name)
        print(f"+ {self.name} picked up a {item_name}!")

    def show_inventory(self):
        """Loops through the list to show everything the player has."""
        print(f"\n--- Inventory for {self.name} ---")
        if not self.inventory:
            print("(Empty)")
        for item in self.inventory:
            print(f"- {item}")
        print("---------------------------\n")
