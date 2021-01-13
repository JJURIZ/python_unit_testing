import unittest
import string_manipulation

class TestCaps(unittest.TestCase):
    
    def test_all_caps(self):
        self.assertEqual(string_manipulation.all_caps("this is lower case"), "THIS IS LOWER CASE")
        self.assertEqual(string_manipulation.all_caps("HELLO SIR"), "HELLO SIR")
        self.assertEqual(string_manipulation.all_caps("I aM uP aNd DoWn"), "I AM UP AND DOWN")

    def test_all_lower(self):
        self.assertEqual(string_manipulation.all_lower("this is lower case"), "this is lower case")
        self.assertEqual(string_manipulation.all_lower("HELLO SIR"), "hello sir")
        self.assertEqual(string_manipulation.all_lower("I aM uP aNd DoWn"), "i am up and down")

if __name__ == '__main__':  
    unittest.main()