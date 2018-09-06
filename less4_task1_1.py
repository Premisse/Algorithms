# Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков.

import timeit
import cProfile

# Анализ алгоритма поиска суммы элементов между минимальным и максимальным элементами, не включая сами элементы из задачи 6 урока 3
import random

def find_summ(array):
    minimum_one = array[0]
    maximum_one = array[-1]
    max_min_nums = 'Минимальное число - {}, максимальное число - {}'.format(minimum_one, maximum_one)
    sum_nums = 0

    for i in array:
        if i < minimum_one:
            minimum_one = i
        elif i > maximum_one:
            maximum_one = i
    min_index = array.index(minimum_one)
    max_index = array.index(maximum_one)
    print('Массив случайных целых чисел: ', array)
    print(max_min_nums)
    if min_index > max_index:
        min_index, max_index = max_index, min_index
    for i in range(min_index + 1, max_index):
        sum_nums += array[i]
    return 'Сумма чисел между ними = {}'.format(sum_nums)

arr = [random.randint(1, 500) for _ in range(150)]
# print(find_summ(arr))

# через cProfile

cProfile.run('find_summ(arr)')

# 1    0.005    0.005    0.020    0.020 less4_task1_1.py:10(find_summ)  --- диапазон 5000000 для списка из 15000
# 1    0.028    0.028    0.114    0.114 less4_task1_1.py:10(find_summ)  --- диапазон 500000000 для списка из 150000
# 1    0.133    0.133    0.566    0.566 less4_task1_1.py:10(find_summ)  --- диапазон 50000000000 для списка из 1500000

# через timeit

# Из-за сложностей с получением массива в качестве аргумента функции (выдает сплошные ошибки), для проверки через timeit
# была взята другая функция, без массивов на входе, см. файл less4_task1_timeit.py
