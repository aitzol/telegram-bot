# -*- coding: utf-8 -*-
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())

from telegram.ext import (Updater, CommandHandler)

def start(update, context):
    ''' START '''
    # Hemen gehitu komandoaren egin beharrekoa
    context.bot.send_message(update.message.chat_id, "Kaixo")
    
def main():
    # Hasieraketa
    TOKEN=os.get("TELEGRAM_TOKEN")
    updater=Updater(TOKEN, use_context=True)

    # Robotak erantzungo dituen ebentuak.
    updater.dispatcher.add_handler(CommandHandler('start',	start))

    # Arrankatu bot-a. Bi funtzionamendu era polling edo webhook 
    updater.start_polling()
    # updater.start_webhook()
    # Ebentuen zain itxaron
    updater.idle()

if __name__ == '__main__':
    main()

