import re



result = re.search(r"^(\w*), (\w*)$","rindding, bike")
print(result)

def rearange_name(name):
    result = re.search(r"^(\w*), (\w*)$",name)
    if result is None:
        return name
    return "{} is {}".format(result[2], result[1])

print(rearange_name("bad, piggies"))
print(rearange_name("bad, piggies hahah"))


# agar dapat mengambil angka hingga akhir

def rearrange_name(name):
  result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)


# untuk mencari kata dengan jumlah spesifik
result = re.search(r"[a-zA-Z]{5}","a apple wet again yesterday")
print(result)

# untuk mencari semua kata dengan jumlah spesifik tetapi tidak sempurna
result = re.findall(r"[a-zA-Z]{5}","a apple wet again yesterday")
print(result)

# untuk mencari semua kata dengan jumlah spesifik dengan sempurna
result = re.findall(r"\b[a-zA-Z]{5}\b","a apple wet again yesterday")
print(result)

# untuk mencari semua kata dengan jumlah spesifik dan berbeda dengan sempurna
#{jumlah min, jumlah max}
result = re.findall(r"\w{5,9}","a apple wet again yesterday")
print(result)

# mencari kata dengan awalan yang ditentukan hingga max panjang kata
result = re.search(r"y\w{,20}","a apple wet again yesterday")
print(result)


def long_words(text):
  pattern = r"[a-z]\w{6,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []



log = "july 31 07:51:48 mycomputer bad_procces[12345]: ERROR Performing package upgrade"
def extract(log):
    regex = r"\[(\d+)\]" 
    result = re.search(regex,log)
    if result is None:
        return "wrong input"
    return result[1]

print(extract(log))
print(extract("july 31 07:51:48 mycomputer bad_procces[wow]: ERROR Performing package upgrade"))


# untuk memisahkan elemen bedasarkan batas symbol
result = re.split(r"[.?!]","a apple. wet again! yesterday?")
print(result)

result = re.split(r"([.?!])","a apple. wet again! yesterday?")
print(result)

# untuk manipulasi string yang tidak dibutuhkan

result = re.sub(r"[\w.%+-]+@[\w.-]+","[SENDED]","send an email for go_nutshel12@gmail.com")
print(result)

result = re.sub(r"^([\w .-]*), ([\w .-]*)$",r"\2 \1","riding, bike")
print(result)









