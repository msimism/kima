# Kima IRC Bot

This is Kima, my personal IRC bot project. 
I will slowly add functionality and have fun with it.
Visit us at irc.paniked.net #paniked for further discussion.

## Features

- Responds to commands with insults, compliments, jokes, and quotes.
- Trolling functionality with rotating actions (insult, compliment, flood).
- Modular design for easy addition of new features.
- JSON-based storage for insults, compliments, jokes, and quotes.
- Help command to display available commands.

## Commands

- `.insult [nick]`: Insult a user.
- `.compliment [nick]`: Compliment a user.
- `.quotes`: Get a random quote.
- `.quotes list`: List all quotes.
- `.quotes read [id]`: Read a specific quote.
- `.quotes add [quote]`: Add a new quote.
- `.quotes del [id]`: Delete a specific quote.
- `.quotes search [keyword]`: Search quotes by content.
- `.quotes search -by [author]`: Search quotes by author.
- `.jokes`: Get a random joke.
- `.jokes list`: List all jokes.
- `.jokes read [id]`: Read a specific joke.
- `.jokes add [joke]`: Add a new joke.
- `.jokes del [id]`: Delete a specific joke.
- `.troll add [nick]`: Add a user to the troll list.
- `.troll remove [nick]`: Remove a user from the troll list.
- `.troll list`: List all users being trolled.
- `.help`: Show help message.

## Setup

1. Clone the repository: `git clone https://github.com/msimism/kima.git`
2. Navigate to the project directory: `cd kima`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the bot: `python kima.py`

## Configuration

- Command prefix can be changed by modifying the `prefix` parameter in `CommandHandler`.

## Contributing

Feel free to submit issues or pull requests. Let's make Kima better together!

## License

This project is licensed under the MIT License.
