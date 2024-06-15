class CommandHandler:
    def __init__(self, remarks, quotes, troll):
        self.remarks = remarks
        self.quotes = quotes
        self.troll = troll

    def handle_message(self, connection, channel, sender, message):
        if message.lower().startswith("!insult"):
            self.handle_insult(connection, channel, message)
        elif message.lower().startswith("!compliment"):
            self.handle_compliment(connection, channel, message)
        elif message.lower().startswith("!quote"):
            self.handle_quote(connection, channel, message)
        elif message.lower().startswith("!troll"):
            self.handle_troll(connection, channel, message)
        else:
            print(f"Unhandled message: {message}")

    def handle_insult(self, connection, channel, message):
        parts = message.split()
        if len(parts) > 1:
            nick = parts[1]
            insult_message = self.remarks.insult(nick)
            connection.privmsg(channel, insult_message)

    def handle_compliment(self, connection, channel, message):
        parts = message.split()
        if len(parts) > 1:
            nick = parts[1]
            compliment_message = self.remarks.compliment(nick)
            connection.privmsg(channel, compliment_message)

    def handle_quote(self, connection, channel, message):
        quote_message = self.quotes.list()
        connection.privmsg(channel, quote_message)
        
    def handle_troll(self, connection, channel, message):
        parts = message.split()
        if len(parts) > 1:
            nick = parts[1]
            troll_message = self.troll.troll(nick)
            connection.privmsg(channel, troll_message)

    # Add more handlers for new commands here
