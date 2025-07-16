
# scope variabel = Local

nama = "wahyu" # global

def ubah_nama(nama_baru):
    nama = nama_baru
    print (f"saya ubah nama local menjadi : {nama}.") #lokal
    
ubah_nama("luna")
print(f"saya ganti menjadi nama global {nama}") # global


# scope variabel = Global   (mengubah variabel asli )

nama = "wahyu" #global

def ubah_nama(nama_baru):
    global nama 
    nama = nama_baru
    print (f"saya ubah nama local menjadi : {nama}.") #global
    
    
ubah_nama("luna")
print(f"saya ganti menjadi nama global {nama}") #Global


nama = "wahyu" #global
makan = "sate"

def ubah_nama(nama_baru):
    global nama
    nama = nama_baru
    print (f"saya ubah nama local menjadi : {nama}.") #global
    
def kasih_makan (makanan,nama_baru):
    global nama,makan
    nama = nama_baru
    makan = makanan
    
ubah_nama("luna")
kasih_makan("rendang", "wijaya")
print(f"saya ganti menjadi nama global {nama}, dan makan {makan}") #Global

