# Ссылка на блок-схемы:
# https://drive.google.com/file/d/12xTQSyUeeSIWUDkwn3nWW-KHMmj31Rxy/view?usp=sharing

# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

print("Посчитаем сколько раз встречается искомая цифра в последовательности чисел.")

x = int(input("Введите количество чисел в последовательности: "))
y = int(input("Введите искомую цифру: "))

i = 1
j = 0

while i < x+1:
    num = int(input("Введите цифру № {}".format(i)))
    if num == y:
        j += 1
        i += 1
    else:
        i += 1
else:
    print("Искомая цифра встречалась {} раз(а)".format(j))