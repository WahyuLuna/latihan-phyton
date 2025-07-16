

data_1 = []
y = 0
print("===========(INPUT PESERTA)===========")
jumlah = int(input("masukan banyak orang yg ingin di data : "))
    
while jumlah > y :
        
        # input data
    nama = str(input("\nmasukan nama anda : "))
    umur = str(input("masukan umur anda : "))
    jk = str(input("masukan jenis kelamin anda : "))
    list_data = [nama, umur, jk]
        #proses input data
    y += 1
    data_1.append(list_data)

print("===========(HASIL INPUT PESERTA)===========")
   
for peserta in data_1 :
    print (f"nama\t :{peserta[0]}")
    print (f"umur\t :{peserta[1]}")
    print (f"kelamin\t :{peserta[2]}\n")

