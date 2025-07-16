
nama = str(input("nama "))
jumlah = int(input("jumlah :"))
relasi = []
for i in range(jumlah):
    kotarelasi = str(input("kotarelasi :"))
    jarak = int(input("jarak :"))
    nk = f"{nama}-{kotarelasi}"
    relasi.append((nk,jarak))
    
kota = (nama,relasi,jumlah)
print(kota)
dekat = []

for i in range(jumlah):
    wow = relasi[i-1]
    relasi[i-1]=dekat.append(wow[1]) 
    
print(min(dekat))





