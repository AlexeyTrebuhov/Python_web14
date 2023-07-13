# 1.	Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# 2.	Напишите к ним тесты. 2-5 тестов на задачу в трёх вариантах:
#   	doctest,
#   	unittest,
#   	pytest.

import os
os.system('cls')
import random

def is_sum( a: float) -> float:
    '''Посчитать сумму цифр вещественного числа'''

    print('Вещественное число = ',a)

    b1 = str(float(a)).split('.')
    b = b1[0]+b1[1]
    sumsss = sum(int(i) for i in str(b))
    return sumsss

if __name__ == '__main__':

    a = random.uniform (99,2222)
    print('Сумма чисел =',is_sum(a))
