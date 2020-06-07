from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode

from antlr4 import *

from cl.EvalVisitor import *
from cl.SkylineParser import *

from os import path, remove, mkdir, listdir
import pickle

# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()

# Diccionari que guardará la taula de simbols de cada usuari que interactui amb el bot durant la sessió.
listOfDictsCurrentSession = {}


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
    message += "<b>NOU</b> /disk: Es mostrarà els Skylines que tinguis a dic en aquell moment."

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)


def author(update, context):
    """Funció de la comanda /author. Que mostra l'autor del bot i el seu correu."""

    message = "SkylineBot!\n@ Rodrigo Arian Huapaya Sierra, rodrigo.arian.huapaya@est.fib.upc.edu"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def lst(update, context):
    """Funció de la comanda /lst. Que mostra els identificadors de l'usuari."""
    username = update.effective_chat.first_name
    last_nameI = ""

    # Comproba si l'usuari té cognom.
    if not update.effective_chat.last_name is None:
        last_nameI = update.effective_chat.last_name[0]

    # Ultims 5 digits del ID de telegram de l'usuari
    id = str(update.message.from_user['id'])[-5:]

    userId = username + last_nameI + id

    # Comproba si l'usuari té dades en la sessió actual
    if userId in listOfDictsCurrentSession:

        userData = listOfDictsCurrentSession[userId]

        message = "Aquesta és la llista de identificadors que tens actualment a la teva taula de simbols:\n\n"

        for id, sky in userData.items():
            message += "<b>ID:</b> " + id + \
                " | <b>Àrea</b>: " + str(sky.get_area()) + "\n"

        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.HTML)

    else:
        message = "No tens dades per mostrar a la teva taula de simbols."
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)


def clean(update, context):
    """Funció de la comanda /clean. Que borra tots els identificadors de l'usuari."""
    username = update.effective_chat.first_name
    last_nameI = ""

    # Comproba si l'usuari té cognom.
    if not update.effective_chat.last_name is None:
        last_nameI = update.effective_chat.last_name[0]

    # Ultims 5 digits del ID de telegram de l'usuari
    id = str(update.message.from_user['id'])[-5:]

    userId = username + last_nameI + id

    # Comproba si l'usuari té dades en la sessió actual
    if userId in listOfDictsCurrentSession:
        del listOfDictsCurrentSession[userId]

        message = "Les teves dades s'han esborrat correctament!"
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)
    else:
        message = "No tens dades a borrar"
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)


def save(update, context):
    """Funció de la comanda /save. Que guarda l'identificador \'id\' que especifiqui l'usuari a disc."""
    username = update.effective_chat.first_name
    last_nameI = ""

    # Comproba si l'usuari té cognom.
    if not update.effective_chat.last_name is None:
        last_nameI = update.effective_chat.last_name[0]

    # Ultims 5 digits del ID de telegram de l'usuari
    id = str(update.message.from_user['id'])[-5:]

    userId = username + last_nameI + id
    skyId = update.message.text.split()[1]

    pathOfUserSky = "Data/" + userId + "/" + skyId + ".sky"

    # Comproba si l'usuari té dades en la sessió actual
    if userId in listOfDictsCurrentSession:

        userData = listOfDictsCurrentSession[userId]

        # Comproba que el ID del Skyline existeix a les dades de l'usuari
        if skyId in userData:
            skyToSave = userData[skyId]

            pickle_out_sky = open(pathOfUserSky, "wb")
            pickle.dump(skyToSave, pickle_out_sky)
            pickle_out_sky.close()

            message = "El Skyline amb ID: \'" + skyId + "\' guardat correctament a disc!"
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

    username = update.effective_chat.first_name
    last_nameI = ""

    # Comproba si l'usuari té cognom.
    if not update.effective_chat.last_name is None:
        last_nameI = update.effective_chat.last_name[0]

    # Ultims 5 digits del ID de telegram de l'usuari
    id = str(update.message.from_user['id'])[-5:]

    userId = username + last_nameI + id
    skyId = update.message.text.split()[1]

    pathOfUserSky = "Data/" + userId + "/" + skyId + ".sky"

    userData = {}

    # Comproba si el directori de l'usuari existeix a disc.
    if path.exists(pathOfUserSky):

        # Comproba si l'usuari té dades en la sessió actual
        if userId in listOfDictsCurrentSession:
            userData = listOfDictsCurrentSession[userId]

        pickle_in_sky = open(pathOfUserSky, "rb")
        sky = pickle.load(pickle_in_sky)

        userData[skyId] = sky

        remove(pathOfUserSky)

        listOfDictsCurrentSession[userId] = userData

        message = "S'ha carregat correctament el Skyline amb ID: \'" + \
            skyId + "\' a la teva taula de simbols de la sessió actual i s'ha esborrat de disc!"
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)
    else:
        message = "El Skyline amb ID: \'" + skyId + "\' no existeix a disc."
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)


def disk(update, context):
    """Funció de la comanda /disk. Que mostra els identificadors de l'usuari a disc."""

    username = update.effective_chat.first_name
    last_nameI = ""

    # Comproba si l'usuari té cognom.
    if not update.effective_chat.last_name is None:
        last_nameI = update.effective_chat.last_name[0]

    # Ultims 5 digits del ID de telegram de l'usuari
    id = str(update.message.from_user['id'])[-5:]

    userId = username + last_nameI + id

    pathOfUser = "Data/" + userId

    # Comproba si el directori de l'usuari existeix a disc.
    if path.exists(pathOfUser):
        listOfSkies = []

        for file in listdir(pathOfUser):
            # Suposarem que només hi ha Skylines a la seva carpeta
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

    username = update.effective_chat.first_name
    last_nameI = ""

    # Comproba si l'usuari té cognom.
    if not update.effective_chat.last_name is None:
        last_nameI = update.effective_chat.last_name[0]

    # Ultims 5 digits del ID de telegram de l'usuari
    id = str(update.message.from_user['id'])[-5:]

    userId = username + last_nameI + id

    pathOfUser = "Data/" + userId

    userData = {}

    # Comproba si l'usuari té dades en la sessió actual
    if userId in listOfDictsCurrentSession:
        userData = listOfDictsCurrentSession[userId]

    # Si el directori de l'usuari no existeix a disc, es crea.
    if not path.exists(pathOfUser):
        mkdir(pathOfUser)

    imgOrError, height, area = parse(message, userData, userId)

    # Guarda la nova taula de simbols de l'usuari
    listOfDictsCurrentSession[userId] = userData

    # Si height és -1, hi ha hagut un error i es comunica d'ell a l'usuari.
    if height == -1:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=imgOrError)

    # Si no hi ha hagut cap error, s'envia una imatge del Skyline, la seva àrea, i la seva alçada.
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
    """Funció que analitza el missatge enviat per l'usuari per retornar un Skyline en cas que el missatge sigui correcte."""

    visitor = EvalVisitor(userData, userId)

    code = InputStream(message)
    lexer = SkylineLexer(code)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    tree = parser.root()

    imgOrError, height, area = visitor.visit(tree)

    return imgOrError, height, area


# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dp = updater.dispatcher

# Indica quina funció executa el bot depenen de l'ordre que rebi:
# /start, /help, /author,/lst, /lst, /clean, /save, /load o /disk.
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
