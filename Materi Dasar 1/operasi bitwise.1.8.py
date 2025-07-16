
a = 9
b = 5

#=====(OR'|')=======
c = a | b
print("\n ===========OR=============")
print ("Nilai :",a, " , Binary :", format(a ,'08b'))
print ("Nilai :",b, " , Binary :", format(b ,'08b'))
print("============================(|)")
print ("Nilai :",c, " , Binary :", format(c ,'08b'))

#=====(AND'&')=======
c = a & b
print("\n ===========AND=============")
print ("Nilai :",a, " , Binary :", format(a ,'08b'))
print ("Nilai :",b, " , Binary :", format(b ,'08b'))
print("============================(&)")
print ("Nilai :",c, " , Binary :", format(c ,'08b'))

#=====(XOR'^')=======
c = a ^ b
print("\n ===========XOR=============")
print ("Nilai :",a, " , Binary :", format(a ,'08b'))
print ("Nilai :",b, " , Binary :", format(b ,'08b'))
print("============================(^)")
print ("Nilai :",c, " , Binary :", format(c ,'08b'))

#=====(NOT'~')=======
c = ~a 
print("\n ===========NOT=============")
print ("Nilai :",a, " , Binary :", format(a ,'08b'))
print("============================(~)")
print ("Nilai :",c, " , Binary :", format(c ,'08b'))
#diakali dangan operator XOR
print("============================(^)")
d= 0b0000001001
e= 0b1111111111
print ("Nilai :",e^d, " , Binary :", format(e^d ,'08b'))

#=====(SHIFTING 'left <<' or 'right>>')=======

#SHIFTTING RIGHT (>>)
c= a >> 2
print("\n ===========SHIFTING (RIGHT)=============")
print ("Nilai :",a, " , Binary :", format(a ,'08b'))
print("============================(>>)")
print ("Nilai :",c, " , Binary :", format(c ,'08b'))

#SHIFTTING LEFT (<<)
c= a << 2
print("\n ===========SHIFTING (LEFT)=============")
print ("Nilai :",a, " , Binary :", format(a ,'08b'))
print("============================(<<)")
print ("Nilai :",c, " , Binary :", format(c ,'08b'))
















