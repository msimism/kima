""" Module Imports """
from includes.command_handler import CommandHandler
from includes.remarks import Remarks
from includes.quotes import Quotes
from includes.troll import Troll
""" Module Imports """

""" Library Imports """
import irc.bot
import ssl
import time
import sys
import logging
import signal
""" Library Imports """

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IRCBot(irc.bot.SingleServerIRCBot):
    def __init__(self, server, port, channels, nickname, username):
        ssl_factory = irc.connection.Factory(wrapper=ssl.wrap_socket)
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, username, connect_factory=ssl_factory)
        self.channel_list = channels
        self.channels = {}  # This dictionary will hold the channel objects
        self.remarks = Remarks()
        self.troll = Troll()
        self.quotes = Quotes()
        self.command_handler = CommandHandler(self.remarks, self.quotes, self.troll)

    def on_welcome(self, connection, event):
        for channel in self.channel_list:
            logging.info(f"Joining {channel}")
            connection.join(channel)

    def on_pubmsg(self, connection, event):
        message = event.arguments[0]
        sender = irc.client.NickMask(event.source).nick
        channel = event.target
        logging.info(f"Message from {sender} in {channel}: {message}")
        self.command_handler.handle_message(connection, channel, sender, message)

    def on_disconnect(self, connection, event):
        logging.warning("Disconnected from the server. Reconnecting...")
        time.sleep(10)
        self.reconnect()

    def reconnect(self):
        server, port = self.connection.server_list[0]
        try:
            self.connection.connect(server, port, self.connection.nick, self.connection.username)
        except Exception as e:
            logging.error(f"Reconnection failed: {e}")
            time.sleep(10)
            self.reconnect()

    def hello(self, connection, names_list):
        for channel in self.channel_list:
            connection.privmsg(channel, f"hello {names_list}")

def graceful_shutdown(signal, frame):
    logging.info("Shutting down gracefully...")
    sys.exit(0)

if __name__ == "__main__":
    server = "irc.twistednet.org"
    port = 6697  # SSL port
    channels = ["#twisted", "#bots"]
    nickname = "kima"
    username = "black"

    bot = IRCBot(server, port, channels, nickname, username)
    
    signal.signal(signal.SIGINT, graceful_shutdown)
    signal.signal(signal.SIGTERM, graceful_shutdown)

    try:
        bot.start()
    except Exception as e:
        logging.error(f"Bot encountered an error: {e}")
        sys.exit(1)
