
#berfungsi sebagai kata kunci dalam duatu fungtion yang di input

def data(**kwargs):
    print(kwargs)
    print(kwargs["nama"])
    print(kwargs["berat"])
    print(kwargs["tinggi"])
    
data(nama = "ucup",berat=70,tinggi=170)

def data2(**list):
    nama = list['nama']
    tinggi = list["berat"]
    berat = list["tinggi"]
    print(f"{nama} punya tinggi {tinggi} dan Berat {berat}")
    
data2(nama = "asep",berat=80,tinggi=165)

# contoh penggabungan kwargs dan args dan

def math(*args,**kwargs):
    output = 0
    if kwargs["opsi"] == "tambah":
        for angka in args:
            output += angka
        print(f"operasi penjumlahan ")
    elif kwargs["opsi"] == "kurang":
        for angka in args:
            output -= angka
        print(f"operasi pengurangan ")
    return output
        
hasil = math(1,2,3,4,5,6,7,8,opsi="tambah")  
print(f"hasil jumlah {hasil}")      
hasil = math(1,2,3,4,5,6,7,8,opsi="kurang")        
print(f"hasil kurang {hasil}")         
        