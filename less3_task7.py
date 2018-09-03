# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

arr = [random.randint(1, 50) for _ in range(15)]

print(arr)

min_1 = arr[0]
min_2 = arr[0]

for i in arr:
    if i < min_1:
        min_1 = i

if arr.count(min_1) == 1:
    for i in arr:
      if i < min_2 and i != min_1:
           min_2 = i
else:
    min_2 = min_1

print('Самый маленький элемент массива: {}. Следующий самый маленький элемент: {}'.format(min_1, min_2))