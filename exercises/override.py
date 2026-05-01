#4-13


class Career:
    def __init__(self, name, tech, salary, AI_vulnerable):
        self.name = name
        self.tech = tech
        self.salary = salary
        self.AI_vulnerable = AI_vulnerable

    def get_description(self):
        return f"{self.name} is a career that requires dedication and hard work. Salary: ${self.salary} per year. Field: {self.tech}."
    
    
    def get_AI_vulnerability(self):
        if self.AI_vulnerable:
            return f"{self.name} is vulnerable to AI automation."
        else:
            return f"{self.name} is not vulnerable to AI automation."
    def danger_level(self):
        if self.name == "Astronaut":
            return "High"
        elif self.name == "IT Professional":
            return "Medium"
        elif self.name == "Maid":
            return "Low"
        else:
            return "Unknown"
        
        
ITpro=Career("IT Professional", "Technology", 80000, True)
print(ITpro.get_description())
print(ITpro.get_AI_vulnerability()) 
Maid=Career("Maid", "Cleaning", 30000, False)
print(Maid.get_description())
print(Maid.get_AI_vulnerability())  
Astronaut=Career("Astronaut", "Space Exploration", 120000, False)
print(Astronaut.get_description())
print(Astronaut.get_AI_vulnerability())
print(f"{Astronaut.name}'s danger level is {Astronaut.danger_level()}")