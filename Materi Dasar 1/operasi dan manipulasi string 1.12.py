
    #mengubah care dari string
    
    #mengubah ke upper case (mengubah semua menjadi huruf kapital)

salam = "hallo"
print("salam =", salam)

salam = salam.upper()
print("upper =", salam)


   # mengubah semua ke lowercase (mengubah semua menjadi huruf kecil)

alay = "AKU KECE ABEZZZZZZ"
print("alay =", alay)
alay = alay.lower()
print("lower = ", alay)


    # pengecekan lower dan upper case 

salam = "hai apa kabar"
jawab = "AKU BAIK SAJA"

apakah_lower = salam.islower()
apakah_lower1 = jawab.islower()

print (salam," adalah lower =", str(apakah_lower), "\n",jawab," adalah lower =",str(apakah_lower1))



salam = "hai apa kabar"
jawab = "AKU BAIK SAJA"

apakah_upper = salam.isupper()
apakah_upper1=  jawab.isupper()

print (salam," adalah upper =", str(apakah_upper), "\n",jawab," adalah upper =",str(apakah_upper1))

                    #===beberapa contoh perintah===
#isalpha () <------- untuk mengecek semuanya huruf
#isalnum () <------- untuk mengecek semuanya huruf dan angka
#isdecimal () <------- untuk mengecek semuanya angka saja
#isspace () <------- untuk mengecek semuanya spasi, tab, newline, \n
#istitle () <------- untuk mengecek semuanya dimulai dengan huruf besar
#capitalize() <------- untuk mengubah huruf depan kecil menjadi kapital
# () <------- untuk 
# () <------- untuk
# () <------- untuk
# () <------- untuk



# mengecek komponen kata ---- startswith() & endswith()

cek_awal = "jalan ke pantai".startswith("jalan")
cek_akhir = "jalan ke pantai".endswith("pantai")

print ("awal =", str(cek_awal),"\n akhir =", str(cek_akhir))

#menggabungkan komponen join() & split()

pisah = ['aku','adalah','human']
gabung = ' '.join(pisah)
print (pisah,"\n",gabung)

gabungan= "aku&&&adalah&&&human"
print (gabungan,"\n",gabungan.split('&'))

    #alokasi char rjust(), ljust(), center()
    
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kanan = "kanan".rjust(10,"=")
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

kiri = "kiri".ljust(10,"-")
print("'"+kiri+"'")

tengah = "tengah".center(10)
print("'"+tengah+"'")

tengah = "tengah".center(10,":")
print("'"+tengah+"'")

    #kebalikan dari center() yaitu strip()

tengah = tengah.strip(":") #menghilangkan tanda
print("'"+tengah+"'")







