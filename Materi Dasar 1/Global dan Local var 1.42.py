# variable Global
# dapat di gunakan oleh semua fungtion atau metode di dalam suatu codingan

Nama_global = 'wahyu'

def tampil():
    print(f" Nama Global adalah {Nama_global}")

tampil()

for i in range(0,5):
    print(f" angka = {i} nama = {Nama_global}")
    


# variable Local
# hanya dapat diakses dalam suatu area/Class tertentu
# hanya dapat di ubah di dalam fungtion local

def lokal():
    nama_local = "Luna"
    print (f"nama local {nama_local}")

# merubah variable global menjadi local

angka=0
def ubah(nilai):
    global angka #fungsi ini mendapat akses mengubah variable global
    angka = nilai
    
print(f"Sebelum = {angka}")
ubah(5)
print(f"Sesudah = {angka}")