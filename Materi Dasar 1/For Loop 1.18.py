

angka1 =  [1,2,3,4,5]
for i in angka1 :
    print (f"hasil {i}")


# dengan menggunakan range

angka2 =  range (5)
for i in angka2 :
    print (f"hasil {i}")

angka3 = range (1,5)
for i in angka3 :
    print(f"sekarang {i}")

nama = "wahyu luna wijaya"
for huruf in nama :
    print(huruf )


# membuat piramida

sisi = int(input("masukan tinggi piramida : "))

#menggunakan FOR

count = 1
for i in range (sisi):
    print("*" * count)
    count += 1


#menggunakan WHILE
count = 1
while True :
    print("*" * count)
    count += 1
    
    if count > sisi:
        break


count = 1
while True :
    if count % 2: #print bila ganjil
        print("*" * count)
        count += 1
        
    else : #akan kembali keatas bnila ganjil
        count += 1
        continue
    
    if count > sisi: #akan break bila mencapai hasil
        break

print("selesai \n")

#piramida sama kaki

count = 1
spasi = int(sisi/2)
while True :
    if count % 2: #print bila ganjil
        print(" " * spasi, "+" * count)
        spasi -= 1
        count += 1
        
    else : #akan kembali keatas bnila ganjil
        count += 1
        continue
    
    if count > sisi: #akan break bila mencapai hasil
        break

print("selesai \n")


















