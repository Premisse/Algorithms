# Ссылка на блоксхемы:
# https://drive.google.com/file/d/1MxReXi2rVMhkFsbYynmA2gXycnVpdrwP/view?usp=sharing

# Пользователь вводит номер буквы в алфавите.
# Определить, какая это буква.

print("Определим букву по ее номеру")

x = int(input("Введите номер буквы "))

letter = ord('a') + x - 1

print("Это буква: {}".format(chr(letter)))