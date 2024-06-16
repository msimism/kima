class Help:
    def __init__(self, command_prefix="."):
        self.command_prefix = command_prefix
        self.commands = {
            "insult": f"{self.command_prefix}insult <nick>: Insult the specified user.",
            "compliment": f"{self.command_prefix}compliment <nick>: Compliment the specified user.",
            "quotes": [
                f"{self.command_prefix}quotes: Get a random quote.",
                f"{self.command_prefix}quotes list: List all quotes.",
                f"{self.command_prefix}quotes read <#>: Read a specific quote by ID.",
                f"{self.command_prefix}quotes del <#>: Delete a quote by ID.",
                f"{self.command_prefix}quotes add <quote> - <author>: Add a new quote."
            ],
            "jokes": [
                f"{self.command_prefix}jokes: Get a random joke.",
                f"{self.command_prefix}jokes list: List all jokes.",
                f"{self.command_prefix}jokes read <#>: Read a specific joke by ID.",
                f"{self.command_prefix}jokes del <#>: Delete a joke by ID.",
                f"{self.command_prefix}jokes add <joke>: Add a new joke."
            ],
            "troll": [
                f"{self.command_prefix}troll add <nick>: Add a user to the trolling list.",
                f"{self.command_prefix}troll remove <nick>: Remove a user from the trolling list."
            ],
            "help": f"{self.command_prefix}help: Display this help message."
        }

    def get_help_message(self):
        help_message = "Available commands:\n"
        for command, description in self.commands.items():
            if isinstance(description, list):
                for desc in description:
                    help_message += f"{desc}\n"
            else:
                help_message += f"{description}\n"
        return help_message
