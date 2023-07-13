import io
import unittest
from unittest.mock import patch
from random import *

from from_unittest import sravnen1, sravnen2


class TestSravn(unittest.TestCase):

    def test_method(self, nums= None):
        '''Проверяем на совпадение'''
        self.assertEqual(sravnen1(nums), sravnen2(nums), msg="yes")

    def test_collection(self,nums= None):
        '''Проверяем на невхождение'''
        self.assertIsNot(self, sravnen1(nums), sravnen2(nums))

    def test_is_not_none(self,nums= None):
        '''Проверяем на пустоту'''
        self.assertIsNot(self, sravnen1(nums))

    @patch('sys.stdout', new_callable=io.StringIO)  #'''Проверяем отсутствие вывода на печать'''
    def test_warning(self, mosk_stdout, nums=None):
        self.assertFalse(sravnen1(nums))
        self.assertEqual(mosk_stdout.getvalue(), '')


if __name__ == "__main__":
    unittest.main(verbosity=2)
    import  doctest
    doctest.testmod(verbose=True)
