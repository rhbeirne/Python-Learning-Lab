#New day

class Shield:
    def __init__(self):
        self.active = False
        self.energy = 100
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
        target_shield.energy = 100
        return "Shields Fully Charged!"
    
shield = Shield()
print(shield.is_protected())
print(shield.take_hit())  # False

repair = RepairStation()
print(repair.recharge(shield))  # "Shields Fully Charged!"
print(shield.energy)  # 100


