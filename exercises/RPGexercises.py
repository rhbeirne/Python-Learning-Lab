# RPG exercises

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
    
    def heal(self, amount):
        self.health += amount
        
        if self.health > self.max_health:
            self.health = self.max_health
    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    def gain_level(self):
        self.level += 1
        self.max_health += 20
        return f"Level up! You are now level {self.level}. Your max health is now {self.max_health}."
    
    def attack(self, target):
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

    


p1 = Player(input("Enter your character's name: "))
p2 = Player("Fat Goblin King", 200)
print(p1.name, p1.health)  # "Wilder 100"
print(p2.name, p2.health)  # "Fat Goblin King 200"
mage1 = Mage("Gandalf")
print(mage1.name, mage1.cast_spell(p2))  # "Gandalf casts a fireball




print(p1.name, p1.gain_level())  # "Wilder Level up! You are now level 2."



p1.take_damage(50)
p1.heal(30)
print(p1.health)  # 80
print(p1.name, p1.gain_level())   # "Level up! You are now level 3."
print(p1.max_health)  # 120

p1.pick_up_item("Sword")
p1.pick_up_item("Shield")
p1.pick_up_item("Health Potion")
print(p1.use_item("Health Potion"))

mage1.pick_up_item("wand")

print(mage1.inventory())



