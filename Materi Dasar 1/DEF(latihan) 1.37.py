
"""Tanpa Menggunakan metode Fungtion"""

print(f"{'Cara 1 tanpa DEF':^40}") #gunakan perintah ":^40" untuk membuat kalimat berada di tengah
print(f"{'Menghitung Luas Dan keliling pergegi panjang':^40}")
print(f"{'-'*40 :^40}")
lebar = int(input("masukan lebar :"))
panjang = int(input("masukan tinggi :"))
luas = lebar*panjang
keliling = 2*(panjang*lebar)
print(f"Luas dari persegi adalah {luas}")
print(f"keliling dari persegi adalah {keliling}")

"""Menggunakan metode Fungtion"""

def header():

    print(f"{'Cara 2 dengan DEF':^40}") #gunakan perintah ":^40" untuk membuat kalimat berada di tengah
    print(f"{'Menghitung Luas Dan keliling pergegi panjang':^40}")
    print(f"{'-'*40 :^40}")
    
def input_user():
    lebar = int(input("masukan lebar :"))
    panjang = int(input("masukan tinggi :"))
    return lebar, panjang

def hitung_luas(lebar, panjang):
    luas = lebar*panjang
    keliling = 2*(panjang*lebar)
    return luas, keliling

def output():
    print(f"Luas dari persegi adalah {luas}")
    print(f"keliling dari persegi adalah {keliling}")
    
while True:
    header()
    input_user()
    output()
    isContinue = input("apakah Lanjut [y/n] : ")
    if isContinue == "n":
        break
print("program selesai")
