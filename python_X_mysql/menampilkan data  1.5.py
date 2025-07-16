import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "latihanpy"
  
)

cursor = db.cursor()
show_data = "SELECT * FROM data_diri"


print ("\n =======(tampil semua data)=======\n")
cursor.execute(show_data) #perintah menampilkan data
results = cursor.fetchall()
for i in results:
    print(i)

print ("\n =======(tampil satu data)=======\n")
cursor.execute(show_data)#perintah menampilkan data dari awal
results2 = cursor.fetchone()# apabila sdh menampilkan data 1
print(results2)

print ("\n =======(tampil sisa data)=======\n")
while results2 is not None: #maka data kedua dan selanjutnya akan di tampilkan disini
    print(results2)
    results2 = cursor.fetchone()

 



