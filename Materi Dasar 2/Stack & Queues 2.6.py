# Stack (mengambil data yg paling akhir masuk)

data = [1,2,3,4,5,6]
print (data)
data.append(7)
print ("data yang masuk",data)
data.append(8)
print ("data yang masuk",data)

out = data.pop()
print("data yang keluar",out)
print("data sekarang ",data)

# Queues (mengambil data sesuai antrian masuk)

from collections import deque

antrian = deque([1,2,3,4,5,6])
print (antrian)
antrian.append(7)
print ("data yang masuk",antrian)
antrian.append(8)
print ("data yang masuk",antrian)
out = antrian.popleft() # mengambil data dari kiri
print("data yang keluar",out)
print("data sekarang ",antrian)
out = antrian.popleft() # mengambil data dari kiri
print("data yang keluar",out)
print("data sekarang ",antrian)