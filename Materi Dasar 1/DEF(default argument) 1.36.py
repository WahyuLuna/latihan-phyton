
#def fungtion(argument = nilai default)

print("\ndengan argument")
def sapa(nama): #akan bekerja dengan argumen yang telah di devenisikan
    print(f"hallo {nama}")   
sapa("wahyu") #argument yang didevenisikan "wahyu"

def bicara(nama, pesan):
    print(f" hai {nama}, {pesan}")
    
bicara("wahyu", "apa kabar mu")#variable pesan di devenisikan

print("\ntanpa argument") # jika tidak ada argument yang di input maka akan menggunakan argumen yang di devenisikan
def sapa2(nama2 = 'ganteng'): # argument yg di defenisikan adalah "ganteng"
    print(f"hallo {nama2}")
sapa2()#tanpa argument

def bicara(nama, pesan = "dimana rumah mu ?"):
    print(f" hai {nama}, {pesan}")
    
bicara("wahyu") #variable pesan tidak di devenisikan

#contoh 2

def kuadrat(angka, pangkat):
    hasil = angka**pangkat
    return hasil

print (kuadrat(5,2))
hasil = kuadrat(angka=5, pangkat=3)
print(hasil)
    
#contoh 3
def tambah(a1=1,a2=2,a3=3,a4=4,a5=5):
    jumlah = a1+a2+a3+a4+a5
    return jumlah

print(tambah())
print(tambah(a1=0,a2=0))
