import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "latihanpy"
  
)

cursor = db.cursor()
show_data = "SELECT `jurusan` FROM `data_diri` WHERE `nama`='wahyu';"


print ("\n =======(tampil semua data)=======\n")
cursor.execute(show_data) #perintah menampilkan data
results = cursor.fetchall()
print ( results)
data = results[0]
print(data)
akhir = data[0]
print(akhir)
