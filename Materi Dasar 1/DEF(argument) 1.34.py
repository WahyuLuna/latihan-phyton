"""FUNGTION DENGAN ARGUMENT(INPUT)"""

#string
def fungsi(nama):
    print(f"nama saya adalah {nama}")
    
nama = "wahyu"
fungsi(nama)

#perhitungan
def tambah(data1, data2):
    hasil = data1 + data2
    print(f"{data1} + {data2} = ", hasil)
    
tambah(3,5)    

#for loop 

def sambutan(tamu):
    data_tamu = tamu.copy() #mengunakan copy agar tidak mengubah data di luar fungtion
    for i in data_tamu:
        print(f"yang terhormat {i}")
        
peserta = ["wahyu", "asep", "ucup", "zaki"]
sambutan(peserta)

        
