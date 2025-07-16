
dataharga = []
datanama = []
datahash = []
datagabungan = []

x=1
while x == 1:
    print("""
    ========(masukan opsi yang anda ingin)=======
    1. Input data
    2. Data Base
    3. Scan    
    \n""")
    pil = int(input("masukan pil anda : "))
    
    if pil == 1:
        x=1
        jumlah = int(input('masukan jumlah barang yang mau di input : '))
        for i in range(jumlah):
            nama = input('\nmasukan nama barang : ')
            harga = int(input('masukan harga barang : '))
            nama = nama.upper()
            datanama.append(nama)
            dataharga.append(harga)
            datah = hash(nama)
            datahash.append(datah)
            datagabungan.append([nama,harga,datah])
            
    elif pil == 2:
        x=1
        print(f"""\n=========(Data Base)========
===(Data Nama Barang)===
{datanama}

===(Data Harga Barang)===
{dataharga}

===(Data code Hash Barang)===
{datahash}

===(Data Gabungan Barang)===
{datagabungan}
""")
            
    elif pil == 3:
        x=1

        print("===(masukan Code barang)===")
        scan = int(input("masukan : "))
        ind = datahash.index(scan)
        print ("\n====(Hasil)====")
        print(f"nama barang adalah = {datanama[ind]}")
        print(f"harga barang adalah = {dataharga[ind]}")
        
    else :
        x=0
            
             
            
        
    