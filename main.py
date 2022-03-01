import logging
import db
import os
import time
import admin

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from picamera import PiCamera

# Constant values
BOT_TOKEN = open('SECRET.txt', 'r').readline().rstrip('\n')
LOGIN_PASSWORD=open('LOGIN_PASSWORD.txt', 'r').readline().rstrip('\n')
ADMIN_USERS=open('ADMIN_USERS.txt', 'r').readlines()
ADMIN_USERS=[s.strip() for s in ADMIN_USERS]
PATH = os.getenv("HOME")


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def login_command(update: Update, context: CallbackContext) -> None:
  if (len(update.message.text.split()) != 2):
    update.message.reply_text('Enter password after "/login"')
    return

  if (update.message.text.split()[1] != LOGIN_PASSWORD):
    update.message.reply_text('Invalid password')
    return

  if (db.checkIfIDExists(id)):
    update.message.reply_text('Already logged in')
    return

  update.message.reply_text('Logging in...')
  db.addToDb(id)
  return


def checkIfLoggedIn(update: Update, context: CallbackContext) -> None:
  if (not db.checkIfIDExists(id)):
    # Block user from all commands except /login if not logged int
    update.message.reply_text("Login with /login")
    return

def photo_command(update: Update, context: CallbackContext) -> None:
  print ("Taking picture…");
  # Initialize the camera
  update.message.reply_text("Hang in there, I'm doing my best..")
  camera = PiCamera();
  camera.start_preview()
  camera.rotation = -90
  camera.capture(PATH + '/pic.jpg')
  time.sleep(2)
  camera.stop_preview()
  camera.close()
  # Seding picture
  update.message.reply_photo(open(PATH + '/pic.jpg', 'rb'))

def update_command(update: Update, context: CallbackContext) -> None:
  os.system('sh ./update.sh')

def deletedata_command(update: Update, context: CallbackContext) -> None:
  update.message.reply_text('Removing user...')
  db.deleteFromDB(id)





def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("photo", photo_command), 1)
    dispatcher.add_handler(CommandHandler("photo", photo_command), 2)
    dispatcher.add_handler(CommandHandler("login", login_command), 2)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()