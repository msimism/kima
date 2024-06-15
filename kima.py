import irc.bot, irc.client, ssl, time, re
import random, sys
#test
class Remarks:
    def __init__(self):
        with open("/text/insults.txt", "r") as insultfile:
            self.insults = [line.strip() for line in insultfile.readlines()]
        with open("/text/compliments.txt", "r") as complimentsfile:
            self.compliments = [line.strip() for line in complimentsfile.readlines()]
            
        
    def load(self, file):
        with open(file, "r") as new_insultfile:
            new_insults = [line.strip() for line in new_insultfile.readlines()]
            self.insults.extend(new_insults)
        with open(file, "r") as new_complimentsfile:
            new_compliments = [line.strip() for line in new_complimentsfile.readlines()]
            self.compliments.extend(new_compliments)

    def random_insult(self):
        return random.choice(self.insults)
        
    def random_compliment(self):
        return random.choice(self.compliments)
    
    def insult(self, nick):
        random_insult = self.random_insult()
        return f"{nick}, {random_insult}"
    
    def compliment(self, nick):
        random_compliment = self.random_compliment()
        return f"{nick}, {random_compliment}"



    
class IRCBot(irc.bot.SingleServerIRCBot):
    def __init__(self, server, port, channel, nickname, username):
        ssl_factory = irc.connection.Factory(wrapper=ssl.wrap_socket)
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, username, connect_factory=ssl_factory)
        self.channel = channel
        self.remarks = Remarks()
        

    def on_welcome(self, connection, event):
        connection.join(self.channel)

    #def on_join(self, connection, event):
    #    connection.privmsg(self.channel, "Hi Panik! I'm your biggest fan")

    def on_pubmsg(self, connection, event):
        message = event.arguments[0]
        sender = irc.client.NickMask(event.source).nick
        channel = event.target
        
        # Regular expression pattern to match words
        pattern = r'\b[A-Za-z]+\b'
        
        if "!hello" in message.lower():
            names = re.findall(pattern, message)
            if len(names) > 1:  # to ensure we have names after !hello
                names_list = ', '.join(names[1:])  # Skip the command itself
                self.hello(connection, names_list)
            else:
                connection.privmsg(self.channel, "No names found to greet.")
        elif message.lower().startswith("!insult"):
            parts = message.split()
            if len(parts) > 1:
                nick = parts[1]
                insult_message = self.remarks.insult(nick)
                connection.privmsg(self.channel, insult_message)
        elif message.lower().startswith("!compliment"):
            parts = message.split()
            if len(parts) > 1:
                nick = parts[1]
                insult_message = self.remarks.compliment(nick)
                connection.privmsg(self.channel, insult_message)
        else:
            print(f"{channel} - {sender} - {message}")


    def on_disconnect(self, connection, event):
        print("Disconnected from the server. Reconnecting...")
        time.sleep(10)
        self.reconnect()

    def reconnect(self):
        server, port = self.connection.server_list[0]
        self.connection.connect(server, port, self.connection.nick, self.connection.username)
    
    def hello(self, connection, names_list):
        connection.privmsg(self.channel, f"hello {names_list}")
        

if __name__ == "__main__":
    server = "irc.twistednet.org"
    port = 6697  # SSL port
    channel = "#paniked"
    nickname = "kima"
    username = "black"

    bot = IRCBot(server, port, channel, nickname, username)
    try:
        bot.start()
    except KeyboardInterrupt:
        sys.exit("Bye")