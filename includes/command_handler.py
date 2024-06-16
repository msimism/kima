import logging

class CommandHandler:
    def __init__(self, remarks, quotes, jokes, insult_troll, compliment_troll, flood_troll, help, prefix="."):
        self.remarks = remarks
        self.quotes = quotes
        self.jokes = jokes
        self.insult_troll = insult_troll
        self.compliment_troll = compliment_troll
        self.flood_troll = flood_troll
        self.help = help
        self.prefix = prefix
        self.trolls = [insult_troll, compliment_troll, flood_troll]
        self.next_troll_index = 0
        logging.info(f"CommandHandler initialized with prefix: {self.prefix}")

    def handle_message(self, connection, channel, sender, message):
        logging.debug(f"Handling message: {message} from {sender} in {channel}")
        if not message.startswith(self.prefix):
            # Check if the sender should be trolled
            troll_message = self.check_trolling(sender)
            if troll_message:
                self.send_multiline_message(connection, channel, troll_message)
            return

        command = message[len(self.prefix):].split()
        if not command:
            logging.debug("No command found after prefix.")
            return

        logging.debug(f"Command found: {command[0]}")
        if command[0].lower() == "insult":
            self.handle_insult(connection, channel, command)
        elif command[0].lower() == "compliment":
            self.handle_compliment(connection, channel, command)
        elif command[0].lower() == "quotes":
            self.handle_quotes_command(connection, channel, sender, command)
        elif command[0].lower() == "jokes":
            self.handle_jokes_command(connection, channel, sender, command)
        elif command[0].lower() == "troll":
            self.handle_troll_command(connection, channel, command)
        elif command[0].lower() == "help":
            self.handle_help(connection, channel)
        else:
            logging.debug(f"Unhandled command: {command[0]}")

    def handle_insult(self, connection, channel, command):
        if len(command) > 1:
            nick = command[1]
            insult_message = self.remarks.insult(nick)
            self.send_multiline_message(connection, channel, insult_message)

    def handle_compliment(self, connection, channel, command):
        if len(command) > 1:
            nick = command[1]
            compliment_message = self.remarks.compliment(nick)
            self.send_multiline_message(connection, channel, compliment_message)

    def handle_quotes_command(self, connection, channel, sender, command):
        if len(command) == 1:
            quote_message = self.quotes.get_random_quote()
            self.send_multiline_message(connection, channel, quote_message)
        elif len(command) > 1:
            subcommand = command[1].lower()
            if subcommand == "list":
                quote_list = self.quotes.list()
                self.send_multiline_message(connection, channel, quote_list)
            elif subcommand == "read" and len(command) > 2:
                try:
                    quote_id = int(command[2])
                    quote_message = self.quotes.get_quote_by_id(quote_id)
                    self.send_multiline_message(connection, channel, quote_message)
                except ValueError:
                    connection.privmsg(channel, "Invalid quote ID.")
            elif subcommand == "del" and len(command) > 2:
                try:
                    quote_id = int(command[2])
                    self.quotes.remove(quote_id)
                    connection.privmsg(channel, f"Quote {quote_id} removed.")
                except ValueError:
                    connection.privmsg(channel, "Invalid quote ID.")
            elif subcommand == "add" and len(command) > 3:
                try:
                    quote_parts = " ".join(command[2:]).rsplit('-', 1)
                    quote = quote_parts[0].strip()
                    author = quote_parts[1].strip()
                    self.quotes.add(quote, author)
                    connection.privmsg(channel, f"Quote added: \"{quote}\" - {author} (added by {sender})")
                except IndexError:
                    connection.privmsg(channel, "Failed to add quote. Please use the format: .quotes add <quote> - <author>")
            else:
                connection.privmsg(channel, "Invalid subcommand or missing parameters for .quotes.")
        else:
            connection.privmsg(channel, "Invalid subcommand for .quotes.")

    def handle_jokes_command(self, connection, channel, sender, command):
        if len(command) == 1:
            joke_message = self.jokes.get_random_joke()
            self.send_multiline_message(connection, channel, joke_message)
        elif len(command) > 1:
            subcommand = command[1].lower()
            if subcommand == "list":
                joke_list = self.jokes.list()
                self.send_multiline_message(connection, channel, joke_list)
            elif subcommand == "read" and len(command) > 2:
                try:
                    joke_id = int(command[2])
                    joke_message = self.jokes.get_joke_by_id(joke_id)
                    self.send_multiline_message(connection, channel, joke_message)
                except ValueError:
                    connection.privmsg(channel, "Invalid joke ID.")
            elif subcommand == "del" and len(command) > 2:
                try:
                    joke_id = int(command[2])
                    self.jokes.remove(joke_id)
                    connection.privmsg(channel, f"Joke {joke_id} removed.")
                except ValueError:
                    connection.privmsg(channel, "Invalid joke ID.")
            elif subcommand == "add" and len(command) > 2:
                joke = " ".join(command[2:])
                self.jokes.add(joke)
                connection.privmsg(channel, f"Joke added: \"{joke}\" (added by {sender})")
            else:
                connection.privmsg(channel, "Invalid subcommand or missing parameters for .jokes.")
        else:
            connection.privmsg(channel, "Invalid subcommand for .jokes.")

    def handle_troll_command(self, connection, channel, command):
        if len(command) > 2:
            action = command[1].lower()
            nick = command[2]
            if action == "add":
                self.add_user_to_troll(nick)
                connection.privmsg(channel, f"{nick} added to trolling list.")
            elif action == "remove":
                self.remove_user_from_troll(nick)
                connection.privmsg(channel, f"{nick} removed from trolling list.")
        else:
            connection.privmsg(channel, "Invalid subcommand for .troll.")

    def add_user_to_troll(self, nick):
        self.trolls[self.next_troll_index].add(nick)
        self.next_troll_index = (self.next_troll_index + 1) % len(self.trolls)

    def remove_user_from_troll(self, nick):
        for troll in self.trolls:
            troll.remove(nick)

    def handle_help(self, connection, channel):
        help_message = self.help.get_help_message()
        self.send_multiline_message(connection, channel, help_message)

    def check_trolling(self, nick):
        troll_message = self.insult_troll.troll_user(nick)
        if not troll_message:
            troll_message = self.compliment_troll.troll_user(nick)
        if not troll_message:
            troll_message = self.flood_troll.troll_user(nick)
        return troll_message

    def send_multiline_message(self, connection, channel, message):
        lines = message.split('\n')
        for line in lines:
            connection.privmsg(channel, line)

    # Add more handlers for new commands here
