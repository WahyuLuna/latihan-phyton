
from testing2 import valid_user
import unittest

class TestRearange(unittest.TestCase):

    def test_basic(self):
        user_name = "asep"
        min = 2
        self.assertEqual(valid_user(user_name,min), True)
     
    def test_len(self):
        user_name = "asep"
        min = 2
        self.assertRaises(ValueError, valid_user,user_name,min)
     

unittest.main()

