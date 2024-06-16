import random

class Quotes:
    def __init__(self):
        self.quotes = {}
        self.next_id = 1
        self.load_quotes_from_file()

    def load_quotes_from_file(self):
        try:
            with open("text/quotes.json", "r") as quotefile:
                jokes = json.load(quotefile)
                for joke in jokes:
                    self.quotes[joke['id']] = joke['joke']
                    if joke['id'] >= self.next_id:
                        self.next_id = joke['id'] + 1
        except FileNotFoundError:
            print("The quotes file was not found.")
        except json.JSONDecodeError:
            print("Error parsing the quotes file. Ensure it is properly formatted JSON.")

    def add(self, quote, author):
        if (quote, author) not in self.quotes.values():
            self.quotes[self.next_id] = (quote, author)
            self.next_id += 1
            self.save_quotes_to_file()

    def remove(self, quote_id):
        if quote_id in self.quotes:
            del self.quotes[quote_id]
            self.save_quotes_to_file()

    def list(self):
        return "\n".join([f"{quote_id}: {quote} - {author}" for quote_id, (quote, author) in self.quotes.items()])

    def get_quote_by_id(self, quote_id):
        if quote_id in self.quotes:
            quote, author = self.quotes[quote_id]
            return f"{quote_id}: {quote} - {author}"
        return "Quote not found."

    def get_random_quote(self):
        quote_id = random.choice(list(self.quotes.keys()))
        quote, author = self.quotes[quote_id]
        return f"{quote_id}: {quote} - {author}"

    def save_quotes_to_file(self):
        with open("text/quotes.json", "w") as quotefile:
            jokes = [{'id': quote_id, 'quote': quote, 'author': author} for quote_id, (quote, author) in self.quotes.items()]
            json.dump(jokes, quotefile, indent=4)
