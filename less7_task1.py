# Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
# Вывести на экран исходный и отсортированный массивы.

import random

print("Отсортируем по убыванию одномерный целочисленный массив из 20 чисел в диапазоне от -100 до 100: ")

array = [random.randint(-100, 100) for i in range(20)]

print(array)

def bubbleSort(arr):
    n = 1
    while n < len(arr):
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        for j, k in reversed(list(enumerate(arr))):
            if arr[j] != arr[0]:
                if k > arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
        n += 1

    return arr

result_array = bubbleSort(array)

print(f'Отсортированный массив: \n{result_array}')
