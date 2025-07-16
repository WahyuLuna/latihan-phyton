import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "latihanpy"
  
)

cursor = db.cursor()
nama = str(input("masukan nama yang ingin di hapus : "))

delete = (f"DELETE FROM data_diri where nama = '{nama}'") 
cursor.execute(delete)
db.commit()
print('berhasil menghapus')