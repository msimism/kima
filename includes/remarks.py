import random

class Remarks:
    def __init__(self):
        with open("text/insults.txt", "r") as insultfile:
            self.insults = [line.strip() for line in insultfile.readlines()]
        with open("text/compliments.txt", "r") as complimentsfile:
            self.compliments = [line.strip() for line in complimentsfile.readlines()]
            
        
    def load(self, file):
        with open(file, "r") as new_insultfile:
            new_insults = [line.strip() for line in new_insultfile.readlines()]
            self.insults.extend(new_insults)
        with open(file, "r") as new_complimentsfile:
            new_compliments = [line.strip() for line in new_complimentsfile.readlines()]
            self.compliments.extend(new_compliments)

    def random_insult(self):
        return random.choice(self.insults)
        
    def random_compliment(self):
        return random.choice(self.compliments)
    
    def insult(self, nick):
        random_insult = self.random_insult()
        return f"{nick}, {random_insult}"
    
    def compliment(self, nick):
        random_compliment = self.random_compliment()
        return f"{nick}, {random_compliment}"