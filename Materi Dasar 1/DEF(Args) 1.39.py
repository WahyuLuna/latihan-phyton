#digunakan untuk memasukan data dalam jumlah yang banyak

def data(nama,tinggi,berat): #jika tidak menggunakan args maka butuh mendefinidsikan banyak hal
     print(f"{nama} punya tinggi {tinggi} dan Berat {berat}")
     
data("ucup", 170,180)

def data2(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan Berat {berat}")
data2(["ucup", 170,180])

# contoh codingan Args (menggunakan symbol (*) di dalam data)
# kita tidak perlu membuat banyak argumen   def contoh(argumen1,2,3,....)<- jika tidak menggunakan args
# jika mengunakan args    def contoh(*argument)<- cukup dengan 1 argument


def data3(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan Berat {berat}")
data3("ucup", 170,180)

#contoh implementasi
def tambah(*data):
    hasil = 0
    for i in data:
        hasil += i
    return hasil

output = tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil = {output}")

output = tambah(24,85,46)
print(f"hasil = {output}")


        
