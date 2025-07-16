import mysql.connector


db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "latihanpy"  
)
# kita tidak dapat membuat nama table dengan nama yang sama
# nama table yang tersedia (data_diri)
cursor = db.cursor()
cursor.execute(f"""
               CREATE TABLE data_diri (
               id INT PRIMARY KEY,
               nama VARCHAR (50) NOT NULL,
               alamat VARCHAR (50) NOT NULL,
               jurusan VARCHAR (50) NOT NULL)        
               """)

print ("table berhasil dibuat")


