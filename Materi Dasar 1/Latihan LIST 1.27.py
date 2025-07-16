
list_buku = []

while True :
    judul = input("masukan judul buku : ")
    penulis = input("masukan nama penulis : ")

    data_buku = [judul,penulis]
    list_buku.append(data_buku)
    print (data_buku)
    
    print("no   judul   penulis")
    for index,buku in enumerate(list_buku):
        print(f"{index}\t{buku[0]}\t{buku[1]}")
        
    akhir = str(input("\napakah ingin lanjut (y/n) : "))
    
    if akhir == "n" or "N":
        break

    
    
print ("terimakasih")




