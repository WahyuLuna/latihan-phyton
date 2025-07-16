
barang = ["kursi", "meja","pintu","jendela","kipas", "kipas"]
print(barang)
barang.append("tv") # menambahkan data
print (barang)
barang.extend("lemari") #menambah kata per huruf
print (barang)
barang.insert(2,"karpet") # memasukan data ke posisi yang telah di tentukan
print (barang)
jumlah = barang.count("kipas") # menghitung jumlah data yang di tentukan
print (jumlah)
barang.remove("kipas") #menghapus data yang di tentukan
print (barang)
barang.reverse() # membakilan posisi data
print(barang)
barang.reverse()

benda = barang # kedua list akan memiliki data yang sama
benda.append("rumah")
print (benda)
benda = barang.copy() # kedua list akan memiliki data yang berbeda
benda.append("halaman")
print (benda)

data = "cocholate"
for i in data:
    print(i)







