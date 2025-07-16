
#===mengunakan========================== for loop

print("for loop")
kumpulan_angka = [1,2,3,4,5,6,7,8,9]

for angka in kumpulan_angka:
    print(angka)

peserta = ["wahyu", "luna", "wijaya"]

for nama in peserta :
    print(nama)


#===mengunakan========================== for loop dan range

print("\nfor loop dan range")
kumpulan_angka = [1,2,3,4,5,6,7,8,9]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")
    

#===mengunakan========================== while

print("\n while loop")
kumpulan_angka = [1,2,3,4,5,6,7,8,9]
panjang = len(kumpulan_angka)
i=0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1
    
#===mengunakan========================== LIST chomperesion

print("\n LIST chomperesion")
data = ["wahyu", 1,2,3,"luna"]

[print(f"data = {i}")for i in data]

#===mengunakan========================== enumerate (INDEX)

print("\n enumerate")
data = ["wahyu", 1,2,3,"luna"]

for index,data in enumerate(data):
    print(f"index = {index}, data = {data}")

#===mengunakan========================== Kuadrat LIST

print("\n Kuadrat LIST")
angka = [1,2,3,4,5,6,7,8,9]
angka_kuadrat = [i**2 for i in angka]
print (angka_kuadrat)


#===mengunakan========================== for loop costum 

print("\n for loop costum")
mobil = ["avanza","xenia","toyota rush","fortuner", "pajero sport","kijang"]
no = 1
for i in mobil:
    print("no ",no," jenis : ",i)
    no += 1


#===mengunakan========================== zip 

print("\n ZIP")
nama = ["wahyu","luna","wijaya","asep","risky"]
jurusan = ["IT",'tataboga','dokter',"pelayaran","arsitek"]

for pelajar,keahlian in zip(nama,jurusan):
    print(f'nama : {pelajar}, dengan jurusan : {keahlian}')
    
    
#===mengunakan========================== set 

print("\n SET")
mobil = ["avanza","xenia","toyota rush","fortuner", "pajero sport","kijang"]
for jenis in sorted(mobil):
    print(jenis)
    
#===mengunakan========================== Reverse 

print("\n Reverse")
for i in reversed(range(1,20,1)):
    print(i)