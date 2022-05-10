# -*- coding: utf-8 -*-
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())

from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)

def start(update, context):
    ''' START '''
    # Hemen gehitu komandoaren egin beharrekoa
    context.bot.send_message(update.message.chat_id, "Kaixo")

def mezua(update, context):
    # prozesatu mezua
    # https://core.telegram.org/bots/api#message
    text = update.message.text
    # Hemen mezua prozesatu eta beharrezkoa bada zerbait erantzun
    if text.lower().find('errorea')!=-1:
        context.bot.send_message(update.message.chat_id, "Mesedez jarri kontaktuan administratzailearekin")

def main():
    # Hasieraketa
    TOKEN=os.environ.get("TELEGRAM_TOKEN")
    updater=Updater(TOKEN, use_context=True)

    # Robotak erantzungo dituen ebentuak.
    updater.dispatcher.add_handler(CommandHandler('start',	start))
    
    # Mezu jasotzeari harpidetu
    updater.dispatcher.add_handler(MessageHandler(Filters.text, mezua))
    # Arrankatu bot-a. Bi funtzionamendu era polling edo webhook 
    updater.start_polling()
    # updater.start_webhook()
    # Ebentuen zain itxaron
    updater.idle()

if __name__ == '__main__':
    main()

