#python-telegram-bot
from logging import error
from telegram.ext import chatmemberhandler
from telegram.ext import *
import Responses as R
import pandas as panda
import requests
import json

keys = '5069133621:AAFPBhlDlhf-40XYNDJuzpKDDhAAtk8XOdc'

def start_command(update, context):
    update.message.reply_text('''
    my command:\n/unnotify to stop getting Timeline notification\n/help to get help
    ''')

def help_command(update, context):
    update.message.reply_text('Work In Progress')

#def cmd(update, context):

def unnotify_command(update, context):
    chat_id = update.message.chat_id
    update.message.reply_text(chat_id)


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_response(text)
    update.message.reply_text(response)

def error(update, context):
   print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('unnotify', unnotify_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)


    updater.start_polling()
    updater.idle()

print('Bot Running')
main()

