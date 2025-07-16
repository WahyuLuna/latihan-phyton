
teman = {
    
    "t1" : "wahyu",
    "t2" : "luna",
    "t3" : "wijaya",
    "t4" : "asep",
    "t5" : "risky",
}

print(teman)

# looping firs try (yang keluar adalah key)

for data in teman :
    print(data)

# untuk mengambil item

# menggunakan keys
keys = teman.keys()
print(keys)

for key in teman.keys():
    print(teman.get(key))


# menggunakan values

values = teman.values()
print(keys)

for values in teman.values():
    print(values)

# menggunakan items
items = teman.items()
print(keys)

for items in teman.items():
    print(items)


for key,values in teman.items():
    print(f"key = {key}, value = {values}")

