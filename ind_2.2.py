#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 10. В кортеже, состоящем из вещественных элементов, вычислить:
# 1) номер минимального по модулю элемента кортежа;
# 2) сумму модулей элементов кортежа, расположенных после первого отрицательного элемента.
# Сжать кортеж, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце списка элементы заполнить нулями.

import sys

if __name__ == '__main__':
    A = tuple(map(float, input().split()))
    if not A:
        print('Заданный кортеж пуст', file=sys.stderr)
        exit(1)

    for i, j in enumerate(a):
        if j < 0:
            a_den = i
            break

    new_a = A[a_den + 1:]
    b = (abs(i) for i in new_a)
    s = sum(b)
    print(s)
