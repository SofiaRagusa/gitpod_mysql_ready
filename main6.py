   #per gli oggetti nella tabella bisogna creare una colonna con id unico per oggetto; chiave primaria

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase2"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers2 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))") #usiamo comando in maiuscolo per dare un numero unico per ogni oggetto 