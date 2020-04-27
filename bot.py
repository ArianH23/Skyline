# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler, MessageHandler
# from telegram import Message, User, Update, Bot as msg, user, update, bot

# nameOfUser = update.effective_chat.username

# defineix una funció que sal


def start(update, context):
    print (update.effective_chat)
    print (context)
    username = update.effective_chat.first_name
    message = "SkylineBot!\nBenvinlgut " + username + "!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()


def author(update, context):
    message = "SkylineBot!\n@ Rodrigo Arian Huapaya Sierra, rodrigo.arian.huapaya@est.fib.upc.edu"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# indica que quan el bot rebi la comanda /start s'executi la funció start
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('author', author))

# engega el bot
updater.start_polling()
