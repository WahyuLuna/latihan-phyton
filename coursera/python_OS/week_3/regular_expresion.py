import re

"""
regular expresion digunakan untuk mencari hal spesipik dalam string     
    
    """
# cara manual
log = "july 31 07:51:48 {14747}mycomputer bad_procces[12345]: ERROR Performing package upgrade"
index = log.index('[')
print(log[index+1:index+6])
index = log.index('{')
print(log[index+1:index+6])


# cara otomatis
regex = r"\[(\d+)\]" #menetukan posisi sesuai dengan lokasi data
result = re.search(regex,log)
print(result[1])
regex = r"\{(\d+)\}" #menetukan posisi sesuai dengan lokasi data
result = re.search(regex,log)
print(result[1])


"""

grep thon /usr/share/dict/words
 #hasilnya akan memberikan setiap kata yang mengandung thon didalamnya

grep i- python /usr/share/dict/words
    #hasilnya akan mencari kata Python dari berbagai jenis huruf besar atau kecil

grep l.rts /usr/share/dict/words
    #hasilnya akan mencari kata dengan awalan l dan akhiran rts

grep ^fruit /usr/share/dict/words
    #hasilnya akan mencari kata yang berawlan kata fruit

grep cat$ /usr/share/dict/words
    #hasilnya akan mencari kata yang berakhiran kata cat

"""

# digunakan untuk mencari sebuah kata spesifik dalam sebuah kata
result = re.search(r"aza","plazae")
print(result)

result = re.search(r"aza","bazaar")
print(result)

# jika kasunya tidak ada yang mirip
result = re.search(r"aza","plaz")
print(result)

result = re.search(r"^x","xenom")
print(result)

result = re.search(r"p.ng","penguin")
print(result)

# untuk mencari sesuai definisi tanpa memperhatikan aturan huruf besar atau kecil
result = re.search(r"p.ng","Penguin", re.IGNORECASE)
print(result)

# untuk mencari kata dengan bagian yang telah dientukan
result = re.search(r"[Pp]ython","Python")
print(result)

#mencari awalan dengan bagian yang ditentukan dengan jarak yang ditentukan
# dengan format [a-z],[A,Z], dan [1-9] (maupun campuran)
result = re.search(r"[a-z]yam","saya memiliki seekor ayam")
print(result)

#contoh dengan format lengkap
result = re.search(r"python[a-zA-Z0-9]","python9")
print(result)

#contoh dengan format retentu
result = re.search(r"[^a-zA-Z]","sayasuka ikan")
print(result)

#contoh dengan format | (mencari salah satu)
result = re.search(r"cat|dog"," i like cats.")
print(result)

#contoh dengan format | (mencari salah satu)
result = re.search(r"cat|dog"," i like dogs.")
print(result)

#contoh dengan format | (mencari keduanya)
# menggunakan re.findall
result = re.findall(r"cat|dog"," i like dogs and cats.")
print(result)

#contoh dengan format kata awal hingga tujuan akhir
result = re.search(r"py.*n","python programming")
print(result)

#contoh dengan format kata awal hingga tujuan akhir
# tetapi hanya mengambil 1 kata
result = re.search(r"py[a-z]*n","python programming")
print(result)

#contoh dengan format mencari huruf yang sama tapi masih terhubung
result = re.search(r"o+l+","woolls")
print(result)

#contoh dengan format mencari huruf yang sama prioritas
result = re.search(r"p?each","to each word")
print(result)
result = re.search(r"p?each","to peach word")
print(result)

#contoh dengan format mencari huruf yang akan menggunakan symbol
# gunakan \ untuk mencari kata yang diawali symbol
result = re.search(r".com","welcome")
print(result)
result = re.search(r"\.com","welcome")
print(result)
result = re.search(r"\.com","google.com")
print(result)

# mengambil kata dengan awalan dan akhiran yang di tentukan bahkan dengan spasi
result = re.search(r"^A.*a$","Australia utara")
print(result)

# mencari kata dengan class yang sdh di tentukan
patter = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(patter,"_this_valid_word_"))
print(re.search(patter,"this in valid word"))
print(re.search(patter,"9this_in_valid_word_"))
print(re.search(patter,"this_valid_word_7"))




# mengecek kata yang mengandung a,e,i

def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True



# mengecek kata yang mengandung simbol [.'?!]

def check_punctuation (text):
  result = re.search(r"[!?.']", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False


def repeating_letter_a(text):
  result = re.search(r"[A a].*a", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True


def check_sentence(text):
  result = re.search(r"^[A-Z ].*[.? ]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True


"""

"""

