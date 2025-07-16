#package adalah kumpulan dari beberapa modul (kumpulan file)
#import file package_data dan package_data2
# gunalkan from untuk memanggil file dari folder cth(from folder1,folder2 import data)


from packagefolder import package_data2 as d2
from packagefolder import package_data as d1

kecepatan = d1.kecepatan(200, 50)
tambah = d2.tambah(15,12)

print(kecepatan)
print(tambah)

from packagefolder import kurang

hasil = kurang(5,10)
print(hasil)

import math
print(math.cos(90))