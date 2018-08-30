# Ссылка на блок-схемы:
# https://drive.google.com/file/d/12xTQSyUeeSIWUDkwn3nWW-KHMmj31Rxy/view?usp=sharing

# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

print("Посчитаем самое большое по сумме цифр число")

number = int(input("Введите число: "))
max_number = 0
max_sum = 0

while number != 0:
    i = 0
    j = number
    while number > 0:
        i = i + number % 10
        number //= 10
    if i > max_sum:
        max_sum = i
        max_number = j

    number = int(input("Введите число: "))
else:
    print("Максимальное по сумме цифр число - {}, сумма его чисел равна - {}".format(max_number, max_sum))