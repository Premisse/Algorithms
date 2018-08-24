# Ссылка на блоксхемы:
# https://drive.google.com/file/d/1MxReXi2rVMhkFsbYynmA2gXycnVpdrwP/view?usp=sharing

# Определить, является ли год, который ввел пользователем, високосным или невисокосным.

print("Определим является ли год високосным")
year = int(input("Введите год: "))

if year % 4 != 0:
    print("Год не високосный")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Год високосный")
    else:
        print("Год не високосный")
else:
    print("Год високосый")