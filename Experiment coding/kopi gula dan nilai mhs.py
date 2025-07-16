
   
#===================(MEMBUAT KOPI)=================
print ("masukan takaran gula dan kopi dengan perbandingan 2/3 ")
gula = int(input("masukan gula (takaran sendok) : "))
kopi = int(input("masukan kopi (takaran sendok) : "))
jumlah = int(input("masukan jumlah porsi minuman : "))

gula = gula % 2 
kopi = kopi % 3

if gula > kopi :
    hasil = "manis"
elif gula < kopi :
    hasil = "pahit"
elif gula == kopi :
    hasil = "sempurna"
    

print (f"anda membuat {jumlah} porsi kopi dengan rasa {hasil}")

#===================(INPUT NILAI MAHASISWA)=============

nama = input("masukan nama : ")
stb = int(input("masukan no stb anda : "))
nilai = float(input("masukan nilai ujian anda : "))

if nilai >= 85 :
    hasil = "A"  
elif nilai >= 70 :
    hasil = "B"
elif nilai >= 55 :
    hasil = "C"
elif nilai >= 20 :
    hasil = "D"
elif nilai >= 20 :
    hasil = "D"
else :
    print ("salah masukan nilai")
    
print (f"""
nama anda : {nama}       
no stb anda : {stb}        
nilai raport anda : {hasil}       
       """)
    

