

#index   0(-3)  1(-2)   2(-1)
data = ["wahyu", "luna", "wijaya"]

#mengambil data dari list
data_0 = data[0]
print (f"data pertama index 0 = {data_0}")

data_terakhir = data[-1]
print (f"data terakhir index -1 = {data_terakhir}")

data_awal = data[-3]
print (f"data awal index -1 = {data_awal}")

#mengsmbil info jumlah dalam list

panjang_data = len(data)
print (f"panjang data = {panjang_data}")

#manipulasi data list

# 1.    menambahkan item pada list sesuai posisi

print (f"data sebelum ditambahkan {data}")

data.insert(0,"lutrax")
print(f"data sesudah di tambah = {data}")

# 2.    menambahkan item pada akhir list 
data.append("lopox")
print (f"data di tambah lagi = {data}")

# 3.    menambahkan  list dengan list

data_baru = ["la","li","lu"]
data.extend(data_baru)
print (f"data di gabung lagi = {data}")

#mengubah data 
data = ["wahyu", "luna", "wijaya"]

data[2] = "w"
print (f"data di ganti lagi = {data}")

#menghapus data

data.remove("luna")
print (f"data di hapus = {data}")

#menghapus data paling terakhir

data = data.pop()
print(f"data akhir = {data}")




