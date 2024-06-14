import irc.bot, irc.client, ssl, time

class IRCBot(irc.bot.SingleServerIRCBot):
    def __init__(self, server, port, channel, nickname, username):
        ssl_factory = irc.connection.Factory(wrapper=ssl.wrap_socket)
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, username, connect_factory=ssl_factory)
        self.channel = channel

    def on_welcome(self, connection, event):
        connection.join(self.channel)

    def on_join(self, connection, event):
        connection.privmsg(self.channel, "Hi Panik! I'm an IRC bot.")

    def on_pubmsg(self, connection, event):
        message = event.arguments[0]
        sender = irc.client.NickMask(event.source).nick
        channel = event.target
        if "hi" in message.lower():
            connection.privmsg(self.channel, "Hi Panik!")
        else:
            print(f"{channel} - {sender} - {message}")

    def on_disconnect(self, connection, event):
        print("Disconnected from the server. Reconnecting...")
        time.sleep(10)
        self.reconnect()

    def reconnect(self):
        server, port = self.connection.server_list[0]
        self.connection.connect(server, port, self.connection.nick, self.connection.username)

if __name__ == "__main__":
    server = "irc.twistednet.org"
    port = 6697  # SSL port
    channel = "#paniked"
    nickname = "kima"
    username = "black"

    bot = IRCBot(server, port, channel, nickname, username)
    bot.start()
