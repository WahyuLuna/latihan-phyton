"""
dalam menajlankan program ada kemungkinan program tsb error
tetapi error didalam sebuah program dapat berbentuk berbagai jenis error
jika menggunakan if else maka dibutuhkan banyak kondisi
maka salah satu solusinya adalah menggunakan TRY dan EXCEPT



"""


def angka(data):
    try:
        print(data + 10)
    except:
        print("ini bukan angka")

# angka(2)
# angka("rumah")

"""
(Raise dan assert) adalah metode untuk menciptakan error dengan keterangan sesuai apa yang kita tetapkan
"""

def valid_user(username, minlen):
    
    # hanya akan mengecek apakah hasilnya true or false
    # jika false maka akan menghasilkan error
    assert type(username)==str,"user name harus string"
    if minlen < 1:
        # raise akan langsung menjalankan error jika dipanggil
        raise ValueError("minlen must be greater than 1")
    if len(username) < minlen:
        raise ValueError("username must be greater than {}".format(minlen))
    return "{} is accept".format(username), True
    
# print(valid_user("asep",2))