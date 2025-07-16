from inspect import *
from queue import Empty

class ArrayStack:
	# LIFO Stack implementation memakai list sebagai penyimpanan
    def __init__(self):
        # inisialisasi, tumpukan kosong
        self._data = []  # nonpublic list instance
    def __len__(self):
        # memberikan tinggi tumpukan
        return len(self._data)
    def is_empty(self):
        # True bila tumpukan kosong
        return len(self._data) == 0
    def push(self, e):
        # memasukkan elemen e di posisi top
        self._data.append(e)  # new item stored at end of list
    def top(self):
        # melihat elemen di posisi top
        # elemen tidak diambil
        # bila stack kosong , error
        if self.is_empty():
            raise Empty("Stuck is empty")
        return self._data[-1]  # the last item in the list
    def pop(self):
        # mengambil elemen di posisi top
        #Raise Empty exception if the stack is empty.
        if self.is_empty():
            raise Empty("Stuck is empty")
        return self._data.pop()
    def peek(self):
        #peek the top element equals to top()
        if self.is_empty():
            raise Empty("Stuck is empty")
        return self._data[-1]
  