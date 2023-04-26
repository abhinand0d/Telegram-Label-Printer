from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import config
import subprocess
import re
from branch_manager import item_load,expense_load,item_search

# Replace the values with your own API_ID, API_HASH, and TOKEN obtained from BotFather
API_ID = config.API_ID
API_HASH = config.API_HASH
TOKEN = config.BOT_TOKEN

item_name = ""
product_code = ""
price = 0
nos = 0

app = Client(
    "my_bot", 
    api_id=API_ID, 
    api_hash=API_HASH, 
    bot_token=TOKEN
    )

# Load item into inline keyboard button
def reply_as_inline_for_item_search(item,rate):
    item_list = item_search(item,rate)
    keys = []
    for i in item_list:
        keys.append([InlineKeyboardButton(text=f"{str(i[0])} - {str(i[3])}", callback_data=f"{i[0]}|{i[1]}|{i[3]}")])
    keyboard = InlineKeyboardMarkup(keys)
    return keyboard



@app.on_message(filters.command('start'))
def start_command(client, message):
    client.send_message(message.chat.id, 'Hi! Abhi I Love You Mannnn')

@app.on_message(filters.command('search'))
def search_command(client, message):
    # Send a message asking for the search query
    client.send_message(message.chat.id, 'What would you like to search?')

@app.on_message(filters.command('searchline'))
def search_command(client, message):
    # Send a message asking for the search query
    msg = message.text
    msg = msg.split(" ")
    item = msg[1]
    rate = msg[2]
    client.send_message(message.chat.id,f"Let's find the {item} with {rate}")
    client.send_message(message.chat.id, f'Choose Your Poison :', reply_markup=reply_as_inline_for_item_search(item,rate))

@app.on_message(filters.command('🔎'))
def search_command(client, message):
    # Send a message asking for the search query
    msg = message.text
    msg = msg.split(" ")
    item = msg[1]
    rate = msg[2]
    client.send_message(message.chat.id,f"Let's find the {item} with {rate}")
    client.send_message(message.chat.id, f'Choose Your Poison :', reply_markup=reply_as_inline_for_item_search(item,rate))


@app.on_message(filters.command('findrate'))
def search_command(client, message):
    # Send a message asking for the search query
    client.send_message(message.chat.id, 'Reply me the rate')

@app.on_message(filters.command('purge'))
def purge_commnad(client,message):
    chat = client.get_chat(message.chat.id)
    messages = client.get_chat_history(message.chat.id)
    client.delete_messages(message.chat.id ,messages)

@app.on_message(filters.text)
def text_message(client, message):
    if message.reply_to_message and message.reply_to_message.text == 'What would you like to search?':
        # Get the search query from the user's input
        search_query = message.text
        # Send a message asking for the price range
        client.send_message(message.chat.id, f'What is the price range for {search_query}?')

    elif message.reply_to_message and message.reply_to_message.text.startswith('What is the price range for'):
        # Get the price range from the user's input
        price_range = message.text
        # Send a message confirming the search query and price range
        search_query = message.reply_to_message.text.split('for ')[1].rstrip('?')
        client.send_message(message.chat.id, f'Searching for {search_query} within {price_range}...')
        # Send the search results
        client.send_message(message.chat.id, f'Here are the results for {search_query} within {price_range}:', reply_markup=reply_as_inline_for_item_search(search_query,price_range))

    elif message.reply_to_message and message.reply_to_message.text.startswith('Reply with Number of Copies to print'):
        # Get the price range from the user's input
        copies = message.text
        # Confirmation message
        client.send_message(message.chat.id, f'Printing {copies} copies of the selected item')
        client.send_message(message.chat.id, f'Sending it to printer....')
        nos = int(copies)
        subprocess.run(["glabels-batch-qt.exe","--define",f"item={item_name}","--define",f"code={product_code}","--define",f"rs={str(price)}","-c",f"{int(nos)}","./retail.glabels","--printer",'TVSE LP45 BPLE'])
        # Completed Printing
        client.send_message(message.chat.id, f'Printing Completed for {item_name} - {nos} Copies')

    
    elif message.reply_to_message and message.reply_to_message.text == 'Reply me the rate':
        # Get the price range from the user's input
        rate = message.text
        rates = f"50% - {float(rate)*1.50}\n55% - {float(rate)*1.55}\n60% - {float(rate)*1.60}\n65% - {float(rate)*1.65}\n80% - {float(rate)*1.80}\n90% - {float(rate)*1.90}"
        # Send a message asking for the price range
        client.send_message(message.chat.id, rates)



# Define a function to handle callback queries from the keyboard
@app.on_callback_query()
def callback_query_handler(client, query):
    # Get the callback data from the query object
    callback_data = query.data
    # Parse the search term from the callback data
    search_term = callback_data.split('|')
    # Send a message confirming the search term
    print(search_term)
    client.send_message(query.message.chat.id, f'You selected {search_term[0]}')
    item_name = search_term[0]
    product_code = search_term[1]
    price = search_term[2]
    client.send_message(query.message.chat.id, f'Reply with Number of Copies to print')

app.run()
