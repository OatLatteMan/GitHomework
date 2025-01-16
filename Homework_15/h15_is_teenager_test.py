# 15_is_teenager_test.py

import h15_is_teenager as h15
import unittest

class Test_teenager(unittest.TestCase):
    def test_is_teenager_13(self):
        result = h15.is_teenager(13)
        self.assertTrue(result)

    def test_is_teenager_10(self):
        result = h15.is_teenager(10)
        self.assertFalse(result)

    def test_is_teenager_19(self):
        result = h15.is_teenager(19)
        self.assertFalse(result)

    def test_is_teenager_n1(self):
        result = h15.is_teenager(-1)
        self.assertFalse(result)

    # def test_is_teenager_text(self):
    #     result = h15.is_teenager('nonsense')
    #     self.assertIsInstance(result)

unittest.main()
