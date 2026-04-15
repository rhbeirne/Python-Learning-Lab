#Fight between Mario and Sonic
# Class that creates both players, speed, jump, color, health, attack-spin or punch
# Choice of who you want to play
# Use attack that makes sense

class Player:
    def __init__(self, name, speed, jump, color, attack):
        self.name = name
        self.speed = speed
        self.jump = jump
        self.color = color
        self.health = 100
        self.attack = attack

    def welcome(self):

        return f"Welcome {self.color} {self.name}. You have {self.speed} speed, {self.jump} jump, and a {self.attack} attack. Your health is {self.health}. Good luck in the fight!"

    def attack_opponent(self, opponent):
        if self.attack == "punch" and self.name == "Mario":
            damage = 100
        elif self.attack == "spin":
            damage = 15
        else:
            damage = 0

        opponent.health -= damage
        return f"{self.name} attacks {opponent.name} with a {self.attack}, dealing {damage} damage! {opponent.name}'s health is now {opponent.health}."


hero =Player("Mario", 50, 100, "red", "punch")
hero2 = Player("Sonic", 100, 50, "blue", "spin")

player_selection = input("Who do you want to play as? (Mario or Sonic): ").capitalize().strip()

if player_selection == "Mario":
    print(hero.welcome())
elif player_selection == "Sonic":
    print(hero2.welcome())
else:
    print("Invalid selection. Please choose either Mario or Sonic.")

first_attack =hero.attack_opponent(hero2)
print(first_attack)
        

        