
#codice per creare un DB my sql

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute( "CREATE DATABASE mydatabase2")

