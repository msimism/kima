class Quotes:
    def __init__(self):
        self.quotes = []
        self.file_path = "text/quotes.txt"
        self.load_quotes_from_file()

    def load_quotes_from_file(self):
        try:
            with open(self.file_path, "r") as quotefile:
                for line in quotefile:
                    quote, author = line.strip().split(' - ')
                    self.quotes.append((quote, author))
        except FileNotFoundError:
            print("The quotes file was not found. Starting with an empty list.")
        except ValueError:
            print("Error parsing the quotes file. Ensure it is properly formatted as 'Quote - Author'.")

    def add(self, quote, author):
        if (quote, author) not in self.quotes:
            self.quotes.append((quote, author))
            self.save_quotes_to_file()

    def remove(self, quote, author):
        if (quote, author) in self.quotes:
            self.quotes.remove((quote, author))
            self.save_quotes_to_file()

    def list(self):
        return "\n".join([f"{quote} - {author}" for quote, author in self.quotes])

    def save_quotes_to_file(self):
        with open(self.file_path, "w") as quotefile:
            for quote, author in self.quotes:
                quotefile.write(f"{quote} - {author}\n")
