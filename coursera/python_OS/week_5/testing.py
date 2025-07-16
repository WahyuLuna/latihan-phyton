"""
Testing adalah metode untuk mengetes sebuah bagian dalam codingan secara otomatis

dengan cara memanggil suatu bagian dari codingan untuk dilakukan pengetesan

cara umunya dengan memanggil bagian tersebut kedalam script khusus untuk melakukan testing




"""
# kita mengambil bagian codingan dari file xample.py
#dan mengambil function range name untuk di test
from xample import range_name
from xample import LetterCompiler

import unittest

class TestRearange(unittest.TestCase):
 
    # untuk test pertama diperkirakan akan berhasil
    #maka tidak perlu melakukan perbaikna pada script induk
    def test_basic(self):
        testcase = "Lovelace, ada"
        expected = "ada Lovelace"
        self.assertEqual(range_name(testcase), expected)
        
    # perbaikan 1    
    #untuk test kedua diperkirakan ada error
    #maka akan dilakukan perbaikan pada script induk
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(range_name(testcase), expected)
      
    
    # untuk test pertama diperkirakan akan berhasil
    #maka tidak perlu melakukan perbaikna pada script induk
    def test_basic2(self):
        testcase = "asep, kurniawan h."
        expected = "kurniawan h. asep"
        self.assertEqual(range_name(testcase), expected)
    
    #perbaikan 2
    #untuk test kedua diperkirakan ada error
    #maka akan dilakukan perbaikan pada script induk
    def test_one_name(self):
        testcase = "bagas"
        expected = "bagas"
        self.assertEqual(range_name(testcase), expected)
      
    # pemanggilan function lain dalam script yang sama  
    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)
        
    
#unittest.main(argv = ['first-arg-is-ignored'], exit = False)        
        
unittest.main()

