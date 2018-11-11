# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 0, 3, 4, 5 (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

arr_1 = [8, 3, 15, 6, 4, 2]
arr_2 = []

for i, j in enumerate(arr_1):
    if arr_1[i] % 2 == 0:
        arr_2.append(i)

print(arr_2)