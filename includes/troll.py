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
        raise NotImplementedError("Subclasses should implement this method")

class InsultTroll(Troll):
    def __init__(self, remarks):
        super().__init__()
        self.remarks = remarks

    def troll_user(self, nick):
        if nick in self.users and self.should_troll():
            return self.remarks.insult(nick)
        return None

class ComplimentTroll(Troll):
    def __init__(self, remarks):
        super().__init__()
        self.remarks = remarks

    def troll_user(self, nick):
        if nick in self.users and self.should_troll():
            return self.remarks.compliment(nick)
        return None

class FloodTroll(Troll):
    def __init__(self):
        super().__init__()

    def troll_user(self, nick):
        if nick in self.users and self.should_troll():
            return "Flood message: This is a flood message targeting " + nick
        return None
