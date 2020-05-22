# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from skyline import *
import sys
from antlr4 import *

from EvalVisitor import *
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

    if path.exists(userPath + "/data.dict"):
        pickle_in = open(userPath + "/data.dict", "rb")
        userData = pickle.load(pickle_in)

        if id in userData:
            skyToSave = userData.get(id)

            pickle_out = open(userPath + "/" + id + ".sky", "wb")
            pickle.dump(skyToSave, pickle_out)
            pickle_out.close()

            message = "Skyline amb ID: \'" + id + "\' guardat correctament a disc!"
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=message)

        else:
            message = "El Skyline amb identificador ID: \'" + id +"\' no existeix en les teves dades."
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=message)

    else:
        message = "Les teves dades estan buides actualment.\nPer tant el Skyline \'" + id + "\' no existeix."
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)


def lst(update, context):
    userId = str(update.message.from_user['id'])

    userPath = "Data/" + userId
    print(path.exists(userPath))
    if path.exists(userPath + "/data.dict"):

        pickle_in = open(userPath + "/data.dict", "rb")
        userData = pickle.load(pickle_in)

        message = "Aquesta és la llista de identificadors que tens actualment:\n\n"

        for id, sky in userData.items():
            message += "<i>ID:</i> " + id + " | <i>Àrea</i>: " + str(sky.get_area()) + "\n"
            print(sky.area)

        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)

    else:
        message = "No tens dades per mostrar."
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
        if path.exists(pathOfUser + "/data.dict"):
            pickle_in = open(pathOfUser + "/data.dict", "rb")
            userData = pickle.load(pickle_in)
            print(userData)

    else:
        os.mkdir(pathOfUser)

    img, height, area = parse(message, userData, userId)

    sendPhoto(img, update, context)
    message = "Àrea: " + str(area) + "\n"
    message += "Alçada: " + str(height)

    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


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

    img, height, area = visitor.visit(tree)
    print("parsing done")

    return img ,height, area

def clean(update, context):
    userId = str(update.message.from_user['id'])

    pathOfUserData = "Data/" + userId + "/data.dict"

    if path.exists(pathOfUserData):
        os.remove(pathOfUserData)

        message = "Les teves dades s'han esborrat correctament!"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    else:
        message = "No tens dades a borrar"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def load(update, context):
    userId = str(update.message.from_user['id'])
    id = update.message.text.split()[1]

    pathOfUserData = "Data/" + userId + "/data.dict"
    pathOfUserSky = "Data/" + userId + "/"+ id +".sky"

    userData = {}

    if path.exists(pathOfUserSky):
        if path.exists(pathOfUserData):
            pickle_in_data = open(pathOfUserData, "rb")
            userData = pickle.load(pickle_in_data)
        
        pickle_in_sky = open(pathOfUserSky, "rb")
        sky = pickle.load(pickle_in_sky)

        userData[id] = sky

        pickle_out = open(pathOfUserData, "wb")
        pickle.dump(userData, pickle_out)
        pickle_out.close()

        os.remove(pathOfUserSky)
        
        message = "S'ha carregat correctament el Skyline amb ID: \'"+ id +"\' a les teves dades i s'ha esborrat de disc!" 
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    else:
        message = "El Skyline amb ID: \'"+ id +"\' no existeix a disc." 
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)


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
dp.add_handler(CommandHandler('clean', clean))
dp.add_handler(CommandHandler('load', load))

dp.add_handler(MessageHandler(Filters.text, leeElTexto))

# engega el bot
updater.start_polling()
