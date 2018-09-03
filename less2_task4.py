# Ссылка на блок-схемы:
# https://drive.google.com/file/d/12xTQSyUeeSIWUDkwn3nWW-KHMmj31Rxy/view?usp=sharing

# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

print("Найдем сумму некоторого количества элементов ряда чисел")
n = int(input("Введите количество элементов: "))

x = 1
y = 0

for i in range(n):
    y = x + y
    x = x / -2
print("Сумма {}".format(y))