# Ссылка на блоксхемы:
# https://drive.google.com/file/d/1MxReXi2rVMhkFsbYynmA2gXycnVpdrwP/view?usp=sharing

# Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).

print("Определим среднее число из трех")
a = int(input("Введите певое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if b < a < c or c < a < b:
    print("Среднее число {}".format(a))
elif a < b < c or c < b < a:
    print("Среднее число {}".format(b))
else:
    print("Среднее число {}".format(c))