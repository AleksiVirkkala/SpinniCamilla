import sqlite3

def getDbContent():
  conn = sqlite3.connect('/home/pi/camillatesti/camilla')
  cur = conn.cursor()
  cur.execute("SELECT * FROM camilladb")
  rows = cur.fetchall()
  return rows