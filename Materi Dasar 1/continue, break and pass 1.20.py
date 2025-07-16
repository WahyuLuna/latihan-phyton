
#PASS beguna sebagai dummy(tidak akan di eksekusi)

angka = 0

while angka < 5:
    angka += 1
    if angka == 3:
        pass #tidak akan di eksekusi
        
    print(angka)


#CONTINUE berfunsi untuk melompati ke loop selanjutnya
angka = 0
print(f"angka sekarang {angka}")

while angka <5:
    angka += 1
    print (f"angka sekarang {angka}") #aksi 1
    
    if angka == 3:
        print("nice")
        continue    # akan membuat loop meloncat ke loop selanjutnya
                    #sehingga wahtsup ke 3 hilang
    print ("whatsup") #aksi 2

print ("finish\n")

#  BREAK (langsung menyelesaikan perulangan )

data = int(input("hitung sampai :"))

angka = 0
print(f"angka sekarang {angka}")

while True:
    angka += 1
    print (f"angka sekarang {angka}") #aksi 1
    
    if angka == data:
        print("nice")
        break    # langsung ke finish
    
    print ("whatsup") #aksi 2

print ("finish")




















