#!/usr/bin/env python3
# Выведите на экран таблицу умножения для чисел от 1 до 10.
for num in range(1, 11):
    print('***********')
    for i in range(1, 11):
        print(num, 'x', i, '=', num * i)
