# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random


def merge_sort(arr):
    length = len(arr)

    if length < 2:
        return arr

    left = merge_sort(arr[len(arr) // 2:])
    right = merge_sort(arr[:len(arr) // 2])

    i, j = 0, 0
    result = []

    while i < len(left) or j < len(right):
        if not i < len(left):
            result.append(right[j])
            j += 1
        elif not j < len(right):
            result.append(left[i])
            i += 1
        elif left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result


array = [random.randint(0, 50) for i in range(20)]

print(array)
print(merge_sort(array))




