# h15_get_upper_chars_test.py

import h15_get_upper_chars as chars
import unittest

class Test_get_upper_chars(unittest.TestCase):
    def test_get_upper_chars_text_with_uppers(self):
        result = chars.get_upper_chars('LoremIpsum')
        self.assertEqual(result, 'LI')

    def test_get_upper_chars_text_without_uppers(self):
        result = chars.get_upper_chars('loremipsum')
        self.assertFalse(result)

unittest.main()
