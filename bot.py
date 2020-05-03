# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# from telegram import Message, User, Update, Bot as msg, user, update, bot
from skyline import *
# nameOfUser = update.effective_chat.username
import os
# defineix una funció que sal
mySkylines = {}

def start(update, context):
    print (update.effective_chat)
    print (context)
    username = update.effective_chat.first_name
    message = "SkylineBot!\nBenvinlgut " + username + "!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def author(update, context):
    message = "SkylineBot!\n@ Rodrigo Arian Huapaya Sierra, rodrigo.arian.huapaya@est.fib.upc.edu"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def leeElTexto(update, context):
    receivedMessage = update.message.text

    if (mySkylines.__contains__(receivedMessage)):

        sky = mySkylines[receivedMessage]
        
        sendPhoto (sky, update, context)

    elif (receivedMessage.find(":=") >= 0):

        message = receivedMessage.split()
        sky = createNewSkyline(message)

        sendPhoto (sky, update, context)


def sendPhoto(skyline, update, context):
    img = skyline.saveImage()
    context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open(img, 'rb'))
    os.remove(img)

def createNewSkyline(message):
    id = message[0]
    op = message[2]
    val = op[1:-1].split(",")

    for i in range(0, len(val)): 
        val[i] = int(val[i]) 

    sky = Skyline(id, [val[0] ,val[2]], val[1])
    img = sky.saveImage()
    
    print(id +" "+ op)
    print (val)
    mySkylines[id] = sky
    return sky
    
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
