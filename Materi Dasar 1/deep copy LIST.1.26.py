
data_1 = [1,2]
data_2 = [3,4]

data_2d = [data_1, data_2]
data_2d_copy = data_2d.copy()

print(f"data = {data_2d}")
print(f"data copy= {data_2d_copy}")

#Mengambil

#yang rendah
data = data_2d[0] [1]
print(f" data = {data}")
#yang tinggi
data = data_2d[1] [0]
print(f" data = {data}")

#addres semuanya

print(f"data 2d         = {hex(id(data_2d))}")
print(f"data 2d_copy    = {hex(id(data_2d_copy))}")

print("addres dari member 1")
print(f"data 2d         = {hex(id(data_2d[0]))}")
print(f"data 2d_copy    = {hex(id(data_2d_copy[0]))}")


#mengunakan DEEP COPY

from copy import deepcopy

data_2d = [data_1, data_2,10]
data_2d_deepcopy = deepcopy(data_2d)

print(f"data 2d             = {hex(id(data_2d))}")
print(f"data 2d_deepcopy    = {hex(id(data_2d_deepcopy))}")

print("addres dari member 1")
print(f"data 2d             = {hex(id(data_2d[0]))}")
print(f"data 2d_deepcopy    = {hex(id(data_2d_deepcopy[0]))}")

data_2d[1][0] = 30
print(f"data = {data_2d}")
print(f"data copy = {data_2d_copy}")
print(f"data deep copy= {data_2d_deepcopy}")



