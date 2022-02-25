def handleMessage(id, command, bot, db):
  # Get list of user ids that are currently logged in
  if (command == '/db'):
    bot.sendMessage(id, 'Reading database...')
    bot.sendMessage(id, db.getDbContent())
  
  # Get log file content
  if (command == '/log'):
    bot.sendMessage(id, 'Reading log file...')
    log = open('log.txt', 'r').readlines()
    log = "".join(log)
    bot.sendMessage(id, log)