import numpy as np

a = np.array(([1,2],    
              [3,4] ))
b = np.array(([1,2],    
              [3,4] ))

print(a)
print(b)

hasil = a*b
print(hasil)

hasil = np.dot(a,b)
print(hasil)
hasil = a.dot(b)
print(hasil)