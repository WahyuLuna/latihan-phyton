
class nilai_mhs :
    def __init__(self,mtk,ipa,ips,ipk,total):
        self.mtk = mtk 
        self.ipa = ipa
        self.ips = ips
        self.ipk = ipk
        self.total = total
        
    def hasil_mhs(self):
        self.total = (self.ipa + self.ips + self.mtk)
        self.ipk = self.total / 3
        print(f"""
    nilai mtk                 = {self.mtk}
    nilai ipa                 = {self.ipa}
    nilai ips                 = {self.ips}
    total rata" nilai saya    = {self.ipk}              
              """)
        
class data_mahasiswa :
    def __init__(self, nama, umur, asal):
        self.nama = nama
        self.umur = umur
        self.asal = asal
    
    def perkenalan(self):
        print(f" nama saya {self.nama}\n umur {self.umur}\n dan berasal dari {self.asal}")
       

def pil1():
    data = data_mahasiswa(
        nama = input("\n masukan nama anda : "),
        umur = input(" masukan umur anda : "),
        asal = input(" masukan asal anda : "),
    )    
    data.perkenalan()
    print("\n==========(TERIMAKASIH TELAH MENGINPUT DATA==========")    

def pil2():
    data2 = nilai_mhs(
        ipa = float(input("\n masukan nilai ipa anda : ")),
        ips = float(input(" masukan nilai ips anda : ")),
        mtk = float(input(" masukan nilai mtk anda : ")),
        total = 0.0,
        ipk = 0.0
    )
    data2.hasil_mhs()
    print("\n==========(TERIMAKASIH TELAH MENGINPUT DATA==========") 
  
print("""
========(masukan opsi yang anda ingin)=======
1. menginput data-mahasiswa
2. menginput nilai_mhs
3. menginput data_mahasiswa dan nilai_mhs     
\n""")
pil = int(input("masukan pil anda : "))     
     
        
if pil == 1:
    pil1()
elif pil == 2 :
    pil2()  
elif pil == 3 :
    pil1()
    pil2()
else :
    print("anda salah menginput pilihan")

print("\n==========(TERIMAKASIH TELAH MENGINPUT DATA==========")      