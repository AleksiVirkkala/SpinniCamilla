# -*- encoding: utf-8 -*-
import telepot
import db
import time
import os

from picamera import PiCamera

path=os.getenv("HOME")
BOT_ID=open('SECRET.txt', 'r').readline().rstrip('\n')
LOGIN_PASSWORD=open('LOGIN_PASSWORD.txt', 'r').readline().rstrip('\n')

# Handling message from Telegram
def handleMessage(msg):
  id = msg['chat']['id'];
  command = msg['text'];
  print ('Command ' + command + ' from chat id' + str(id));

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

  # elif (command == '/video'):
  #  print("Taking video...");
  #  camera = PiCamera()
  #  camera.resolution = (640, 480)
  #  camera.rotation = -90
  #  camera.start_recording(path + '/spinni_video.h264')
  #  camera.wait_recording(60)
  #  camera.stop_recording()
  #  camera.close()
  #  # Send video
  #  bot.sendVideo(id, open(path + '/spinni_video.h264', 'rb'))
  #  bot.sendMessage(id, 'YOOOO')
  elif (command == '/update'):
    os.system('sh ./update.sh')
  elif (command == '/deletedata'):
    bot.sendMessage(id, 'Removing user...')
    db.deleteFromDB(id)
  elif (command == '/db'):
    bot.sendMessage(id, 'Reading database...')
    bot.sendMessage(id, db.getDbContent())
  else:
    bot.sendMessage(id, "Laita /photo perkele")




bot = telepot.Bot(BOT_ID);
bot.message_loop(handleMessage);
print ("Listening to bot messages….");
while 1:
    time.sleep(10);