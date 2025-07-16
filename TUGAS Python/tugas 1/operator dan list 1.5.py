# operator  + menyambung dua LIST

a = [1,2,3]
b = [4,5,6]

c = a + b
print(c)

# operator  + mengulang isi list LIST

a = [0]
b = [1,2,3]

print(a*4)
print(b*3)

# operator slice (yaitu a:b) bekerja pada list

t = ['a','b','c','d','e','f','g']
print( t[1:3])
print( t[:4])
print( t[2:])

# LIST ADT

    # Append list

pyList = [1,2,3,4,5,6]

pyList.append(50)
pyList.append(18)
pyList.append(64)
print(pyList)

    # extend LIST

pyListA = [32,12]
pyListB = [4,6,31,9]

pyListA.extend(pyListB)
print(pyListA)

    # insert LIST

pyList = [1,2,3,4,5,6]
pyList.insert(3,79)
print(pyList)

    # Pop LIST

pyList = [1,2,3,4,5,6]
pyList.pop(0)
print(pyList)

    # Contoh Codingan
    
# 1

t = ['a', 'b', 'c', 'd']
del(t[1])
print(t)

# 2

t = ['a', 'b', 'c', 'd','e', 'f']
del(t[1:5])
print(t)

# 3

s = 'spam'
t = list(s)
print(t)

# 4

s = 'pining for the fjord'
t = s.split()
print(t)


# 5

t = ['pining', 'for', 'the', 'fjord']
delimiter = ' '
data = delimiter.join(t)
print(data)


# 6

s = 'spam-spam-spam'
delimiter = '-'
data = s.split(delimiter)
print(data)
