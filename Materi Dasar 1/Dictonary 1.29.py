
#array/LIST --> diakses menggunakan index [0-dst]

data_list = ["Wahyu","luna","wijaya"]
print(data_list[0])


# Dictonary (dict ---> associative LIST/array)
#indentifier -> key (ingat tanda , di akhir data)

data_dict = {
    "key1" : "value1",
    "wlw" : "wahyu luna wijaya",
    "number": 100,
    "list": data_list
}

print(data_dict["key1"])
print(data_dict["wlw"])
print(data_dict["number"])
print(data_dict["list"])


member1 = {"ID": 100, 
           "name": "wahyu luna wijaya",
           "class": "TI",
           "status":"Pelajar"}

member2 = {"ID": 101, 
           "name": "asep bin ngeles",
           "class": "TI",
           "status":"Pelajar"}

member3 = {"ID": 102, 
           "name": "Rehan Van Bogor",
           "class": "TI",
           "status":"Dosen"}

memberlist = {100:member1,101:member2,102:member3}

print(memberlist[100])
print(memberlist[101])
print(memberlist[102])








