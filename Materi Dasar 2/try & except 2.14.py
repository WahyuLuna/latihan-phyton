
#try dan except berguna untuk mengganti pemberitauan error vscode, menjadi suatu metode lain

while True:
    try:
        angka = int(input("masukan angka : "))
        break
    except:
        print("ini bukan angka")

print(f"angka yang anda masukan adalah : {angka}")

while True:
    try:
        penyebut = int(input("masukan penyebut : "))
        pembilang = int(input("masukan pembilang : "))
        hasil =  penyebut / pembilang
        break
    
    except ValueError:
        print("ini bukan angka ")
    except ZeroDivisionError:
        print(" angka pembilang yang anda masukan nol silahkan masukan angka lain")
    
print (f"hasil perhitungan : {hasil}")


while True:
    try:
        angka = int(input("masukan angka : "))
        break
    except Exception as rr:
        print(rr)

print(f"angka yang anda masukan adalah : {angka}")

"""
type exception error
1. IDError (error input img dll)
2. ImportError (error input import)
3. ValueError    
4. keyboardInterupted

    """