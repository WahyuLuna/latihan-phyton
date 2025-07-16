
def valid_user(username, minlen):
    
    # hanya akan mengecek apakah hasilnya true or false
    # jika false maka akan menghasilkan error
    assert type(username)==str,"user name harus string"
    if minlen < 1:
        # raise akan langsung menjalankan error jika dipanggil
        return False
    if len(username) < minlen:
        return True
    return True
  