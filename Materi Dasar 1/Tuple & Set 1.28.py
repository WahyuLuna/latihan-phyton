
#Data List
data_list = [1,2,3,4,5,6,7,8,9]
print(type(data_list))
print(data_list)


#Data Tuple (tidak bisa di rubah isi datanya) symbol = ()
#lebih ringan di bandingkan LIST
#lebih cepat prosesnya di bandingkan LIST
data_tuple = (1,2,3,4,5,6,7,8,9)
print(type(data_tuple))
print(data_tuple)

#Data Set (data yang tidak memiliki index) symbol = {}
#akan otomatis mengurutkan angka
# apabila ada data yang sama akan di jadikan satu
data_set = {1,8,5,9,7,4,6,2,3,3,3}
data_ganjil = {1,3,5,7,9}
data_genap = {2,4,6,8,10}
data_set2 = (data_ganjil.union(data_genap)) #mengambungkan data
data_set3 = (data_ganjil.intersection(data_set)) #mengambil data yang  memiliki duplikat yang sama dengan data sebelumnaya

print(type(data_set))
print (data_set)
print (data_set2)
print (data_set3)

# apa yang data di kerjakan riap type data
print("="*10)
print(dir(data_list))
print("="*10)
print(dir(data_tuple))
print("="*10)
print(dir(data_set))