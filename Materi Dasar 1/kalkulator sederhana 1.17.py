
print (f"================ \n Kalkulator Sederhana \n================\n")

a1 = float(input("Masukan Angka 1 : "))
op = input(f"Masukan jenis operasi perhitungan (+,-,*,/,%) : ")
a2 = float(input("Masukan Angka 2 : "))

if op == "+":
    hasil = a1 + a2

elif op == "-":
    hasil = a1 - a2

elif op == "x" or op == "*" :
    hasil = a1 * a2

elif op == "/":
    hasil = a1 / a2

elif op == "%":
    hasil = a1 % a2

else :
    print ("yang bener dong input data nyaa....")

print (f"hasil dari {a1} {op} {a2} = {hasil}")
