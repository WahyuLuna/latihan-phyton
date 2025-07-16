
angka = [1,3,6,2,4,4,7,8,5,4,6,3,6,3,9,1,4,7,8,5,2,2,5,4,7,8]
print (f"data angka = {angka}")

#count data

jumlah_4 = angka.count(4)
jumlah_3 = angka.count(3)


print (f"jumlah angka 4 = {jumlah_4}")
print (f"jumlah angka 3 = {jumlah_3}")


# ambil posisi data

#         0         1        3
data = ["wahyu", "luna", "wijaya"]
print (f"data {data}")

index_data = data.index("luna")
print (f"index si luna = {index_data}")

#mengurutkan list data

angka.sort()
data.sort()
print(f"angka sort = {angka}")
print(f"data sort = {data}")
# urutkan balik
angka.reverse ()
print(f"angka reverse = {angka}")
print(f"data sort = {data}")


