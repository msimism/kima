""" Main module to run the Kima IRC bot """
""" Module Imports """
from includes.command_handler import CommandHandler
from includes.remarks import Remarks
from includes.quotes import Quotes
from includes.jokes import Jokes
from includes.troll import Troll
from includes.help import Help
from includes.logger import Logger
""" Module Imports """

""" Library Imports """
import irc.bot
import ssl
import time
import sys
import signal
import argparse
import logging  # Ensure logging is imported
""" Library Imports """

# Parse command line arguments
parser = argparse.ArgumentParser(description='Run Kima IRC Bot')
parser.add_argument('--debug', help='Module to debug (e.g., troll, command_handler, all)', default=None)
args = parser.parse_args()

# Configure logging
log_file = "kima.log"
debug_modules = ['includes.quotes', 'includes.command_handler', 'includes.troll', 'includes.remarks', 'includes.jokes', 'includes.help'] if args.debug == 'all' else [f'includes.{args.debug.lower()}']
logger = Logger('kima', level=logging.DEBUG if args.debug else logging.INFO, log_file=log_file, debug_modules=debug_modules).get_logger()

class IRCBot(irc.bot.SingleServerIRCBot):
    def __init__(self, server, port, channels, nickname, username):
        ssl_factory = irc.connection.Factory(wrapper=ssl.wrap_socket)
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, username, connect_factory=ssl_factory)
        self.channel_list = channels
        self.channels = {}  # this dictionary will hold the channel objects
        self.remarks = Remarks()
        self.troll = Troll(self.remarks)
        self.quotes = Quotes()
        self.jokes = Jokes()
        self.help = Help()
        self.command_handler = CommandHandler(self.remarks, self.quotes, self.jokes, self.troll, self.help)

    def on_welcome(self, connection, event):
        for channel in self.channel_list:
            connection.join(channel)

    def on_pubmsg(self, connection, event):
        message = event.arguments[0]
        sender = irc.client.NickMask(event.source).nick
        channel = event.target

        self.command_handler.handle_message(connection, channel, sender, message)

    def on_disconnect(self, connection, event):
        logger.info("Disconnected from the server. Reconnecting...")
        time.sleep(10)
        self.reconnect()

    def reconnect(self):
        server, port = self.connection.server_list[0]
        self.connection.connect(server, port, self.connection.nick, self.connection.username)
    
    def hello(self, connection, names_list):
        for channel in self.channel_list:
            connection.privmsg(channel, f"hello {names_list}")

if __name__ == "__main__":
    server = "irc.paniked.net"
    port = 6697  # SSL port
    channels = ["#paniked"]
    nickname = "kima"
    username = "black"

    bot = IRCBot(server, port, channels, nickname, username)
    try:
        bot.start()
    except KeyboardInterrupt:
        sys.exit("Bye")
