""" Jokes module to handle jokes management """

import json
import random
import logging
import threading

logger = logging.getLogger('includes.jokes')

class Jokes:
    def __init__(self, file_path="data/jokes/jokes.json"):
        self.file_path = file_path
        self.jokes = []
        self.load_jokes_from_file()
        self.lock = threading.Lock()

    def load_jokes_from_file(self):
        try:
            with open(self.file_path, "r") as file:
                jokes_data = json.load(file)
                if isinstance(jokes_data, list):
                    self.jokes = jokes_data
                else:
                    logger.error(f"Invalid format in {self.file_path}, expected a list.")
                    self.jokes = []
            logger.debug(f"Jokes loaded: {self.jokes}")
        except FileNotFoundError:
            logger.warning(f"{self.file_path} not found. Starting with an empty joke list.")
            self.jokes = []
        except json.JSONDecodeError:
            logger.error(f"{self.file_path} is not a valid JSON file. Starting with an empty joke list.")
            self.jokes = []

    def add(self, joke):
        if not joke:
            logger.warning("Joke must not be empty.")
            return "Joke must not be empty."
        new_id = max((j['id'] for j in self.jokes), default=0) + 1
        new_joke = {"id": new_id, "joke": joke}
        self.jokes.append(new_joke)
        self.save_jokes_to_file()
        logger.info(f"Joke added: {new_id} - {joke}")
        return f"Joke added: {new_id}"

    def remove(self, joke_id):
        joke_id = int(joke_id)
        for joke in self.jokes:
            if joke['id'] == joke_id:
                self.jokes.remove(joke)
                self.save_jokes_to_file()
                logger.info(f"Joke {joke_id} removed.")
                return f"Joke {joke_id} removed."
        logger.warning(f"Joke {joke_id} not found.")
        return "Joke not found."

    def list(self):
        return "\n".join(f"{j['id']}: {j['joke']}" for j in self.jokes)

    def get_random_joke(self):
        if self.jokes:
            joke = random.choice(self.jokes)
            return f"{joke['id']}: {joke['joke']}"
        return "No jokes available."

    def get_joke_by_id(self, joke_id):
        joke_id = int(joke_id)
        for joke in self.jokes:
            if joke['id'] == joke_id:
                return f"{joke['id']}: {joke['joke']}"
        return "Joke not found."

    def save_jokes_to_file(self):
        with self.lock:
            try:
                with open(self.file_path, "w") as file:
                    json.dump(self.jokes, file, indent=4)
                logger.debug("Jokes saved successfully.")
            except IOError as e:
                logger.error(f"Error saving jokes: {e}")
