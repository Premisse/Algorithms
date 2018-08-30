# Ссылка на блок-схемы:
# https://drive.google.com/file/d/12xTQSyUeeSIWUDkwn3nWW-KHMmj31Rxy/view?usp=sharing

# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше загаданного введенное пользователем число.
# Если за 10 попыток число не отгадано, то вывести его.

import random
print("Отгадайте целое число от 1 до 100")

chance = 0

secret_number = random.randint(1, 101)

while chance < 10:
    number = int(input("Введите число: "))
    if number == secret_number:
        print("Верно!")
        break
    else:
        print("Неверно! Попробуйте еще раз")
    chance += 1
else:
    print("У вас закончились попытки. Случайное число было {}".format(secret_number))