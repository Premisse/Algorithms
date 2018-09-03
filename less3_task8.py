# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.

print('Введите целые числа: ')
LINE = 5
COL = 4
arr = []

for i in range(COL):
    arr_line = []
    line_sum = 0

    for j in range(LINE-1):
        num = int(input('Введите число для строки {}: '.format(i)))
        line_sum += num
        arr_line.append(num)

    arr_line.append(line_sum)
    arr.append(arr_line)

for lines in arr:
    print(lines)
