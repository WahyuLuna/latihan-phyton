#data import = data_import
import data_import  #(memanggil seluruh proses di file lain)-->(import [nama file])
#syarat
# gunakan 'as' untuk menyederhanakan nama cth:(import data_import as di) maka data_import = di
#gunaka 'from' untuk mengambil def yg di perlukan sj (form data_diri import diri)
#nama harus bersambung
#jika ingin mengambil data harus menggunakan . (data_import.data_list)
# gunalkan from untuk memanggil file dari folder cth(from folder1,folder2 import data)

data_import.diri()
print(data_import.data_list)



