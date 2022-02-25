# -*- encoding: utf-8 -*-
import telepot
import db
import time
import os
import admin

from picamera import PiCamera

path=os.getenv("HOME")
BOT_ID=open('SECRET.txt', 'r').readline().rstrip('\n')
LOGIN_PASSWORD=open('LOGIN_PASSWORD.txt', 'r').readline().rstrip('\n')

ADMIN_USERS=open('ADMIN_USERS.txt', 'r').readlines()
ADMIN_USERS=[s.strip() for s in ADMIN_USERS]


# Handling message from Telegram
def handleMessage(msg):
  try:
    id = msg['chat']['id'];
    command = msg['text'];
    print ('Command ' + command + ' from chat id ' + str(id));

    if (command.split()[0] == '/login'):
      if (len(command.split()) != 2):
        bot.sendMessage(id, 'Enter password after "/login"')
        return
      
      if (command.split()[1] != LOGIN_PASSWORD):
        bot.sendMessage(id, 'Invalid password')
        return

      if (db.checkIfIDExists(id)):
        bot.sendMessage(id, 'Already logged in')
        return

      bot.sendMessage(id, 'Logging in...')
      db.addToDb(id)
      return

    if (not db.checkIfIDExists(id)):
      # Block user from all commands except /login if not logged int
      bot.sendMessage(id, "Login with /login")
      return
      
    elif (command == '/photo'):
      print ("Taking picture…");
      # Initialize the camera
      bot.sendMessage(id, "Hang in there, I'm doing my best..")
      camera = PiCamera();
      camera.start_preview()
      camera.rotation = -90
      camera.capture(path + '/pic.jpg')
      time.sleep(2)
      camera.stop_preview()
      camera.close()
      # Seding picture
      bot.sendPhoto(id, open(path + '/pic.jpg', 'rb'))

    elif (command == '/update'):
      os.system('sh ./update.sh')
    elif (command == '/deletedata'):
      bot.sendMessage(id, 'Removing user...')
      db.deleteFromDB(id)
  
    elif (str(id) in ADMIN_USERS):
      admin.handleMessage(id, command, bot, db)

    else:
      bot.sendMessage(id, "Laita /photo perkele")
  except:
    print("virhe :(")





bot = telepot.Bot(BOT_ID);
bot.message_loop(handleMessage);
print ("Listening to bot messages….");
while 1:
    time.sleep(10);