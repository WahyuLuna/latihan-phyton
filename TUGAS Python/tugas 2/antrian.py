class antrian:
    #implementasi antrian memakai Python list.
    
	def __init__(self):
	    #inisialisasi antrian.
	    self._data = [] # data disimpan dalam list

	def __len__(self):
	    #memberikan jumlah elemen dalam antrian.
	    return len(self._data)

	def size(self):
	    return len(self._data)

	def is_empty(self):
	    #memeriksa apakah antrian kosong.
	    return len(self._data) == 0

	def enqueue(self, x):
	    #memasukkan x ke dalam antrian.
	    self._data.append(x) 

	def dequeue(self):
	    #mengambil elemen terdepan dari tumpukan 
	    #Raise error Exception bila kosong.
	    if self.is_empty():
	        raise Exception('Tumpukan kosong')
	    else:
	        x = self._data[0]
	        self._data.pop(0)
	    return x
	def front(self):
	    #melihat elemen terdepan
	    if self.is_empty():
	        raise Exception('Tumpukan kosong')
	    return self._data[0]

	def rear(self):
	    #melihat elemen paling belakang
	    if self.is_empty():
	        raise Exception('Tumpukan kosong')
	    return self._data[-1]

	def lihat_isi(self):
	    n = self.size()
	    for i in range(n):
	        print(self._data[i])




a=antrian()
a.enqueue(4)
a.enqueue(6)
a.enqueue(8)
a.lihat_isi()

a.dequeue()

a.size()

a.dequeue()

a.dequeue()

a.dequeue()


