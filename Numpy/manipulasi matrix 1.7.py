import numpy as np

a = np.array(([1,2,3],    
              [4,5,6] ))

print(a)
print("ukuran matrix a = ", a.shape)

# Tranpost matrix
print("Tranpost matrix")
trans = a.transpose()
print(trans)
trans = np.transpose(a)
print(trans)

# Flater aray,vektor baris
print("Flater aray,vektor baris")
flater = a.ravel()
print(flater)

flater = np.ravel(a)
print(flater)

# Rershape
print("Reshape")
reshape = a.reshape(3,2)
print(reshape)


# Rezise (akan mengubah nilai a secara permanen dengan bentuk yg ditentukan) 
print("Resize")
resize = a.resize(3,2)
print(a)
print("ukuran matrix a = ", a.shape)

