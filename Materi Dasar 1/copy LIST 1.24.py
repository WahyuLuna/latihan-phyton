
# cara duplikat list

a = ["wahyu", "luna", "wijaya"]
print (f"a = {a}")

b=a
print (f"a = {b}")

# mengubah member
a[1] = "lutrax"

print (f"a = {a}")
print (f"a = {b}")

#addres kedua
print("tanpa ada perintah copy maka id akan :")
print (f"addres a = {id(a)}")
print (f"addres b = {id(b)}")
print (f"addres a = {hex(id(a))}")
print (f"addres b = {hex(id(b))}")


#menduplikat data

c= a.copy
print("dengan ada perintah copy maka id akan :")
print (f"addres a = {id(a)}")
print (f"addres c = {id(c)}")
print (f"addres a = {hex(id(a))}")
print (f"addres c = {hex(id(c))}")














