import sqlite3

def getDbContent():
  conn = sqlite3.connect('/home/pi/camillatesti/camilla')
  cur = conn.cursor()
  cur.execute("SELECT * FROM camilladb")
  rows = cur.fetchall()
  return rows

def addToDb(chatID):
  conn = sqlite3.connect('/home/pi/camillatesti/camilla')
  cur = conn.cursor()
  print(str(chatID))
  return cur.execute("INSERT INTO camilladb VALUES ('" + str(chatID) + "');")