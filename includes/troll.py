import random

class Troll:
    def __init__(self):
        self.users = []

    def add(self, nick):
        if nick not in self.users:
            self.users.append(nick)

    def remove(self, nick):
        if nick in self.users:
            self.users.remove(nick)

    def should_troll(self):
        return random.choice([True, False])

    def troll_user(self, nick):
        if nick in self.users and self.should_troll():
            return random.choice(["insult", "compliment"])
        return None
