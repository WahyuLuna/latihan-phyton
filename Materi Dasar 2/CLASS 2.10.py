
  # variable self.
class mahasiswa1():
    nama  = 'unkow name'
    
    def __init__(self): #(_init_)akan langsung terpanggil apa bila class "mahasiswa" di panggil
        print("ini adalah init")
    
    def belajar(self,kondisi): # untuk mengetahui self milik siapa / hanya akan muncul jika di panggil
        print(self.nama ,"sedang belajar",kondisi)
        
    def belajar1(self,): # untuk mengetahui self milik siapa / hanya akan muncul jika di panggil
        print(self.nama ,"sedang belajar")
        
    def tidur(self): # untuk mengetahui self milik siapa / hanya akan muncul jika di panggil
        print(self.nama ,"sedang tidur")
  
  # variable __init__  
class mahasiswa2():
    
    def __init__(self,data,stb): #akan langsung terpanggil apa bila class "mahasiswa" di panggil
        print("ini adalah init")
        self.nama = data
        self.nim = stb
    
    # variable Privar
class ujian():
    
    __nilai = 0 # apabila sebuah variabel di awali __(dua garis bawah) maka nilai tsb tidak dapat di ubah di luar class
    
    def uts(self,input_nilai):
        self.__nilai += input_nilai
        print(f"nilai kamu = {self.__nilai}")
    
    def hasil (self):
        if self.__nilai <= 50:
            print("kamu gagal")
        elif self.__nilai <= 80:
            print("nilai kamu lumayan bagus")
        elif self.__nilai <= 100:
            print("nilai kamu bagus sekali")
  
    # variable class
class kuliah():
    jurusan = "tehnik informatika"
    jumlah_mhs = 0
    def __init__(self,input_nama,input_nim):
        self.nama = input_nama
        self.nim = input_nim
        print(self.nama,self.nim)
        kuliah.jumlah_mhs += 1 # menghiting julah data yang masuk pada DEF ini
        
    # Class inheritance
class ojek():
    def __init__(self, nama,daerah,kendaraan):
        self.nama = nama
        self.daerah = daerah
        self.kendaraan = kendaraan
        
    def cek_data(self):
        print(f"\nnama : {self.nama} \ndaerah : {self.daerah} \nkendaraan : {self.kendaraan}")
        
class Gojek(ojek): #tidak perlu membuat variabel data yang sama, cukup menimpa data yang mau di ganti
    
    def cek_data(self): #contoh data yang mau di timpa
        print("\nsilahkan cek di aplikasi tentang data diri ")
    
#######################################(Main Program)####################################


print("__init__ =================================")
otong = mahasiswa1()#mengunakan class 1
asep = mahasiswa1()#mengunakan class 1
risky= mahasiswa1()#mengunakan class 1
rehan = mahasiswa2("rehan wangsaf", 121086) #mengunakan class 2


asep.nama = "asep suroto"
risky.nama = "risky bogor"
print("\nnama =================================")
print(rehan.nama,rehan.nim)
print(otong.nama)
print(asep.nama)
print(risky.nama)


data = "kurang semangat"
print("\nnama + self + kondisi + keterangnan  =================")

otong.belajar(data)
asep.belajar1()
risky.tidur()

print("\n nilai  ===========================")

ulangan = ujian()
ulangan.uts(45)
ulangan.hasil()

print("\n variable class  ===========================")

ucup = kuliah("ucup surucup", 212088)
otong = kuliah("otong galau", 212077)
wangsaf = kuliah("wangsaf bogor", 212066)

wangsaf.jurusan = "tehnik industri"
print(ucup.jurusan)
print(otong.jurusan)
print(wangsaf.jurusan)
print("jumlah mahasiswa : ",kuliah.jumlah_mhs)


print("\n class inheritance  ===========================")


ojek1 = ojek("ucup surucup", "Makassar", "motor")
ojek2 = ojek("otong galau", "bandung", "mobil")
ojek3 = Gojek("wangsaf bogor", "surabaya", "motor")

ojek1.cek_data()
ojek2.cek_data()
ojek3.cek_data()

