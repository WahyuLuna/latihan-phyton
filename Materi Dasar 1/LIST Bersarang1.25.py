
data_0 = [0,1]
data_1 = [2.3]

data_list_biasa = [1,2,3,4]

print(f"list biasa {data_list_biasa}")

list_2d = [data_0,data_1,data_list_biasa]

print(list_2d)

# contoh pengunaan

per_0 = ["wahyu", 18, "laki-laki", "awal"]
per_1 = ["luna", 19, "laki-laki", "tengah"]
per_2 = ["wijaya", 20, "laki-laki", "akhir"]

list_per = [per_0, per_1, per_2]

print (list_per)

for peserta in list_per :
    print (f"nama\t :{peserta[0]}")
    print (f"umur\t :{peserta[1]}")
    print (f"kelamin\t :{peserta[2]}")
    print (f"urutan\t :{peserta[3]}\n")



