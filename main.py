#!/usr/bin/env python3
from telegram.ext import (run_async, Updater, CallbackQueryHandler, CommandHandler, MessageHandler, ConversationHandler, Filters, PicklePersistence)
from telegram import (ChatAction, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ParseMode)
import logging, os, sys, toml, time, string
from threading import Thread

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)

config = toml.load("./config.toml")


def start(update, context):
    username = update.message.from_user.username
    user_id = update.message.from_user.id

    logging.info("/start %s with ID %s", username, user_id)

    context.bot.send_message(chat_id=update.effective_chat.id, text=config["text"]["start"].format(update.message.from_user.first_name))


def food_recommendation(update, context):
    username = update.message.from_user.username
    user_id = update.message.from_user.id

    context.bot.send_message(chat_id=update.effective_chat.id, text=config["text"]["food_recommendation"].format(update.message.from_user.first_name))

def messages(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=config["text"]["unknown_user_input"].format(update.message.from_user.first_name))

def feedback(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=config["text"]["feedback"].format(update.message.from_user.first_name))

def error(update, context):
    """
    Log any errors that occurred
    """
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    logging.info(config["text"]["bot_started"])

    # Create the Updater and pass it your bot's token.
    pp = PicklePersistence(filename=config["telegram"]["pickle_file"])

    updater = Updater(token=config["telegram"]["token"], persistence=pp, use_context=True)
    bot = updater.bot

    bot.set_my_commands(config["telegram"]["commands"])
    bot.send_message(chat_id=config["admin"]["bot_admin"], text=config["text"]["bot_started"])

    def stop_and_restart():
        """Gracefully stop the Updater and replace the current process with a new one"""
        updater.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)

    def restart(update, context):
        update.message.reply_text('Bot is restarting...')
        Thread(target=stop_and_restart).start()

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('r', restart, filters=Filters.user(user_id=config["admin"]["bot_admin"])))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('eat_what_leh', food_recommendation))
    dp.add_handler(CommandHandler('feedback', feedback))
    dp.add_handler(MessageHandler(Filters.all, messages))
    
    # log all errors
    dp.add_error_handler(error)

    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,SIGTERM or SIGABRT.
    updater.idle()

if __name__ == '__main__':
    main()