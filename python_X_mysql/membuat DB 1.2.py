import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = ""  
)

Nama_DB = input(str("Masukan Nama data base : "))

cursor = db.cursor()
cursor.execute(f"CREATE DATABASE {Nama_DB}")#data bases yg sdh jadi (latihanpy)

print ("data base berhasil dibuat ")
