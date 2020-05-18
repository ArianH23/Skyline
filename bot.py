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

mySkylines = {}
visitor = EvalVisitor(mySkylines)

def start(update, context):
    print(update.effective_chat)
    print(context)
    username = update.effective_chat.first_name
    message = "SkylineBot!\nBenvinlgut " + username + "!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def author(update, context):
    message = "SkylineBot!\n@ Rodrigo Arian Huapaya Sierra, rodrigo.arian.huapaya@est.fib.upc.edu"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def leeElTexto(update, context):
    message = update.message.text

    sky = parse(message)

    sendPhoto(sky, update, context)


def sendPhoto(skyline, update, context):
    
    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(skyline, 'rb'))
    os.remove(skyline)


def parse(message):
    
    code = InputStream(message)
    lexer = SkylineLexer(code)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    tree = parser.root()

    result = visitor.visit(tree)
    return result


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
