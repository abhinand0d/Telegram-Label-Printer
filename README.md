# Telegram Bot for Inventory Management

This is a Telegram bot for managing inventory. It allows users to search for items in the inventory and print labels.

## Requirements
* Python 3.6+
* pyrogram library
* glabels-batch-qt.exe
* TVSE LP45 BPLE Printer

## Installation

1. Clone the repository: `git clone https://github.com/abhinand0d/Telegram-Label-Printer.git`
2. Install the required libraries: `pip install -r requirements.txt`
3. Replace the `API_ID`, `API_HASH`, and `BOT_TOKEN` values in the code with your own values obtained from BotFather.
4. Run the bot: `python main.py`

## Usage

The bot currently supports the following commands:

* `/start`: Sends a welcome message to the user.
* `/search`: Initiates a search for an item in the inventory.
* `/searchline <item> <rate>`: Searches for an item with a specific rate.
* `/🔎 <item> <rate>`: Searches for an item with a specific rate.
* `/findrate`: Asks the user to reply with the rate of the item.
* `/purge`: Deletes all messages in the chat.
* Sending a text message: Used for replying to the bot's prompts.

## Functions

The bot currently supports the following functions:

* `reply_as_inline_for_item_search(item, rate)`: Loads items into inline keyboard button.
* `start_command(client, message)`: Sends a welcome message to the user.
* `search_command(client, message)`: Initiates a search for an item in the inventory.
* `search_command(client, message)`: Searches for an item with a specific rate.
* `search_command(client, message)`: Searches for an item with a specific rate.
* `search_command(client, message)`: Asks the user to reply with the rate of the item.
* `purge_commnad(client,message)`: Deletes all messages in the chat.
* `text_message(client, message)`: Handles text messages from the user.
* `callback_query_handler(client, callback_query)`: Handles callback queries from the keyboard.

## Authors

* Abhinand Dhandapani <abhinanddhandapnai704@gmail.com>

## Thanks
- Pyrogram
- Telegram
- Pyodbc
