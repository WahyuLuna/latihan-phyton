
#operasi logika atau bolean

# not, or, and, xor

print("===== NOT ====")
a = True
c= not a
print("DATA a = ",a)
print ("DATA C = ",c)

#or (apa bila salah satu true maka hasilnya akan true)

print("===== OR ====")
a= False
b= False
c= a or b
print (a,"or",b,'=', c)

a= False
b= True
c= a or b
print (a,"or",b,'=', c)

a= True
b= False
c= a or b
print (a,"or",b,'=', c)

a= True
b= True
c= a or b
print (a,"or",b,'=', c)

#AND (apabila salah satu false maka hasilnya akan menjadi false)

print("===== AND ====")
a= False
b= False
c= a and b
print (a,"and",b,'=', c)

a= False
b= True
c= a and b
print (a,"and",b,'=', c)

a= True
b= False
c= a and b
print (a,"and",b,'=', c)

a= True
b= True
c= a and b
print (a,"and",b,'=', c)

#XOR (akan false apabila ada yang sama)

print("===== XOR ====")
a= False
b= False
c= a ^ b
print (a,"^",b,'=', c)

a= False
b= True
c= a ^ b
print (a,"^",b,'=', c)

a= True
b= False
c= a ^ b
print (a,"^",b,'=', c)

a= True
b= True
c= a ^ b
print (a,"^",b,'=', c)


























