


print ("==================|JASA RENTAL MOBIL|==================\n")
akhir = 1
while akhir == 1 :
    nama = input("masukan nama anda : ")
    print ("""
==================|PILIH JENIS MOBIL|==================
    1. AD (AVANZA DELUXE)
    2. AV (AVANZA VELOX)
    3. XS (XENIA SPORTY)
    4. RZ (TOYOTA RUSH)
    5. TR (TERRIOS)
    6. IV (INNOVA)
    7. FR (FORTUNER)          
       """)
    no = int(input("masukan no type mobil anda : "))
    bulan = int(input("masukan lama sewa (bulan) : "))
    
    if no == 1 :
        kode = "AD"
        jenis = "AVANZA DELUXE"
        harga = bulan*250000
    elif no == 2:
        kode = "AV"
        jenis = "AVANZA VELOX"
        harga = bulan*250000   
    elif no == 3:
        kode = "XS"
        jenis = "XENIA SPORTY"
        harga = bulan*150000
    elif no == 4:
        kode = "RZ"
        jenis = "TOYOTA RUSH"
        harga = bulan*100000
    elif no == 5:
        kode = "TR"
        jenis = "TERRIOS"
        harga = bulan*150000
    elif no == 6:
        kode = "IV"
        jenis = "INNOVA"
        harga = bulan*200000
    elif no == 7:
        kode = "FR"
        jenis = "FORTUNER"
        harga = bulan*300000
    else :
        print ("ERROR INPUT")    
        
    print(f"""
==================|NOTA PEMBAYARAN|==================      
    nama : {nama}      
    kode kendaran yang di sewa : {kode}
    jenis kendaran yang di sewa : {jenis} 
    lama kendaraan di sewa : {bulan}      
    total harga sewa adalah :Rp. {harga:,}      
          """)
    akhir = int(input("masih ingin melakukan transaksi (1/0): "))
    
    
    
print ("\n==================|TERIMAKASIH|==================")
        
    
    
  