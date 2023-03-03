#crea database mysql

import mysql.connector  #importando la libreria

mydb = mysql.connector.connect(      # mydb serve ad interagirecol db 
  host="localhost",              #indirizzo dove sta il db
  user="root",
  password=""
)

mycursor = mydb.cursor()  #funzione che serve per i comandi a mysql in linguaggio sql

mycursor.execute("CREATE DATABASE mydatabase")

