# Kima IRC Bot

This is Kima, my personal IRC bot project. 
I will slowly add functionality and have fun with it.
Visit us at irc.paniked.net #paniked for further discussion.

## Features

- **Insults and Compliments**: Integrated the `Remarks` class to handle insults and compliments.
- **Quotes Management**: Add, list, read, and delete quotes.
- **Jokes Management**: Add, list, read, and delete jokes.
- **Trolling Management**: Rotate between different trolling behaviors like insults, compliments, and flooding.

## Commands

- **Insults**: `.insult <nick>`
- **Compliments**: `.compliment <nick>`
- **Quotes**:
  - `.quotes` - Get a random quote.
  - `.quotes list` - List all quotes.
  - `.quotes read <#>` - Read a specific quote by ID.
  - `.quotes del <#>` - Delete a quote by ID.
  - `.quotes add <quote> - <author>` - Add a new quote.
- **Jokes**:
  - `.jokes` - Get a random joke.
  - `.jokes list` - List all jokes.
  - `.jokes read <#>` - Read a specific joke by ID.
  - `.jokes del <#>` - Delete a joke by ID.
  - `.jokes add <joke>` - Add a new joke.
- **Trolling**:
  - `.troll add <nick>` - Add a user to the trolling list.
  - `.troll remove <nick>` - Remove a user from the trolling list.
- **Help**: `.help` - Display this help message.

## Recent Changes

### Updates

- **Refactored CommandHandler for Troll Management**:
  - Added a list of troll subclasses and a variable to track the next troll subclass to use.
  - Updated the `handle_troll_command` method to add and remove users from the trolling list, rotating through the troll subclasses.
  - Implemented `add_user_to_troll` method to add a user to the next troll subclass in the rotation.
  - Implemented `remove_user_from_troll` method to remove a user from all troll subclasses.
- **Added Debug Logging**:
  - Added debug logging to the `IRCBot` class to trace the handling of `privnotice` events.
  - Enhanced logging in `CommandHandler` to debug command handling and trolling actions.
- **Ensured `privnotice` Handling**:
  - Verified and ensured the `on_privnotice` method is registered to handle notice events.
  - Added a global handler for `privnotice` events in the `IRCBot` class.
- **Implemented Graceful Shutdown**:
  - Added signal handling to ensure the bot shuts down gracefully on receiving termination signals.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/kima.git
   cd kima
