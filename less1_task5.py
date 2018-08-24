# Ссылка на блоксхемы:
# https://drive.google.com/file/d/1MxReXi2rVMhkFsbYynmA2gXycnVpdrwP/view?usp=sharing

# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

print("Введите две буквы латинского алфавита")
x = ord(input("Первая буква: "))
y = ord(input("Вторая буква: "))

px = x - ord('a') + 1
py = y - ord('a') + 1

print("Позиции этих букв: {} и {}".format(px, py))

l = abs(px - py)

print("Между ними {} букв(ы)".format(l))