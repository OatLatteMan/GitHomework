# h15_get_upper_chars_test.py

import unittest
import h15_get_upper_chars as h16

class Test_get_upper_chars(unittest.TestCase):
    def get_upper_chars_text_with_uppers(self):
        result = h16.get_upper_chars('LoremIpsum')
        self.assertTrue(result)

    def get_upper_chars_text_without_uppers(self):
        result = h16.get_upper_chars('loremipsum')
        self.assertFalse(result)

unittest.main()
