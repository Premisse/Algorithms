# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

arr = [[random.randint(1, 50) for _ in range(3)] for _ in range(3)]

for lines in arr:
    print(lines)

line_max = 0

for j in range(3):
    col_min = 50
    for i in range(3):
        if arr[i][j] < col_min:
            col_min = arr[i][j]

    if col_min > line_max:
        line_max = col_min

print('Максимальный элемент среди минимальных элементов столбцов матрицы: {}'.format(line_max))