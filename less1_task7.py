# Ссылка на блоксхемы:
# https://drive.google.com/file/d/1MxReXi2rVMhkFsbYynmA2gXycnVpdrwP/view?usp=sharing

# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

print("Определим возможность существования треугольника и его тип")
a = int(input("Введите длину первого отрезка: "))
b = int(input("Введите длину второго отрезка: "))
c = int(input("Введите длину третьего отрезка: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Такой треугольник не существует")
elif a != b and a != c and b != c:
    print("Треугольник разносторонний")
elif a == b == c:
    print("Треугольник равносторонний")
else:
    print("Треугольник равнобедренный")