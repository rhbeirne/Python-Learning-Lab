# Exercise 1: List Comprehension
all_scores = [50, 120, 85, 200, 30, 150]
high_scores = [s for s in all_scores if s > 100]

# Exercise 2: For Loop
stars = ["Gold", "Cyan", "Gold", "Magenta"]
player_color = "Gold"
for s in stars:
    if s == player_color:
        print("Hit")
    else:
        print("Miss")

# Exercise 3: Functions
def calculate_points(base_points, multiplier):
    return base_points * multiplier

# Exercise 4: Dictionaries
star_values = {"Gold": 100, "Cyan": 50, "Magenta": 75}
print(star_values["Magenta"])

# Exercise 5: Input Validation
target_color = "Neon"
if target_color in star_values:
    print("Valid star!")
else:
    print("Unknown anomaly!")

# Exercise 6: While Loops
energy = 0
while energy < 100:
    energy += 10

# Exercise 7: *args
def total_points(*args):
    return sum(args)

# Exercise 8: List Slicing
all_hits = ["Gold", "Cyan", "Magenta", "Gold", "Silver", "Neon"]
recent = all_hits[-3:]

# Exercise 9: Class Methods
class Star:
    def __init__(self):
        self.active = False
    def reset(self):
        self.active = True

# Exercise 10: Data Cleaning
raw_data = [100, None, 50, None, 200]
total = 0
for item in raw_data:
    if item is not None:
        total += item


class FuelTank:
    def __init__(self):
        self.level = 100

    def consume_fuel(self, amount):
        
        if amount <= self.level:
            self.level -= amount
        else:
            print("Not enough fuel")

class Spaceship:
    def get_power(self, engine_count): # Added a colon here too!
        return engine_count * 10

# 1. Create the "instance" (The Toolbox)
my_ship = Spaceship() 

# 2. Use the "instance" to call the method
current_power = my_ship.get_power(3) 

print(current_power) # Result: 30    

class Spaceship:
    def __init__(self, engines):
        self.engine_count = engines

    def calculate_total_power(self):
        return self.engine_count * 10

total_power = Spaceship(5).calculate_total_power()
print(total_power) # Result: 50



        