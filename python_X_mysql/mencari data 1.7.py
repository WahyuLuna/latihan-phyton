import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "latihanpy"
  
)


data = str(input("masukan nama : "))
cursor = db.cursor()
show_data = f"SELECT * FROM `data_diri` WHERE nama = '{data}'"


print ("\n =======(tampil semua data)=======\n")
cursor.execute(show_data) #perintah menampilkan data
results = cursor.fetchall()
for i in results:
    print(i)

 



