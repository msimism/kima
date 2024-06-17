# CHANGELOG

## TODO

- **Improve error handling**
- **Add more insult and compliment messages**
- **Enhance quote and joke management features**
- **Implement additional commands and functionalities**

## Recent Changes

### Updates

- **Refactored Code for Modularity**: The main code has been refactored to handle more modular coding.
  - **Additions moved to `/includes/`**: New functionality has been moved to the `/includes/` directory.
  - **Split Functions**: Functions have been split into their own modules for better editing and maintainability.
- **Added Remarks Handling**: Integrated the `Remarks` class to handle insults and compliments.
- **Moved Text Files**: Moved compliments, insults, and quotes into the `/data/remarks/` directory for easier editing and adding new content.
- **Command Prefix Configuration**: Made command prefix easily configurable.
- **Added Logging**: Added detailed logging for each module to aid in debugging and maintenance.
- **Enhanced Trolling Functionality**: Improved the `Troll` class to rotate between insults, compliments, and floods.
- **JSON-based Storage**: Updated storage for insults, compliments, jokes, and quotes to use JSON format.
- **Help Command**: Added a `.help` command to display available commands.

### Fixes

- **Fixed Carriage Return Issue**: Updated command handling to split multi-line messages, preventing the `Carriage returns not allowed in privmsg(text)` error.
- **Error Handling for Quotes and Jokes**: Improved error handling for quote and joke ID operations.
- **Trolling Actions Logging**: Added logging to track trolling actions and ensure they are executed properly.
- **Fixed Loading Issues**: Corrected issues with loading quotes and jokes from JSON files.
