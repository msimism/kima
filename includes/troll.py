""" Troll module to handle trolling behavior """

import logging
import random

logger = logging.getLogger('includes.troll')

class Troll:
    def __init__(self, remarks):
        self.remarks = remarks
        self.users = []
        logger.info("Troll initialized.")

    def add(self, nick):
        if nick not in self.users:
            self.users.append(nick)
            logger.debug(f"User added to troll list: {nick}")

    def remove(self, nick):
        if nick in self.users:
            self.users.remove(nick)
            logger.debug(f"User removed from troll list: {nick}")
            return True
        return False

    def list_users(self):
        return self.users

    def should_troll(self):
        return random.choice([True, False])

    def troll_user(self, nick, message):
        if nick in self.users and self.should_troll():
            action = random.choice(["insult", "compliment", "flood"])
            logger.debug(f"Trolling user with {action}: {nick}")
            if action == "insult":
                return self.remarks.insult(nick)
            elif action == "compliment":
                return self.remarks.compliment(nick)
            elif action == "flood":
                return self.flood(nick, message)
        return None

    def flood(self, nick, message):
        colors = ["\x0304", "\x0309", "\x0312", "\x0306"]  # Red, Light Blue, Light Green, Purple
        flood_message = "".join([random.choice(colors) + char for char in message])
        logger.debug(f"Flood message for {nick}: {flood_message}")
        return f"{nick}: {flood_message}"
