
#operasi komparasi

#sertiap hasil dari operasi koprasi adalah bolean

# >, <,>=,<=,==,!=,is,is not

from operator import is_not


a = 3
b = 2

hasil = a > 10
print (a,'>',10,'=',hasil)
hasil = b < 10
print (b,'<',10,'=',hasil)
hasil = a >= 10
print (a,'=>',10,'=',hasil)
hasil = b <= 10
print (b,'<=',10,'=',hasil)
hasil = a == 10
print (a,'==',10,'=',hasil)
hasil = b != 10
print (b,'!=',10,'=',hasil)

# perbandingan is / is not

# 'is'/'is not' serbagai kompararasi objek identifity
# tambahkan Hex untuk melihat id objek

x= 5
y= 5
m= 10
n= 12

print ("nilai x = ",x,"id = ",hex(id(x)))
print ("nilai y = ",y,"id = ",hex(id(y)))
print ("nilai m = ",m,"id = ",hex(id(m)))
print ("nilai n = ",n,"id = ",hex(id(n)))


print ("hasil perbandingan is")
hasilxy = x is y
hasilmn = m is n
print ("x is y =", hasilxy)
print ("m is n =", hasilmn)

print ("hasil perbandingan is not")
hasilxy = x is not y
hasilmn = m is not n
print ("x is y =", hasilxy)
print ("m is n =", hasilmn)













