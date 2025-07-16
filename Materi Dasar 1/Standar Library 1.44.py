# jika mau melihat Standar Library di (python standar library)<-- cari di google
# jika mau menginstal library python di (pypi)<-- dari di google
from collections import Counter

data=['a', 'b', 'c', 'd', 'e','a','c','b','a']
hitung = Counter(data)
print(f"jumlah data = {hitung}")
print(f"jumlah a = {hitung['a']}")
print(f"jumlah b = {hitung['b']}")

