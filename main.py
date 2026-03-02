
from scripts.VRPlayer import VRPlayer
from scripts.enemies import Boss

p1 = VRPlayer("Richard", [0, 0, 0], 100)
b1 = Boss("Ganon",[5,5,5],500 ,99)

b1.show_inventory() # Notice: Boss can use Player methods!
