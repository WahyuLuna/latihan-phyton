

import datetime 
hari = datetime.date.today()
print (hari)

# di singkat/sederhanakan

import datetime as dt
hari = dt.date.today()
print (hari)

tanggal = dt.date(2003,12,18)
print (f"""
       
sekarang tanngal : {tanggal}  
dan hari ini adalah hari : {hari:%A}
dan saya lahir pada hari : {tanggal:%A}

       """)

#KALKULATOR TANGGAL :

import datetime as dt
hari = datetime.date.today()
print ("masukan tanngal,bulan, tahun lahir anda")
tanggal = int(input("tanggal :\t"))
bulan = int(input("bulan :\t\t"))
tahun = int(input("tahun :\t\t"))

operate = dt.date(tahun,bulan,tanggal)
umur = hari - operate
umurtahun = umur.days // 365
print ("tanggal lahir anda :", operate)
print (f"dan anda lahir pada hari : {operate:%A}")
print ("dan umur anda sekarang : ", umurtahun, "tahun")
