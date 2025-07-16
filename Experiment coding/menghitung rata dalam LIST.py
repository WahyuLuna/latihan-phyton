
angka = []
jumlah = str(input("masukan angka yg ingin di jumlah : "))

while jumlah != "" :
    x = eval(jumlah)
    angka.append(x)
    jumlah = str(input("masukan angka yg igin di jumlah : "))
    
total = len(angka)
data = sum(angka)
rata = data/total
print("angka : ", angka)
print ("jumlah : ",data)
print("Rata - Rata : ", rata)

# bonus soal 

angka = []
n = 20
x= 0
while n > x:
    angka.append(n)
    print (n)
    n -= 1
print("hasil total = ", sum(angka))