
from scripts.VRPlayer import VRPlayer
from scripts.enemies import Boss

p1 = VRPlayer("Richard")
b1 = Boss("Ganon", 99)

b1.show_inventory() # Notice: Boss can use Player methods!
