# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] = > [2, 10]


from random import *
import os
from typing import Any, List
import doctest

os.system("cls")

class Subsequence:
    '''Выбор уникальных элементов последовательности'''

    def sravnen1 (nums:list) -> list[Any]:
        '''Первое решение'''

        nums1 = list(filter(lambda x: nums.count(x) == 1, nums))
        return (nums1)

    def sravnen2 (nums:list) -> list[Any]:
        '''Второе решение'''

        nums2 =  [i for i in nums if nums.count(i) == 1]
        return (nums2)

    if __name__ == '__main__':

        doctest.testmod(verbose=True)
        nums =  [randint(1, 11) for i in range(21)]
        print(sravnen1(nums), sravnen2(nums))


def sravnen1(nums):
    return None


def sravnen2():
    return None