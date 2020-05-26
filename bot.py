from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode

from antlr4 import *

from cl.EvalVisitor import *
from cl.SkylineParser import *

from os import path, remove, mkdir, listdir
import pickle


def start(update, context):
    """Funció de la comanda /start. Que saluda a l'usuari."""

    username = update.effective_chat.first_name
    message = "SkylineBot!\nBenvingut " + username + \
        "!\nEnvia /help per a obtenir el llistat de comandes del bot."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def help(update, context):
    """Funció de la comanda /help. Que mostra totes les ordres possibles del bot."""

    message = "A continuació tens un llistat de les comandes que es poden executar en aquest bot:\n\n"
    message += "/start: Es mostrarà el missatge inicial del bot.\n\n"
    message += "/help: Es mostrarà aquest missage un altre cop, en el que pots trobar informació sobre les comandes del bot.\n\n"
    message += "/author: Es mostrarà el nom complet i el correu de qui ha fet aquest bot.\n\n"
    message += "/lst: Es mostrarà els identificadors dels Skylines que tinguis definits en aquell moment.\n\n"
    message += "/clean: Es borraran tots els identificadors dels Skylines que tinguis definits en aquell moment.\n\n"
    message += "/save id: Es guardarà el Skyline que tinguis definit amb l'identificador 'id'.\n\n"
    message += "/load id: Es carregarà el Skyline que tinguis a disc amb l'identificador 'id'.\n\n"

    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def author(update, context):
    """Funció de la comanda /author. Que mostra l'autor del bot i el seu correu."""

    message = "SkylineBot!\n@ Rodrigo Arian Huapaya Sierra, rodrigo.arian.huapaya@est.fib.upc.edu"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def lst(update, context):
    """Funció de la comanda /lst. Que mostra els identificadors de l'usuari."""

    userId = str(update.message.from_user['id'])

    pathOfUserData = "Data/" + userId + "/data.dict"
    if path.exists(pathOfUserData):
        pickle_in = open(pathOfUserData, "rb")
        userData = pickle.load(pickle_in)
        print(userData)
        message = "Aquesta és la llista de identificadors que tens actualment:\n\n"

        for id, sky in userData.items():
            message += "<b>ID:</b> " + id + \
                " | <b>Àrea</b>: " + str(sky.get_area()) + "\n"
            # print(sky.area)

        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)

    else:
        message = "No tens dades per mostrar."
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)


def clean(update, context):
    """Funció de la comanda /clean. Que borra tots els identificadors de l'usuari."""

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
    """Funció de la comanda /save. Que guarda l'identificador \'id\' que especifiqui l'usuari a disc."""

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
            message = "El Skyline amb ID: \'" + \
                skyId + "\' no existeix en les teves dades."
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=message)

    else:
        message = "Les teves dades estan buides actualment.\nPer tant el Skyline \'" + \
            skyId + "\' no existeix."
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)


def load(update, context):
    """Funció de la comanda /load. Que carrega l'identificador \'id\' de disc que especifiqui l'usuari i el borra de disc."""

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


def disk(update, context):
    """Funció de la comanda /disk. Que mostra els identificadors de l'usuari a disc."""

    userId = str(update.message.from_user['id'])

    pathOfUser = "Data/" + userId

    if path.exists(pathOfUser):
        listOfSkies = []

        for file in listdir(pathOfUser):
            if file.endswith(".sky"):
                listOfSkies.append(file[:-4])

        if len(listOfSkies) > 0:
            message = "Aquesta és la llista de Skylines que tens actualment a disc:\n\n"

            for sky in listOfSkies:
                message += "<b>ID:</b> " + sky + "\n"

            context.bot.send_message(
                chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)

        else:
            message = "No tens dades per mostrar a disc."
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=message)
    else:
        message = "No tens dades per mostrar a disc."
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)


def leeElTexto(update, context):
    """
    Funció que es crida per defecte si no s'utilitza cap ordre.\n
    S'encarrega d'analitzar el text donat per a crear un Skyline
    utilitzant les dades que tingui emmagatzemades l'usuari.
    """

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

    imgOrError, height, area = parse(message, userData, userId)

    # Si height és -1, hi ha hagut un error i es comunica d'ell a l'usuari.
    if height == -1:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=imgOrError)

    else:

        sendPhoto(imgOrError, update, context)
        message = "Àrea: " + str(area) + "\n"
        message += "Alçada: " + str(height)

        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)


def sendPhoto(photoOfSkyline, update, context):
    """Funció que envia la imatge d'un Skyline a l'usuari."""

    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(photoOfSkyline, 'rb'))
    remove(photoOfSkyline)


def parse(message, userData, userId):
    """Funció que analitza el missatge enviat per l'usuari per retornar un Skyline"""

    visitor = EvalVisitor(userData, userId)
    print("parsing")
    code = InputStream(message)

    lexer = SkylineLexer(code)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    tree = parser.root()

    imgOrError, height, area = visitor.visit(tree)
    print("parsing done")

    return imgOrError, height, area


# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()


# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dp = updater.dispatcher

# Indica quina funció executa el bot depenen de l'ordre que rebi:
# /start, /help, /author,/lst, /lst, /clean, /save o /load.
dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('help', help))
dp.add_handler(CommandHandler('author', author))
dp.add_handler(CommandHandler('lst', lst))
dp.add_handler(CommandHandler('clean', clean))
dp.add_handler(CommandHandler('save', save))
dp.add_handler(CommandHandler('load', load))
dp.add_handler(CommandHandler('disk', disk))

dp.add_handler(MessageHandler(Filters.text, leeElTexto))

# engega el bot
updater.start_polling()
