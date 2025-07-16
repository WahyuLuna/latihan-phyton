

#1. menyambung string(concatenate)

nama_pertama = "wahyu"
nama_tengah = "Luna"
nama_akhir = "wijaya"

nama_lengkap = nama_pertama + " " +nama_tengah + " " + nama_akhir
print (nama_lengkap)

#2. menghitung pancang string

panjang = len(nama_lengkap) 
print ("jumlah huruf dan angka dan simbil di di dalam ",nama_lengkap,"adalah", panjang)


#3. operator untuk string
    #a. mengecek apakah ada komponen char di dalam string
    
d= "a"
status = d in nama_lengkap
print ("string", d," ada didalam ", nama_lengkap,"? =", str(status))

d= "k"
status = d in nama_lengkap
print ("string", d," ada didalam ", nama_lengkap,"? =", str(status))

    #b. mengulang string
    
print ("\nLuna "*5)
    
    #c. indexing

print ("index ke 0 : ", nama_lengkap[0])
print ("index ke 1 : ", nama_lengkap[1])
print ("index ke 2 : ", nama_lengkap[2])
print ("index ke 3 : ", nama_lengkap[3])
print ("index ke 4 : ", nama_lengkap[4])

print ("\nindex ke 6-10 : ", nama_lengkap[6:10])
print ("\nindex ke 0.2.4.6.8.10 : ", nama_lengkap[0:10:2])

    #d. huruh paling besar

print("paling besar :", max(nama_lengkap))
print("paling kecil :", min(nama_lengkap))

    #4. ASCII CODE
data = ord("W")
print("ASCII CODE untuk W adalah :", str(data))

data = 87
print("ASCII CODE 87 adalah :", chr(data))

    #5. operator dalam bentuk method 
    
data = "saya sedang coding"
jumlah = data.count("a")
print ("jumlah a pada kata ", data, "adalah :", jumlah) 











