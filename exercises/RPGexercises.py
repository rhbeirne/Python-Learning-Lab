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


