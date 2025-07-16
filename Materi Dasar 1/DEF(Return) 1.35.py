
#return akan berfungsi sebagai pendefinisian/pengembalian semua nilai yang terjadi pada fungtion menuju variable yang telah di tentukan

"""Menggunakan return"""
def kuadrat(x):
    hasil = x**2 #bisa langsung dipanggil karna sedah ada perintah Return
    tambah = x+2 #hanya bisa dipanggil dengan perintah print
    print("\n", tambah)
    return hasil # hasil kodingan fungtion akan di kembalikan/di patokan pada variable "hasil"

y = kuadrat(4) #dapat memanggil hasil tanpa perintah Print
kuadrat(4)# hanya bisa memanggil data yang ada perintah print
print(y)

"""Tanpa menggunakan return"""
def kuadrat2(x):
    hasil = x**2 #tidak muncul pada hasil karena tidak di devenisikan di Return
    kurang = x+2 #hanya bisa dipanggil dengan perintah print
    print("\n", kurang)
    return 0 # hasil kodingan fungtion akan bernilai 0 karena di definisikan 0

z = kuadrat2(4) #dapat memanggil hasil tanpa perintah Print
kuadrat2(4)# hanya bisa memanggil data yang ada perintah print
print(z)

"""Menggunakan return dengan banyak variable"""
def matematika(angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2
    return tambah,kurang,kali,bagi # saat mengambil return maka akan dibagi sesuai urutan

t,k,m,n = matematika(5,2) # data pada return akan di berikan sesuai urutan

print(f" hasil tambah = {t}")
print(f" hasil kurang = {k}")
print(f" hasil kali = {m}")
print(f" hasil bagi = {n}")





