#  В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

arr = [random.randint(1, 50) for _ in range(10)]

minimum_one = arr[0]
maximum_one = arr[-1]
sum_nums = 0

for i in arr:
    if i < minimum_one:
        minimum_one = i

    elif i > maximum_one:
        maximum_one = i

min_index = arr.index(minimum_one)
max_index = arr.index(maximum_one)

print('Массив случайных целых чисел: ', arr)
print('Минимальное число - {}, максимальное число - {}'.format(minimum_one, maximum_one))

if min_index > max_index:
    min_index, max_index = max_index, min_index

for i in range(min_index+1, max_index):
    sum_nums += arr[i]

print('Сумма чисел между ними = {}'.format(sum_nums))


