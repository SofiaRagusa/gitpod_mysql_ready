# per selezionare i dati registrati nella tabella usa select nel cursore 

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase2"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()      #fetchall seleziona tutte le ultime righe registrate

for x in myresult:
  print(x)
