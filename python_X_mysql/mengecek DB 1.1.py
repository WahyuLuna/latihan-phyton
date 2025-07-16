import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "latihanpy" # anda dapat mengecek nama data bases anda di sini dengan memasukan nama data base
  
)

if db.is_connected():
  print("berhasil")
