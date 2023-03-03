# come creare una tabella

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase2"
)

mycursor = mydb.cursor()  
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")