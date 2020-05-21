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
from telegram import ParseMode


def start(update, context):

    username = update.effective_chat.first_name
    message = "SkylineBot!\nBenvingut " + username + "!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def save(update, context):
    id = update.message.text.split()[1]
    userId = str(update.message.from_user['id'])

    userPath = "Data/" + userId

    if path.exists(userPath):
        pickle_in = open(userPath + "/data.dict", "rb")
        userData = pickle.load(pickle_in)

        if id in userData:
            skyToSave = userData.get(id)

            pickle_out = open(userPath + "/" + id + ".sky", "wb")
            pickle.dump(skyToSave, pickle_out)
            pickle_out.close()

            message = "Skyline amb identificador " + id + " guardat correctament a disc!"
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=message)

        else:
            message = "El Skyline amb identificador " + id + \
                " no existeix. Per tant encara no es pot començar a guardar res"
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=message)

    else:
        message = "Encara no s'ha assignat cap variable."
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)


def lst(update, context):
    userId = str(update.message.from_user['id'])

    userPath = "Data/" + userId
    if path.exists(userPath):

        pickle_in = open(userPath + "/data.dict", "rb")
        userData = pickle.load(pickle_in)

        message = "Aquesta és la llista de identificadors que tens actualment:\n\n"

        for id, sky in userData.items():
            message += "<i>ID:</i> " + id + " | <i>Àrea</i>: " + str(sky.get_area()) + " altura" + str(sky.get_height()) + "\n"
            print(sky.area)

        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)

    else:
        message = "Encara no s'ha començat a utilitzar el programa."
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)


def author(update, context):
    message = "SkylineBot!\n@ Rodrigo Arian Huapaya Sierra, rodrigo.arian.huapaya@est.fib.upc.edu"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def leeElTexto(update, context):
    message = update.message.text
    print(message)

    userId = str(update.message.from_user['id'])

    pathOfUser = "Data/" + userId
    userData = {}

    if path.exists(pathOfUser):
        pickle_in = open(pathOfUser + "/data.dict", "rb")
        userData = pickle.load(pickle_in)
        print(userData)

    else:
        os.mkdir(pathOfUser)

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

# indica que quan el bot rebi la comanda /start, /author, /save,
# /load, /lst, /clear s'executi la funció start
dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('author', author))
dp.add_handler(CommandHandler('save', save))
dp.add_handler(CommandHandler('lst', lst))

dp.add_handler(MessageHandler(Filters.text, leeElTexto))

# engega el bot
updater.start_polling()
