print("======|SELAMAT DATANG DI ATM BERSAMA|======")

nama = input("Masukan Nama Anda : ")
norek = input("Masukan No. Rekening Anda : ")
jenbank = input("Masukan Jenis Bank Anda : ")
pss = input("Masukan Password Anda : ")



# Menu Utama

tt=1
while tt == 1:
    print("""
    ========(masukan opsi yang anda ingin)=======
    1. Tarik Tunai
    2. Transfer Uang
    3. Transaksi Lain     
    \n""")
    pil = int(input("masukan pil anda : "))



        #Tarik tunai

    if pil == 1:
        x= 10
        while x == 10:
            print("""
        ========(masukan nominal mata uang yang anda ingin)=======
        1. 50.000
        2. 100.000  
        """)
            piljen = int(input("pilih no tipe nominal mata uang : "))
            
            # Mata Uang 50.000
            if piljen == 1:
                print("Masukan Jumlah Uang Yang ingin Anda Tarik")
                print("""
        ========(Masukan Jumlah Uang Yang ingin Anda Tarik)=======
        ! Harus kelipatan Rp. 50.000
        ! Max Penarikan Rp. 2.000.000
        """)
                uang= int(input("Jumlah : "))
                
                a = uang
                a2 = a/50000
                a3 = a2%1
                
                if a > 2000000:
                    x=10
                elif a3==1 or a3==0:
                    x=1
                    print(f"""
    ========(RESI)=======
    nama : {nama}
    No.Rek : {norek}
    Bank : {jenbank}
    Jumlah Penarikan : Rp. {uang:,}     
    \n""")
                    tt = int(input('apakah anda ingin Melakukan Transaksi lain [(Y=1)/(T=0)]: '))
                else:
                    x=10

    
            # Mata Uang 100.000        
            elif piljen == 2:
                print("Masukan Jumlah Uang Yang ingin Anda Tarik")
                print("""
        ========(Masukan Jumlah Uang Yang ingin Anda Tarik)=======
        ! Harus kelipatan Rp. 100.000
        ! Max Penarikan Rp. 2.000.000
        """)
                uang= int(input("Jumlah : "))
                
                a = uang
                a2 = a/100000
                a3 = a2%1
                
                if a > 2000000:
                    x=10
                elif a3==1 or a3==0:
                    x=1
                    print(f"""
    ========(RESI)=======
    nama : {nama}
    No.Rek : {norek}
    Bank : {jenbank}
    Jumlah Penarikan : Rp. {uang:,}     
    \n""")
                    tt = int(input('apakah anda ingin Melakukan Transaksi lain [(Y=1)/(T=0)]: '))
                else:
                    x=10
    
            #tranfer Uang
    
    elif pil == 2:
        x= 12
        while x == 12:
            tujuan= int(input("Masukan No Rekening Tujuan Anda : "))
            jb = input("Masukan Nama Bank Anda : ")
            print("\nMinimal Jumlah Tranfer Rp.50.000 dan Max Rp. 1.000.000.000\n")
            uang = int(input("Masukan Jumlah Uang Yang Ingin Anda Transfer : Rp. "))
            
            if uang > 1000000000  :
                print("jumlah transfer Melebihi Dari Batas maksimal, Silah kan memasukan ulang")
                x =12
            elif uang <50000 :
                print("jumlah transfer Kuran Dari Batas Minimal, Silah kan memasukan ulang")
                x= 12
            else  :
                x= 1
                print(f"""
        ========(RESI)=======
        Pengirim : {nama}
        No. Rek Pengirim : {norek}
        bank : {jenbank}
        No.Rek Tujuan : {tujuan}
        Bank Tujuan: {jb}
        Jumlah Transfer : Rp. {uang:,}     
        \n""")
                tt = int(input('apakah anda ingin Melakukan Transaksi lain [(Y=1)/(T=0)]: '))
            
        #Transaksi Lain
        
    elif pil == 3: 
        x= 12
        while x==12:
            print("""
        ========(Pilih Jenis Transaksi Lain)=======
        1. Isi Saldo (Dana,Gopay,Link Aja)
        2. Bayar Biaya Sekolah 
        
        """)
            jentran = int(input("Pilihan = "))
        
            if jentran == 1:
                x=1
                y = 1
                while y == 1 :
                    print("""
            ========(Pilih Jenis Saldo Anda)=======
            1. Dana
            2. Gopay
            3. Link Aja
            
            """)
                    piljen = int(input("pilihan : "))
                    
                    if piljen == 1:
                        y = 2
                        tujuan= int(input("Masukan No Dana Tujuan Anda : "))
                        print("\nMinimal Jumlah Tranfer Rp.10.000 dan Max Rp. 1.000.000\n")
                        uang = int(input("Masukan Jumlah Uang Yang Ingin Anda Transfer : Rp. "))
                        
                        if uang > 1000000  :
                            print("jumlah transfer Melebihi Dari Batas maksimal, Silah kan memasukan ulang")
                            x =12
                        elif uang <10000 :
                            print("jumlah transfer Kuran Dari Batas Minimal, Silah kan memasukan ulang")
                            x= 12
                        else  :
                            x= 1
                            print(f"""
            ========(RESI)=======
            Pengirim : {nama}
            No. Rek Pengirim : {norek}
            bank : {jenbank}
            No Saldo Tujuan : {tujuan}        
            Jumlah Transfer Isi Saldo : Rp. {uang:,}     
            \n""")
                            tt = int(input('apakah anda ingin Melakukan Transaksi lain [(Y=1)/(T=0)]: '))
                    elif piljen == 2:
                        y = 2
                        tujuan= int(input("Masukan No Gopay Tujuan Anda : "))
                        print("\nMinimal Jumlah Tranfer Rp.10.000 dan Max Rp. 1.000.000\n")
                        uang = int(input("Masukan Jumlah Uang Yang Ingin Anda Transfer : Rp. "))
                        
                        if uang > 1000000  :
                            print("jumlah transfer Melebihi Dari Batas maksimal, Silah kan memasukan ulang")
                            x =12
                        elif uang <10000 :
                            print("jumlah transfer Kuran Dari Batas Minimal, Silah kan memasukan ulang")
                            x= 12
                        else  :
                            x= 1
                            print(f"""
            ========(RESI)=======
            Pengirim : {nama}
            No. Rek Pengirim : {norek}
            bank : {jenbank}
            No Saldo Tujuan : {tujuan}        
            Jumlah Transfer Isi Saldo : Rp. {uang:,}     
            \n""")
                            tt = int(input('apakah anda ingin Melakukan Transaksi lain [(Y=1)/(T=0)]: '))
                    elif piljen == 3:
                        y = 2
                        tujuan= int(input("Masukan No Link Aja Tujuan Anda : "))
                        print("\nMinimal Jumlah Tranfer Rp.10.000 dan Max Rp. 1.000.000\n")
                        uang = int(input("Masukan Jumlah Uang Yang Ingin Anda Transfer : Rp. "))
                        
                        if uang > 1000000  :
                            print("jumlah transfer Melebihi Dari Batas maksimal, Silah kan memasukan ulang")
                            x =12
                        elif uang <10000 :
                            print("jumlah transfer Kuran Dari Batas Minimal, Silah kan memasukan ulang")
                            x= 12
                        else  :
                            x= 1
                            print(f"""
            ========(RESI)=======
            Pengirim : {nama}
            No. Rek Pengirim : {norek}
            bank : {jenbank}
            No Saldo Tujuan : {tujuan}        
            Jumlah Transfer Isi Saldo : Rp. {uang:,}     
            \n""")
                            tt = int(input('apakah anda ingin Melakukan Transaksi lain [(Y=1)/(T=0)]: '))
                    else :
                        y = 1
                        print ("Anda Salah menginput Pilihan")
            
            elif jentran == 2 :
                x=1
                bayar = []                
                print("=====(Masuka Kode Pembayaran Sekolah Anda)======")
                bayar = input("Kode Pembayaran : ")
                pan = len(bayar)
                
                if pan < 3:
                    total = 2000000
                elif pan < 6:
                    total = 3500000
                elif pan > 5 :
                    total = 4500000
                
                
                print(f"""
            ========(RESI)=======
            Pengirim : {nama}
            No. Rek Pengirim : {norek}
            bank : {jenbank}
            No kode Pembayaran : {bayar}        
            Jumlah Pembayaran : Rp. {total:,}     
            \n""")
                tt = int(input('apakah anda ingin Melakukan Transaksi lain [(Y=1)/(T=0)]: '))
            
            else:
                x=12
                print ("Anda Salah menginput Pilihan")