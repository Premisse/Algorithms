# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

arr = [random.randint(-50, 50) for _ in range(10)]

print(arr)
num = -50
position = 0

for i in arr:
    if i < 0 and i > num:
        num = i

print('Максимальный отрицательный элемент {}, его позиция: {}'.format(num, arr.index(num)))