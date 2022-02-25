def handleMessage(id, command, bot, db):
  if (command == '/db'):
    bot.sendMessage(id, 'Reading database...')
    bot.sendMessage(id, db.getDbContent())