# !/usr/bin/env python3
# -*- config: utf-8 -*-

# Вариант 10. В кортеже, состоящем из вещественных элементов, вычислить:
# 1) номер минимального по модулю элемента кортежа;
# 2) сумму модулей элементов кортежа, расположенных после первого отрицательного элемента.
# Сжать кортеж, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце списка элементы заполнить нулями.

import sys

if __name__ == '__main__':
    x = tuple(map(float, input().split()))
    a = float(input('Введите a: '))
    b = float(input('Введите b: '))
    if not x:
        print('Заданный список пуст', file=sys.stderr)
        exit(1)
    if a > b:
        print('a не может быть больше b', file=sys.stderr)
        exit(1)

    new_x = tuple(i for i in x if not a <= i <= b)
    z = len(x) - len(new_x)
    arr_z = (0,)
    new_z = arr_z * z
    result = new_x + new_z
    print(new_x)
    print(result)
