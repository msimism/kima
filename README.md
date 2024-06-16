# Kima - IRC Bot

This is Kima, my personal IRC bot project. 
I will slowly add functionality and have fun with it. Visit us at `irc.paniked.net #paniked` for further discussion.

## Features

- **Insults**: Random insults generated using the `Remarks` class.
- **Compliments**: Random compliments generated using the `Remarks` class.
- **Quotes**: Manage quotes with commands to add, remove, list, read, and get a random quote.
- **Jokes**: Manage jokes with commands to add, remove, list, read, and get a random joke.
- **Trolling**: Random troll messages generated using the `Troll` class.

## Commands

### Insults
- `.insult <nick>`: Insult the specified user.

### Compliments
- `.compliment <nick>`: Compliment the specified user.

### Quotes
- `.quotes`: Get a random quote.
- `.quotes list`: List all quotes.
- `.quotes read <#>`: Read a specific quote by ID.
- `.quotes del <#>`: Delete a quote by ID.
- `.quotes add <quote> - <author>`: Add a new quote.

### Jokes
- `.jokes`: Get a random joke.
- `.jokes list`: List all jokes.
- `.jokes read <#>`: Read a specific joke by ID.
- `.jokes del <#>`: Delete a joke by ID.
- `.jokes add <joke>`: Add a new joke.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/kima.git
    ```
2. Navigate to the project directory:
    ```bash
    cd kima
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Edit the `main.py` file to set your server, port, channels, nickname, username, and command prefix.

## Usage

Run the bot:
```bash
python kima.py
