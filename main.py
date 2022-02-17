# -*- encoding: utf-8 -*-
import telepot
import db
import time
import os

from picamera import PiCamera

path=os.getenv("HOME")
BOT_ID=open('SECRET.txt', 'r').readline().rstrip('\n')

# Handling message from Telegram
def handleMessage(msg):
  id = msg['chat']['id'];
  command = msg['text'];
  print ('Command ' + command + ' from chat id' + str(id));
  if (command == '/photo'):
    print ("Taking picture…");
    # Initialize the camera
    camera = PiCamera();
    camera.start_preview()
    camera.rotation = -90
    camera.capture(path + '/pic.jpg')
    time.sleep(2)
    camera.stop_preview()
    camera.close()
    # Seding picture
    bot.sendPhoto(id, open(path + '/pic.jpg', 'rb'))
    bot.sendMessage(id, "WOOO :OO")
  elif (command == '/video'):
    print("Taking video...");
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.rotation = -90
    camera.start_recording(path + '/spinni_video.h264')
    camera.wait_recording(60)
    camera.stop_recording()
    camera.close()
    # Send video
    bot.sendVideo(id, open(path + '/spinni_video.h264', 'rb'))
    bot.sendMessage(id, 'YOOOO')
  elif (command == '/update'):
    os.system('sh ./update.sh')
  elif (command == '/db'):
    bot.sendMessage('Reading database...')
    bot.sendMessage(db.getDbContent())

  else:
    bot.sendMessage(id, "Laita /photo perkele")
  



bot = telepot.Bot(BOT_ID);
bot.message_loop(handleMessage);
print ("Listening to bot messages….");
while 1:
    time.sleep(10);