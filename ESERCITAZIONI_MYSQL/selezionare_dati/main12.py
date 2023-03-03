# per selezionare solo una riga usa fetchone() che restituisce la prima riga

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase2"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)