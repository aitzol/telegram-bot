# -*- coding: utf-8 -*-

from telegram.ext import (Updater, CommandHandler)

def start(update, context):
    ''' START '''
    # Hemen gehitu komandoaren egin beharrekoa

def main():
    # Hasieraketa
    TOKEN=""
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

