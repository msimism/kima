""" Help module to handle help messages """

import logging

logger = logging.getLogger('includes.help')

class Help:
    def __init__(self):
        self.help_message = self.load_help_message()
        logger.info("Help initialized.")

    def load_help_message(self):
        return """
        Available commands:
        - .insult [nick]: Insult a user.
        - .compliment [nick]: Compliment a user.
        - .quotes: Get a random quote.
        - .quotes list: List all quotes.
        - .quotes read [id]: Read a specific quote.
        - .quotes add [quote]: Add a new quote.
        - .quotes del [id]: Delete a specific quote.
        - .quotes search [keyword]: Search quotes by content.
        - .quotes search -by [author]: Search quotes by author.
        - .jokes: Get a random joke.
        - .jokes list: List all jokes.
        - .jokes read [id]: Read a specific joke.
        - .jokes add [joke]: Add a new joke.
        - .jokes del [id]: Delete a specific joke.
        - .troll add [nick]: Add a user to the troll list.
        - .troll remove [nick]: Remove a user from the troll list.
        - .troll list: List all users being trolled.
        - .help: Show this help message.
        """

    def get_help_message(self):
        logger.debug("Fetching help message.")
        return self.help_message
