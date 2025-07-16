

#format string
#string (kata/huruf)
nama = "wahyu"
format = f"hello {nama}"
print (format)

#bolean

boolean = True
format = f"boolean = {boolean}"
print(format)



#angka

angka = 2003.12
format = f"angka ={angka}"
print(format)

#bilangan jutaan
angka = 15000000 
format = f"angka ={angka:,}"
print(format)

#bilangan desimal
desimal = 2003.1812
format = f"desimal ={desimal:.2f}"
print(format)


#menampilkan leading zero 0
desimal = 2003.1812
format = f"desimal ={desimal:09.2f}"
print(format)

#menampilkan tanda +/-

minus = -10
plus = 10.1234
formatminus = f"minus = {minus:-d}"
formatplus = f"plus = {plus:+.2f}"
print(formatminus)
print(formatplus)

#format presentase
presentase = 0.0456
format = f"presentase{presentase:.2%}"
print(format)

#melakukan operasi aritmatika
harga = 10000
jumlah = 5

format  = f"harga total = {harga*jumlah:,}"
print(format)

#format binary,octal,hexdecimal

angka = 1812
binary = f"binary = {bin(angka)}"
octa = f"octa = {oct(angka)}"
hexdecimal = f"hexdecimal = {hex(angka)}"

print(binary)
print(octa)
print(hexdecimal)








