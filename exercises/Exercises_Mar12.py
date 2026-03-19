#New day


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
        if target_shield.energy == 100:
            return "Shields already at full energy!"

        target_shield.energy = 100
        return "Shields Fully Charged!"

def function_two(n):
    return n + 10

result_two = function_two(5)
print(result_two)  # 15
result_two = result_two + 10
print(result_two)  # 25

shield = Shield(80)
repair = RepairStation()
print(repair.recharge(shield))  # "Shields Fully Charged!"
print(shield.energy)  # 100

repair.recharge(shield)
print(shield.energy)  # 100


