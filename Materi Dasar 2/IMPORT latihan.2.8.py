# data import = matematika.py

import matematika as m
from matematika import tambah,kurang,bagi,kali #dapat memanggil banyak fungtion dengan menullis nama fungtion
# atau (from matematika import *) akan memanggil semua fungtion didalam class matematika

print(__name__)# akan menghasilkan nama file yang terkait
pil = int(input("""masukan jenis perhitungan anda
            1. tambah
            2. kurang
            3. bagi
            4. kali
            pil : """))

if pil == 1:
    tambah()
elif pil == 2:
    kurang()
elif pil == 3:
    bagi()
elif pil == 4:
    kali()
