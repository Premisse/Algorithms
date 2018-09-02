# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

arr = [random.randint(1, 101) for _ in range(15)]

minimum_one = arr[0]
maximum_one = arr[-1]

for i in arr:
    if i < minimum_one:
        minimum_one = i

    elif i > maximum_one:
        maximum_one = i

min_index = arr.index(minimum_one)
max_index = arr.index(maximum_one)

print('Массив случайных целых чисел: ', arr)
print('Минимальное число - {}, находится в позиции - {}'.format(minimum_one, min_index))
print('Максимальное число - {}, находится в позиции - {}'.format(maximum_one, max_index))

arr[min_index], arr[max_index] = arr[max_index], arr[min_index]

print('Массив после рокировки:       ', arr)

