class ArrayQueue:
    #implementasi FIFO queue memakai Python list 
    DEFAULT_CAPACITY = 10 # kapasitas awal antrian baru
    
    def __init__(self):
        #ciptakan antrian baru kosong 
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        #memberikan banyaknya elemen dalam antrian
        return self._size

    def is_empty(self):
      #bila antrian kosong mengembalikan hasil True
        return self._size == 0

    def first(self):
        #menampilkan nilai (tidak mencopot) elemen 
      #yang ada di posisi depan.
        #menampilkan Empty exception bila kosong.
         if self.is_empty():
             raise Exception('Queue is empty')
         return self._data[self._front]

    def dequeue(self):
        #mengeluarkan elemen terdepan dari antrian
        #Raise Empty exception bila kosong.
        if self.is_empty():
             raise Exception('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None 
        # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
         #menambah elemen pada bagian belakang
         if self._size == len(self._data):
            self._resize(2*len(self._data)) 
            # double the array size
         avail = (self._front + self._size) % len(self._data)
         self._data[avail] = e
         self._size += 1
    def _resize(self, cap): 
         # we assume cap >= len(self)
         # lakukan pemekaran bila melampaui
         # kapasitas awal
         old = self._data # keep track of existing list
         self._data = [None]*cap 
         # allocate list with new capacity
         walk = self._front
         for k in range(self._size): 
             # only consider existing elements
             self._data[k] = old[walk] 
             # intentionally shift indices
             walk = (1 + walk) % len(old) 
             # use old size as modulus
         self._front = 0


Q = ArrayQueue()
Q.enqueue(5)
Q.enqueue(3)
print(len(Q))
