# -*- coding: utf-8 -*-
from dotenv import load_dotenv, find_dotenv
from ping3 import ping
import os
load_dotenv(find_dotenv())

from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start(update, context):
    ''' START '''
    # Hemen gehitu komandoaren egin beharrekoa
    context.bot.send_message(update.message.chat_id, "Kaixo")

def egin_ping(update, context):
    """ 
    Komando honekin ping bat egingo dugu parametro bezala jasotako ip-ra
    eta erantzuna bueltatu
    """
    # Komandoaren parametroak context.args zerrendan jasoko ditugu
    if len(context.args):
        ip = context.args[0]
        response = ping(ip)
        if response==False:
            msg = 'Host unknown'
        elif response == None:
            msg = "Host time out"
        else:
            msg = "Ping ok"
    else:
        msg = "Zein ip-tara?"
    context.bot.send_message(update.message.chat_id, msg)


def mezua(update, context):
    # prozesatu mezua
    # https://core.telegram.org/bots/api#message
    text = update.message.text
    # Hemen mezua prozesatu eta beharrezkoa bada zerbait erantzun
    if text.lower().find('errorea')!=-1:
        keyboard = [
            [
                InlineKeyboardButton("Inprimagailua", callback_data="1"),
                InlineKeyboardButton("Sarea", callback_data="2"),
            ],
            [InlineKeyboardButton("Beste bat", callback_data="3")],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("Non dago errorea?: ", reply_markup=reply_markup)

def botoiari_erantzun(update, context):
    """ Hemen prozesatuko dira teklatuak bidalitako aukerak"""
    query = update.callback_query
    if query.data == '1':
        msg = "Inprimagailu arduradunari abisatu diogu"
        # Hemen benetan abisua pasa ;)
    elif query.data == '2':
        msg = "Sare arduradunari abisatu diogu"
    else:
        msg = "Monitorizazio tresnak aztertzen ari gara."
    query.edit_message_text(msg)
    
def main():
    # Hasieraketa
    TOKEN=os.environ.get("TELEGRAM_TOKEN")
    updater=Updater(TOKEN, use_context=True)

    # Robotak erantzungo dituen ebentuak.
    updater.dispatcher.add_handler(CommandHandler('start',	start))
    updater.dispatcher.add_handler(CommandHandler('ping', egin_ping))
    updater.dispatcher.add_handler(CallbackQueryHandler(botoiari_erantzun))
    # Mezu jasotzeari harpidetu
    updater.dispatcher.add_handler(MessageHandler(Filters.text, mezua))
    # Arrankatu bot-a. Bi funtzionamendu era polling edo webhook 
    updater.start_polling()
    # updater.start_webhook()
    # Ebentuen zain itxaron
    updater.idle()

if __name__ == '__main__':
    main()

