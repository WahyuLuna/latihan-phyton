import numpy as np

a = np.arange(10)**2

print(a)

#indexing
print("nilai a paling awal : ", a[0])
print("nilai a paling akhir : ",a[-1])


#sciling
print("nilai 1-5 elemen a  : ",a[0:4])
print("nilai awal-5 elemen a  : ",a[:5])
print("nilai 4-akhir elemen a  : ",a[3:])

#iterensi

for i in a:
    print("value = ",i)

