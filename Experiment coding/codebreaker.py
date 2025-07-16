
data = int(input("masukan tiga digit angka : "))
data2 = str(data)
panjang = len(data2)
print(panjang)
code = 111
while True:
    
    if code == data:
        print("True")
        print("Password anda adalah = ",code)
        break
    else:
        print("false")
        code = code + 1
        
        