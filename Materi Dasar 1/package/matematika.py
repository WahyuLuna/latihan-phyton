#file ini di panggil oleh (__init__ 1.43.py) yang berada di luar folder package
# tetapi melalui perantara file (__init__.py) yang berada satu folder dengan file matematika

def tambah(*args):
    hasil=0
    
    for data in args:
        hasil += data
    return hasil

def pangkat(n):
    return lambda angka:angka**n