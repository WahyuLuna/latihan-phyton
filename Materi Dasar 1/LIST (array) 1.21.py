
#data list string
data_nama = ["wahyu", "luna", "wijaya"]
print (data_nama)

#data list integer
data_angka = [1,2,3,4,5]
print (data_angka)

#data list boolean
data_boolean = [True, False, True, True]
print (data_boolean)

#data list campuran
data_campuran = ["wahyu", 18, True]
print (data_campuran)

#data list range
data_range = range(0, 10)
data_list = list(data_range)
print (data_list)


#membuat list dengan for loop

data_list_for = [i**2 for i in range(0, 10)]
print (data_list_for)


#data list dengan for if

data_list_for_if = [ i for i in range(0, 10)if i != 5]
print (data_list_for_if)

#data list genap
data_list_for_if = [ i for i in range(0, 20)if i%2 == 0]
print (data_list_for_if)

#data list ganjil
data_list_for_if = [ i for i in range(0, 20)if i%2 != 0]
print (data_list_for_if)






