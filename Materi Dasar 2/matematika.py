print(__name__)
angka1 = int(input("masukan angka 1 : "))
angka2 = int(input("masukan angka 2 : "))

def tambah():
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")
    
def kurang():
    hasil = angka1 - angka2
    print(f"{angka1} - {angka2} = {hasil}")
    
def bagi():
    hasil = angka1 / angka2
    print(f"{angka1} / {angka2} = {hasil}")
    
def kali():
    hasil = angka1 * angka2
    print(f"{angka1} * {angka2} = {hasil}")

