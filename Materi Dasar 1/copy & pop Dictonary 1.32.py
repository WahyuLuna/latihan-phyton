
teman = {
    
    "t1" : "wahyu",
    "t2" : "luna",
    "t3" : "wijaya",
    "t4" : "asep",
    "t5" : "risky",
}

friends = teman.copy()


print(friends)
print(teman,"\n")

teman["t5"] = "rehan wangsaf"
print(friends)
print(teman,"\n")

#pop dictonary (mentranfer data file dari data1 ke data 2)

data_t5 = friends.pop("t5")
print(data_t5)
print(friends,"\n")


#pop item dictonary (mengambil data paling akhir dari data 1 ke data 2)

data_akhir = friends.popitem()
print(data_akhir)
print(friends)


