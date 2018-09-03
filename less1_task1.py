# Ссылка на блоксхемы:
# https://drive.google.com/file/d/1MxReXi2rVMhkFsbYynmA2gXycnVpdrwP/view?usp=sharing

# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

print("Найдем сумму и произведение цифр трехзначного числа")
x = int(input("Введите трехзначное число: "))

a = x % 10
x = x // 10
b = x % 10
c = x // 10

sum = a + b + c
print("Сумма цифр трехначного числа равна: {}".format(sum))

mult = a * b * c
print("Произведение цифр трехзначного числа равно: {}".format(mult))