# akan langsung di jalankan saat ada yang memanggil file __init__
# symbol . mewakili package dimana init ini berasal
# file yang memnaggil packagfe sj tidak perlu memanggil file yang telah di import oleh init


from . import matematika # file ini otomatis memanggil file matematika
from . import matematika2 # file ini otomatis memanggil file matematika2
print('ini dari file __init__.py yang berada di dalam file package')
