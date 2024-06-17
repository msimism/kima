""" Quotes module to handle quotes management """

import json
import random
import logging
import os
import threading

logger = logging.getLogger('includes.quotes')

class Quotes:
    def __init__(self, file_path="data/quotes/quotes.json"):
        self.file_path = file_path
        self.quotes = {}
        self.load_quotes_from_file()
        self.last_search = {}
        self.lock = threading.Lock()

    def load_quotes_from_file(self):
        try:
            with open(self.file_path, "r") as file:
                self.quotes = json.load(file)
            logger.debug(f"Quotes loaded: {self.quotes}")
        except FileNotFoundError:
            logger.warning(f"{self.file_path} not found. Starting with an empty quote list.")
            self.quotes = {}
        except json.JSONDecodeError:
            logger.error(f"{self.file_path} is not a valid JSON file. Starting with an empty quote list.")
            self.quotes = {}

    def add(self, quote, added_by):
        if not quote or not added_by:
            logger.warning("Quote and added_by must not be empty.")
            return "Quote and added_by must not be empty."
        new_id = str(max(map(int, self.quotes.keys()), default=0) + 1)
        self.quotes[new_id] = {"quote": quote, "added_by": added_by}
        self.save_quotes_to_file()
        logger.info(f"Quote added: {new_id} - {quote} - added by {added_by}")
        return f"Quote added: {new_id}"

    def remove(self, quote_id):
        if str(quote_id) in self.quotes:
            del self.quotes[str(quote_id)]
            self.save_quotes_to_file()
            logger.info(f"Quote {quote_id} removed.")
        else:
            logger.warning(f"Quote {quote_id} not found.")
            return "Quote not found."

    def list(self):
        return "\n".join(f"{qid}: {qdata['quote']} - added by {qdata['added_by']}" for qid, qdata in self.quotes.items())

    def get_random_quote(self):
        if self.quotes:
            quote_id = random.choice(list(self.quotes.keys()))
            return f"{quote_id}: {self.quotes[quote_id]['quote']} - added by {self.quotes[quote_id]['added_by']}"
        return "No quotes available."

    def get_quote_by_id(self, quote_id):
        if str(quote_id) in self.quotes:
            qdata = self.quotes[str(quote_id)]
            return f"{quote_id}: {qdata['quote']} - added by {qdata['added_by']}"
        return "Quote not found."

    def search_quotes(self, keyword, search_by):
        if search_by == "content":
            matching_quotes = [qid for qid, qdata in self.quotes.items() if keyword.lower() in qdata['quote'].lower()]
        elif search_by == "author":
            matching_quotes = [qid for qid, qdata in self.quotes.items() if keyword.lower() in qdata['added_by'].lower()]
        else:
            return "Invalid search option."

        if not matching_quotes:
            return "No matching quotes found."
        
        if keyword not in self.last_search:
            self.last_search[keyword] = matching_quotes
        
        if not self.last_search[keyword]:
            self.last_search[keyword] = matching_quotes

        quote_id = self.last_search[keyword].pop(0)
        self.last_search[keyword].append(quote_id)
        qdata = self.quotes[quote_id]

        # Bold and underline the keyword in the quote text
        formatted_quote = self.highlight_keyword(qdata['quote'], keyword)
        return f"{quote_id}: {formatted_quote} - added by {qdata['added_by']}"

    def highlight_keyword(self, text, keyword):
        bold = "\x02"
        underline = "\x1F"
        reset = "\x0F"
        formatted_keyword = f"{bold}{underline}{keyword}{reset}"
        return text.replace(keyword, formatted_keyword)

    def save_quotes_to_file(self):
        with self.lock:
            try:
                with open(self.file_path, "w") as file:
                    json.dump(self.quotes, file, indent=4)
                logger.debug("Quotes saved successfully.")
            except IOError as e:
                logger.error(f"Error saving quotes: {e}")
