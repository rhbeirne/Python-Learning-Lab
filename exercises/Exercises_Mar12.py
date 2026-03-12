#New day

from asyncio import shield


class Shield:
    def __init__(self, energy  ):
        self.active = False
        self.energy = energy
        self.overdrive = False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def is_protected(self):
        return self.active

    def take_hit(self):
        if self.active:
            if self.overdrive:
                self.energy -= 40
            else:
                self.energy -= 20
            return True
        else:
            return False
        


class RepairStation:
    def recharge(self, target_shield):
        target_shield.energy == 100:
            return "Shields already at full energy!"
        
        
    


repair = RepairStation()
print(repair.recharge(shield))  # "Shields Fully Charged!"
print(shield.energy)  # 100

repair.recharge(shield)
print(shield.energy)  # 80


