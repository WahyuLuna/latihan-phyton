#mengambil file dalam package
# file bernama __init__.py akan langsung di jalankan apa bila package di panggil
import package # memanggil folder package (yang berisi matematika dan matematika2)

tambah = package.matematika.tambah(1,2,3,4,5) #data matematika di ambil didalam folder package file matematika
pangkat = package.matematika.pangkat(2) 
kurang = package.matematika2.kurang(1,2,3,4,5)

print(f"hasil tambah = {tambah}")
print(f"hasil pangkat = {pangkat(5)}")
print(f"hasil kuang = {kurang}")