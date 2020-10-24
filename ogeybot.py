import random
import logging
import time
from telegram.ext import *
from telegram import *
from telegram.ext import MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
updater = Updater('YOUR_TOKEN', use_context=True)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def private(update: Update, context: CallbackContext):
    update.message.reply_text(text="I work only inside groups")

def start(update, context):
    update.message.reply_text("I'm in.")

def ogey(update, context):
    update.message.reply_text("rrat")

def Welcomechat(update, context):
    ID_Supergroup = str(update.message.chat.id)
    Supergroup_name = str(update.message.chat.title)
    if update.message.new_chat_members[0].id == context.bot.id:
        update.message.reply_text(text="Ogey.")


def main():
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.private & Filters.update.message, callback=private))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, callback=Welcomechat))
    dp.add_handler(CommandHandler("Start", start))
    dp.add_handler(MessageHandler(Filters.text("ogey"), ogey))
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()
