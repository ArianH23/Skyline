# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from skyline import *
from antlr4 import *

from cl.EvalVisitor import *
from os import path, remove, mkdir
import pickle
from telegram import ParseMode


def start(update, context):

    username = update.effective_chat.first_name
    message = "SkylineBot!\nBenvingut " + username + \
        "!\nEnvia /help per a obtenir el llistat de comandes del bot."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def help(update, context):
    message = "A continuació tens un llistat de les comandes que es poden executar en aquest bot:\n\n"
    message += "/start: Es mostrarà el missatge inicial del bot.\n\n"
    message += "/help: Es mostrarà aquest missage un altre cop en el que pots trobar informació sobre les comandes del bot.\n\n"
    message += "/author: Es mostrarà el nom complet i el correu de qui ha fet aquest bot.\n\n"
    message += "/lst: Es mostrarà els identificadors dels Skylines que tinguis definits en aquell moment.\n\n"
    message += "/clean: Es borraran tots els identificadors dels Skylines que tinguis definits en aquell moment.\n\n"
    message += "/save id: Es guardarà el Skyline que tinguis definit amb l'identificador 'id'.\n\n"
    message += "/load id: Es carregarà el Skyline que tinguis a disc amb l'identificador 'id'.\n\n"

    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def author(update, context):
    message = "SkylineBot!\n@ Rodrigo Arian Huapaya Sierra, rodrigo.arian.huapaya@est.fib.upc.edu"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def lst(update, context):
    userId = str(update.message.from_user['id'])

    pathOfUserData = "Data/" + userId + "/data.dict"
    if path.exists(pathOfUserData):
        pickle_in = open(pathOfUserData , "rb")
        userData = pickle.load(pickle_in)
        print(userData)
        message = "Aquesta és la llista de identificadors que tens actualment:\n\n"

        for id, sky in userData.items():
            message += "<i>ID:</i> " + id + \
                " | <i>Àrea</i>: " + str(sky.get_area()) + "\n"
            print(sky.area)

        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)

    else:
        message = "No tens dades per mostrar."
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)


def clean(update, context):
    userId = str(update.message.from_user['id'])

    pathOfUserData = "Data/" + userId + "/data.dict"

    if path.exists(pathOfUserData):
        remove(pathOfUserData)

        message = "Les teves dades s'han esborrat correctament!"
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)
    else:
        message = "No tens dades a borrar"
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)


def save(update, context):
    userId = str(update.message.from_user['id'])
    skyId = update.message.text.split()[1]

    pathOfUserData = "Data/" + userId + "/data.dict"
    pathOfUserSky = "Data/" + userId + "/" + skyId + ".sky"

    if path.exists(pathOfUserData):
        pickle_in_data = open(pathOfUserData, "rb")
        userData = pickle.load(pickle_in_data)

        if skyId in userData:
            skyToSave = userData.get(skyId)

            pickle_out_sky = open(pathOfUserSky, "wb")
            pickle.dump(skyToSave, pickle_out_sky)
            pickle_out_sky.close()

            message = "Skyline amb ID: \'" + skyId + "\' guardat correctament a disc!"
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=message)

        else:
            message = "El Skyline amb identificador ID: \'" + \
                skyId + "\' no existeix en les teves dades."
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=message)

    else:
        message = "Les teves dades estan buides actualment.\nPer tant el Skyline \'" + \
            skyId + "\' no existeix."
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)


def load(update, context):
    userId = str(update.message.from_user['id'])
    skyId = update.message.text.split()[1]

    pathOfUserData = "Data/" + userId + "/data.dict"
    pathOfUserSky = "Data/" + userId + "/" + skyId + ".sky"

    userData = {}

    if path.exists(pathOfUserSky):

        if path.exists(pathOfUserData):
            pickle_in_data = open(pathOfUserData, "rb")
            userData = pickle.load(pickle_in_data)

        pickle_in_sky = open(pathOfUserSky, "rb")
        sky = pickle.load(pickle_in_sky)

        userData[skyId] = sky

        pickle_out = open(pathOfUserData, "wb")
        pickle.dump(userData, pickle_out)
        pickle_out.close()

        remove(pathOfUserSky)

        message = "S'ha carregat correctament el Skyline amb ID: \'" + \
            skyId + "\' a les teves dades i s'ha esborrat de disc!"
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)
    else:
        message = "El Skyline amb ID: \'" + skyId + "\' no existeix a disc."
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)


def leeElTexto(update, context):
    message = update.message.text
    print(message)

    userId = str(update.message.from_user['id'])

    pathOfUser = "Data/" + userId
    pathOfUserData = "Data/" + userId + "/data.dict"

    userData = {}

    if path.exists(pathOfUser):
        if path.exists(pathOfUserData):
            pickle_in = open(pathOfUserData, "rb")
            userData = pickle.load(pickle_in)
            print(userData)

    else:
        mkdir(pathOfUser)

    img, height, area = parse(message, userData, userId)

    if height == -1:
        context.bot.send_message(chat_id=update.effective_chat.id, text=img)

    else:

        sendPhoto(img, update, context)
        message = "Àrea: " + str(area) + "\n"
        message += "Alçada: " + str(height)

        context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def sendPhoto(skyline, update, context):

    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(skyline, 'rb'))
    remove(skyline)


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

    return img, height, area



# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()


# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dp = updater.dispatcher

# indica que quan el bot rebi la comanda /start, /help, /author,
# /lst, /lst, /clean, /save o /load s'executi la funció start
dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('help', help))
dp.add_handler(CommandHandler('author', author))
dp.add_handler(CommandHandler('lst', lst))
dp.add_handler(CommandHandler('clean', clean))
dp.add_handler(CommandHandler('save', save))
dp.add_handler(CommandHandler('load', load))

dp.add_handler(MessageHandler(Filters.text, leeElTexto))

# engega el bot
updater.start_polling()
