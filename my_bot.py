from telegram.ext import Updater, CommandHandler
import os

# Define the start command callback
def start(update, context):
    update.message.reply_text('Hello! Welcome to my bot.')

def main():
    # Get your bot token from environment variables or replace it with your actual token
    TOKEN = '7500313919:AAFLrinWH5a8_XshkrYzpM5Z9WRGURKDczM'

    # Create an Updater object with the bot token
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add a command handler for the /start command
    dp.add_handler(CommandHandler("start", start))

    # Start the bot
    updater.start_polling()

    # Keep the bot running until interrupted
    updater.idle()

if __name__ == '__main__':
    main()
