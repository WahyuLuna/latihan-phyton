
# metode normal

def kuadrat(angka):
    return angka**2
print(f"hasil fungsi kuadrat {kuadrat(3)}")

# metode Lamda
# lamda dapat menggantikan fungtion
# mempersingkat codingan

kuadratlamda = lambda angka:angka**2
print (f"hasil dari kuadrat lambda {kuadratlamda(3)}")

pangkat = lambda num,pow : num**pow
print (f"hasil dari kuadrat lambda dua input {pangkat(3,2)}")

# kasus 2 (sorting LIST dengan lambda)

data = ["asep","gilang","donoh","zak"]
def sortir(data):
    return len(data)
data.sort(key=sortir)
print(f"sortir dengan fungtion = {data}")

#menggunakan lambda
data = ["asep","gilang","donoh","zak"]
data.sort(key=lambda nama:len(nama))
print(f"sortir dengan lambda = {data}")

# Kasus 3 ( Filter LIST dengan lambda)

data=[1,2,3,4,5,6,7,8,9,10]
def Kurang_dari_enam(angka):
    return angka<6

data_angka_filter = list(filter(Kurang_dari_enam,data))
print(f"dengan fungtion = {data_angka_filter}")

# Metode lambda

data=[1,2,3,4,5,6,7,8,9,10]
data_angka_filter = list(filter(lambda x:x<6,data))
print(f"dengan menggunakan lambda {data_angka_filter}")

# lambda angka genap
data=[1,2,3,4,5,6,7,8,9,10]
data_genap = list(filter(lambda x:(x%2==0),data))
print(f"mencari genap dengan menggunakan lambda {data_genap}")

data=[1,2,3,4,5,6,7,8,9,10]
ganjil = list(filter(lambda x:(x%2==1),data))
print(f"mencari ganjil dengan menggunakan lambda {ganjil}")


#====================={ ANONYMOOUS FUNGTION}

#normal

def pangkat(angka,n):
    hasil = angka**2
    return hasil
data_hasil = pangkat(5,2)
print(f"fungsi biasa {data_hasil}")

# dengan Anonymouse fungtion

def pangkat2(n):
    return lambda angka:angka**n

pangkat=pangkat2(2)
print(f"dengan anonymous lambda {pangkat(5)}")



