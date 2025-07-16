import numpy as np

# perbedaan numpy dan arra biasa adlah numpy tidak memiliki koma dan array biasa memiliki koma

a = np.array([1,2,3,4])
b = np.array([1,2,3,4])
c = [1,2,3,4]
print(a)
print(b)
print(c)
print(a + b + c)

a = a + 1
b = b + [1]
c = c + [1]

print(a)
print(b)
print(c)
print(a+b)