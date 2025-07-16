
nama = "wahyu luna"
umur = 18
tinggi = 165.5
nomorsepatu = 42


#normal String standar
string =  f"nama = {nama}, umur = {umur}, tinggi = {tinggi}, nomor sepatu = {nomorsepatu}"
print (5*"=", "Data string", 5*"=")
print(string)

#String Multiline
string =  f"nama = {nama}, \numur = {umur}, \ntinggi = {tinggi}, \nnomor sepatu = {nomorsepatu}"
print ('\n', 5*"=", "Data string", 5*"=")
print(string)

#string miltyline (kutip triplets)
# cara rapat ke kanan
string = f""" 
nama            = {nama:>15}
umur            = {umur:>15}
tinggi          = {tinggi:>15}
nomor sepatu    = {nomorsepatu:>15}

"""
print ('\n', 5*"=", "Data string", 5*"=")
print(string)



















