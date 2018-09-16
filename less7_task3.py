# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найти в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках.

import random

print("Найдем медиану массива")
m = int(input("Введите натуральное число: "))

array = [random.randint(-50, 50) for i in range(2*m + 1)]
newarray = array[:]

mins = []
length = len(array)

for i in range(len(newarray) - 1):
    while len(mins) < (length // 2 + 1):
        minimum = min(newarray)
        x = newarray.index(minimum)
        y = newarray.pop(x)
        mins.append(y)

mediana = mins[-1]
print(f'Список: {array}')
print(f'Медиана: {mediana}')


