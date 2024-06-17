""" CommandHandler module to handle IRC bot commands """

import logging

logger = logging.getLogger('includes.command_handler')

class CommandHandler:
    def __init__(self, remarks, quotes, jokes, troll, help, prefix="."):
        self.remarks = remarks
        self.quotes = quotes
        self.jokes = jokes
        self.troll = troll
        self.help = help
        self.prefix = prefix
        logger.info(f"CommandHandler initialized with prefix: {self.prefix}")

    def handle_message(self, connection, channel, sender, message):
        logger.debug(f"Handling message: {message} from {sender} in {channel}")
        if not message.startswith(self.prefix):
            troll_message = self.troll.troll_user(sender, message)
            if troll_message:
                self.send_multiline_message(connection, channel, troll_message)
            return

        command = message[len(self.prefix):].split()
        if not command:
            logger.debug("No command found after prefix.")
            return

        logger.debug(f"Command found: {command[0]}")
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
            logger.debug(f"Unhandled command: {command[0]}")

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
            elif subcommand == "add" and len(command) > 2:
                quote = " ".join(command[2:])
                result = self.quotes.add(quote, sender)
                connection.privmsg(channel, result)
            elif subcommand == "search" and len(command) > 2:
                search_by = "content"
                if command[2] == "-by":
                    search_by = "author"
                    keyword = " ".join(command[3:])
                else:
                    keyword = " ".join(command[2:])
                search_result = self.quotes.search_quotes(keyword, search_by)
                self.send_multiline_message(connection, channel, search_result)
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
        if len(command) > 1:
            action = command[1].lower()
            if action == "add" and len(command) > 2:
                nick = command[2]
                self.troll.add(nick)
                connection.privmsg(channel, f"{nick} added to trolling list.")
            elif action == "remove" and len(command) > 2:
                nick = command[2]
                removed = self.troll.remove(nick)
                if removed:
                    connection.privmsg(channel, f"{nick} removed from trolling list.")
                else:
                    connection.privmsg(channel, f"{nick} was not on the trolling list.")
            elif action == "list":
                troll_list = self.troll.list_users()
                connection.privmsg(channel, f"Currently trolling: {', '.join(troll_list)}")
            else:
                connection.privmsg(channel, "Invalid subcommand for .troll.")
        else:
            connection.privmsg(channel, "Invalid subcommand for .troll.")

    def handle_help(self, connection, channel):
        help_message = self.help.get_help_message()
        self.send_multiline_message(connection, channel, help_message)

    def send_multiline_message(self, connection, channel, message):
        lines = message.split('\n')
        for line in lines:
            connection.privmsg(channel, line)

    # Add more handlers for new commands here
