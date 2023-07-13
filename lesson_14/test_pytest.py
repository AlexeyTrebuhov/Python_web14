import pytest
from from_doctest import is_sum
from from_unittest import sravnen1
from random import *

#a = random.uniform (99,2222)
a = 99.3333
nums =  [randint(1, 11) for i in range(21)]

def test_sravnenye1():
    '''Сравниваем заданной или рандомное значение'''
    assert is_sum(a) == 30

def test_sravnenye2():
    '''Сравниваем разные типы данных из разных файлов'''
    assert is_sum(a) != sravnen1(nums)

if __name__ == '__main__':
   pytest.main(['-v'])