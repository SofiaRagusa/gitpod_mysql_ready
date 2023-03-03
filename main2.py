#verificare la presenza dei databases elencando tutti i dati

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
)

mycursor = mydb.cursor()
mycursor.execute( "SHOW DATABASES")

for x in mycursor:
  print (x)


