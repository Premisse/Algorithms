# Ссылка на блок-схемы:
# https://drive.google.com/file/d/12xTQSyUeeSIWUDkwn3nWW-KHMmj31Rxy/view?usp=sharing

# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

print("Сформируем обратное число")
number = input("Введите число: ")

# Можно было решить без циклов так:

# rebum = number[::-1]
# print(rebum)

# Или через два цикла вот так:

number = int(number)
rebmun = []

while number>0:
    rebmun.append(number % 10)
    number //= 10

for num in rebmun:
    print(num, end='')

