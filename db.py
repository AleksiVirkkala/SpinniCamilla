import sqlite3
# cur.execute("CREATE TABLE chats (id int PRIMARY KEY)")

def getDbContent():
  conn = sqlite3.connect('/home/pi/camillatesti/camilla')
  cur = conn.cursor()
  cur.execute("SELECT id FROM chats;")
  rows = cur.fetchall()
  cur.close()
  return rows

def checkIfIDExists(chatID):
  conn = sqlite3.connect('/home/pi/camillatesti/camilla')
  cur = conn.cursor()
  cur.execute("SELECT id FROM chats where id = " + str(chatID) + ";")
  rows = cur.fetchall()
  cur.close()
  return len(rows) == 1

def addToDb(chatID):
  conn = sqlite3.connect('/home/pi/camillatesti/camilla')
  cur = conn.cursor()
  cur.execute("INSERT INTO chats (id) VALUES (" + str(chatID) + ");")
  conn.commit()
  cur.close()
  return