import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "db_barang"
)

cursor = db.cursor()
jumlah = int(input("masukan berapa data yang ingin di input : "))

for i in range (jumlah):
  nama = str(input("Masukan Nama : "))
  alamat = str(input("Masukan alamat anda : "))
  jurusan = str(input("masukan Jurusan anda : "))
  # gunakan perintah seperti menggunakan MYSQL pada umunya (membuat,mengubah,menambah,menghapus, dll)
  query = (f"INSERT INTO barang (nama, harga, jenis, hash) VALUES ('{nama}', '{alamat}', '{jurusan}')") #perhatikan dengan akurat symbol ""/''/,/()
  cursor.execute(query)# unutk menjalankana program

db.commit()
print("data berhasil di input")