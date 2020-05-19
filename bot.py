# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from skyline import *
import sys
from antlr4 import *
from SkylineLexer import SkylineLexer
from SkylineParser import SkylineParser
from SkylineVisitor import SkylineVisitor
from EvalVisitor import EvalVisitor
import os
from os import path
import pickle


def start(update, context):
    print(update.effective_chat)
    print(context)
    username = update.effective_chat.first_name
    message = "SkylineBot!\nBenvingut " + username + "!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def author(update, context):
    message = "SkylineBot!\n@ Rodrigo Arian Huapaya Sierra, rodrigo.arian.huapaya@est.fib.upc.edu"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def leeElTexto(update, context):
    message = update.message.text
    print(message)

    userId = str(update.message.from_user['id'])
    
    pathOfDict = "Data/" + userId + ".dict"
    userData = {}

    if path.exists(pathOfDict):
        pickle_in = open(pathOfDict, "rb")
        userData = pickle.load(pickle_in)
        print(userData)

    sky = parse(message, userData, userId)

    sendPhoto(sky, update, context)


def sendPhoto(skyline, update, context):

    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(skyline, 'rb'))
    os.remove(skyline)


def parse(message, userData, userId):
    visitor = EvalVisitor(userData, userId)
    print("parsing")
    code = InputStream(message)

    lexer = SkylineLexer(code)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    tree = parser.root()

    img = visitor.visit(tree)
    return img


# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()


# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dp = updater.dispatcher

# indica que quan el bot rebi la comanda /start o /author s'executi la funció start
dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('author', author))

dp.add_handler(MessageHandler(Filters.text, leeElTexto))

# engega el bot
updater.start_polling()
