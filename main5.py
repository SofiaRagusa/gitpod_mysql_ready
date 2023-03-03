# controlla che la tabella del tuo database esista

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase2"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:              #eseguendo un print per ogni elemento nel db 
  print(x)