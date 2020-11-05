#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 1. Ввести кортеж А из 10 элементов, найти наибольший элемент и переставить его с первым
# элементом. Преобразованный массив вывести.

import sys

if __name__ == '__main__':
    A = tuple(map(int, input().split()))
    if len(A) != 10:
        print('Неверный размер кортежа', file=sys.stderr)
        exit(1)

    B = list(A)
    i_max = B.index(max(B))
    B[0], B[i_max] = B[i_max], B[0]
    A = tuple(B)
    print(A)
