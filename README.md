# Kima - My Personal IRC Bot Project

Welcome to Kima, my personal IRC bot project.  
I will be slowly adding functionality and having fun with it. 




## Recent Changes
- **Refactored Code for Modularity**: The main code has been refactored to handle more modular coding.
  - **Additions moved to `/includes/`**: New functionality has been moved to the `/includes/` directory.
  - **Split Functions**: Functions have been split into their own modules for better editing and maintainability.
- **Added Remarks Handling**: Integrated the `Remarks` class to handle insults and compliments.
- **Moved Text Files**: Moved compliments, insults, and quotes into the `/text/` directory for easier editing and adding new content.

## Getting Started

#### Prerequisites

- Python 3.x
- `irc` library: You can install it using pip

  ```bash
  pip install irc

##### Running the Bot

Clone this repository:

```bash
git clone https://github.com/msimism/kima.git
cd kima
```

Run the bot:

```bash
python kima.py
```


