
"""
w = write mode / mode menulis dan menghapus file lama , jika file ada ada maka akan dibuat file baru
r = read mode / hanya bisa membaca
a = appending mode / menambahkan data di akhir baris
r+ = write and read mode
.write() = untuk menginput text
.read() = untuk membaca text di file 
.readline() = unutk membaca pada garis yang telah di tentukan
.close() = untuk mengakhiri program agar tidak terus berjalan     
"""

# membuat dan mengisi file text

file = open("data.txt",'w')

file.write ('ini adalah date text yang di buat program python')
file.write ('\nini adalah baris ke dua')
file.write ('\nini adalah baris ke tiga')
file.write ('\nini adalah baris ke empat')
file.close()

# membaca file text
# apabila perintah pertama telah mebaca maka perintah berukutnya tidak dapat membaca text jika tidak di close
file2 = open("data.txt",'r')
print(file2.read()) # 
print(file2.read(15)) # hanya akan membaca 15 huruf
file2.close()


file2 = open("data.txt",'r')
print(file2.readline())
print(file2.readline())
file2.close()

# append file text
file3 = open("data.txt", 'a')
file3.write("dara ini di buat oleh data Append")
file3.close()

file3 = open("data.txt",'r')
print(file3.read()) 
