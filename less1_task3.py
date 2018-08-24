# Ссылка на блоксхемы:
# https://drive.google.com/file/d/1MxReXi2rVMhkFsbYynmA2gXycnVpdrwP/view?usp=sharing

# По введенным пользователем координатам двух точек вывести уравнение прямой, проходящей через эти точки.

print("Выведем уравнение прямой, проходящей через заданные точки")
print("Введите координаты первой точки: ")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))

print("Введите координаты второй точки: ")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

k = (y1 - y2) / (x1 - x2)
b = y2 - k*x2

print("Уравнение прямой, проходящей через эти точки: y = {} * x + {}".format(k, b))