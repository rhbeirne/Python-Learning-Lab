#Exercises


import json

import random

import math




player_stats = {"level": 5, "health": 100}
print(json.dumps(player_stats))


roll = random.randint(1, 20)
if roll == 20:
    print("Amazing! Direct hit!")
elif roll == 1:
    print("Oh no, you tripped!")
else:
    print(f"You rolled a {roll}.")  


items = ["Shield", "Bread", "Key"]
print(json.dumps(items))


from datetime import datetime
now = datetime.now()

# We only care about the hour being less than 10
if now.hour < 10:
    print("Morning Bonus Granted!")
else:
    print("No bonus, it's past 10 AM.")