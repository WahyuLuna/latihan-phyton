import numpy as np

#membuat vektor
a = np.array([1,2,3,4,5,6])
b = np.array([1,2,3,4,5,6])

#membuar vektor dengan range(menampilkan angka dalam jarak tertentu)

c = np.arange(1,20,2)

# membuat linspace (menampilkan 4 anggka dalam jarak 1-20 )
d = np.linspace(1,20,4)


# membuat array multy deimansi \ matrix

e = np.array([(1,2,3,4),(1,2,3,4)])

# membuat matrix dengan nilai 0
f = np.zeros([3,5])#([tinggi, lebar])

# membuat matrix dengan nilai 1
g = np.ones([3,5])#([tinggi, lebar])

# membuat matix intetitas
h = np.identity(5)#([tinggi, lebar])
h1 = np.eye(3)#([tinggi, lebar])




#display

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(h1)

