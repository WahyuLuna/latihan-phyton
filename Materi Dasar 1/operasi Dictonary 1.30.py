

data = {
    "nam1" : "wahyu",
    "nam2" : "luna",
    "nam3" : "wijaya",
    "nam5" : ""
    
}

LENDICT = len(data)
print(F"panjand data dictonary : {LENDICT}")

#mengecek key exist atau tidak
print("\n mengecek key exist atau tidak \n")
#True
KEY = "nam1"
CHECKKEY = KEY in data
print(f"apakah {KEY} ada di dalam data dictonary : {CHECKKEY}")

#False
KEY = "nam4"
CHECKKEY = KEY in data
print(f"apakah {KEY} ada di dalam data dictonary : {CHECKKEY}")

#mengakses value (read) dengan get
print("\n mengakses value (read) dengan get \n")
print(data["nam2"])# bila datanya tidak ada = error
print(data.get("nam3"))
print(data.get("nam4")) # bila datanya tidak ada = None
print(data.get("nam4", "file tidak ada")) #midofikasi pemberitahuan


#mengupdate data 
print("\n mengupdate data \n")
data["nam5"] = "wahyu luna wijaya"
print(data)

data.update({"nam5":"kosong"})
print(data)

data.update({"nam6":"Wahyu Luna Wijaya"})
print(data)

#menghapus data dictonary 
print("\n menghapus data \n")
del data["nam5"]
print(data)




