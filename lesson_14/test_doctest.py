import os
os.system('cls')
import random


def is_sum( a: float) -> bool:
    '''
    Расчет суммы чисел вещественного числа.
    >>> is_sum(3.4)
    7
    >>> is_sum(3.456)
    18
    >>> is_sum(3.4566543)
    36
    '''

    b1 = str(float(a)).split('.')
    b = b1[0]+b1[1]
    sumsss = sum(int(i) for i in str(b))
    return sumsss

#help(is_sum)

if __name__ == '__main__':

    import  doctest
    doctest.testmod(verbose=True)
    a = random.uniform (111,2)
    print(is_sum(a))