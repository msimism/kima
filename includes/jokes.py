import json
import random

class Jokes:
    def __init__(self):
        self.jokes = {}
        self.next_id = 1
        self.load_jokes_from_file()

    def load_jokes_from_file(self):
        try:
            with open("text/jokes.json", "r") as joke_file:
                jokes = json.load(joke_file)
                for joke in jokes:
                    self.jokes[joke['id']] = joke['joke']
                    if joke['id'] >= self.next_id:
                        self.next_id = joke['id'] + 1
        except FileNotFoundError:
            print("The jokes file was not found.")
        except json.JSONDecodeError:
            print("Error parsing the jokes file. Ensure it is properly formatted JSON.")

    def add(self, joke):
        self.jokes[self.next_id] = joke
        self.next_id += 1
        self.save_jokes_to_file()

    def remove(self, joke_id):
        if joke_id in self.jokes:
            del self.jokes[joke_id]
            self.save_jokes_to_file()

    def list(self):
        return "\n\n".join([f"{joke_id}: {joke}" for joke_id, joke in self.jokes.items()])

    def get_joke_by_id(self, joke_id):
        if joke_id in self.jokes:
            return f"{joke_id}: {self.jokes[joke_id]}"
        return "Joke not found."

    def get_random_joke(self):
        joke_id = random.choice(list(self.jokes.keys()))
        return f"{joke_id}: {self.jokes[joke_id]}"

    def save_jokes_to_file(self):
        with open("text/jokes.json", "w") as joke_file:
            jokes = [{'id': joke_id, 'joke': joke} for joke_id, joke in self.jokes.items()]
            json.dump(jokes, joke_file, indent=4)
