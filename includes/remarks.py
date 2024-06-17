""" Remarks module to handle insults and compliments """

import logging
import random
import json

logger = logging.getLogger('includes.remarks')

class Remarks:
    def __init__(self):
        self.insults = self.load_remarks("data/remarks/insults.json")
        logger.debug(f"Loaded insults: {self.insults}")
        
        self.compliments = self.load_remarks("data/remarks/compliments.json")
        logger.debug(f"Loaded compliments: {self.compliments}")
        
        logger.info("Remarks initialized.")

    def load_remarks(self, file_path):
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            logger.warning(f"{file_path} not found. Starting with an empty list.")
            return []
        except json.JSONDecodeError:
            logger.error(f"{file_path} is not a valid JSON file. Starting with an empty list.")
            return []

    def random_insult(self):
        insult = random.choice(self.insults)
        logger.debug(f"Selected random insult: {insult}")
        return insult
        
    def random_compliment(self):
        compliment = random.choice(self.compliments)
        logger.debug(f"Selected random compliment: {compliment}")
        return compliment
    
    def insult(self, nick):
        random_insult = self.random_insult()
        logger.debug(f"Generated insult for {nick}: {random_insult}")
        return f"{nick}, {random_insult}"
    
    def compliment(self, nick):
        random_compliment = self.random_compliment()
        logger.debug(f"Generated compliment for {nick}: {random_compliment}")
        return f"{nick}, {random_compliment}"
