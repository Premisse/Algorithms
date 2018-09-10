# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# без перевода в десятичный формат

import collections

# функция дополнит нулями число, если в нем меньше разрядов, чем возможно
def overtake(num):
    while len(num) < 5:
        j = '0'
        num = j + num
    return num

# функция создания списка из введенной строки
def add_to_lst(str):
    num_lst = []
    i = 0
    while i < len(str):
        num_lst.append(str[i])
        i += 1
    return num_lst

# функция заменит буквы на соответствующие числа
def transition(lst):
    new_lst = []
    i = 0
    while i < len(lst):
        for key in lst[:]:
            if key.isalpha():
                if key == 'A' or key == 'a':
                    key = 10
                    new_lst.append(key)
                    i += 1
                elif key == 'B' or key == 'b':
                    key = 11
                    new_lst.append(key)
                    i += 1
                elif key == 'C' or key == 'c':
                    key = 12
                    new_lst.append(key)
                    i += 1
                elif key == 'D' or key == 'd':
                    key = 13
                    new_lst.append(key)
                    i += 1
                elif key == 'E' or key == 'e':
                    key = 14
                    new_lst.append(key)
                    i += 1
                elif key == 'F' or key == 'f':
                    key = 15
                    new_lst.append(key)
                    i += 1
            else:
                new_lst.append(int(key))
                i += 1
        i += 1
    return new_lst

# функция сложения чисел из двух списков
def getSum(lst1, lst2):
    # result = list(map(lambda a, b: int(a) + int(b), lst1[::-1], lst2[::-1]))
    result = []
    count = 0
    for n1, n2 in zip(lst1, lst2):
        i = n1 + n2
        if count == 1:
            i += 1
        if i >= 16:
            while i >= 16:
                i -= 16
            count = 1
        else:
            count = 0
        result.append(i)
    return result [::-1]

# функция умножения чисел двух списков
def add_product(lst1, lst2):
    result = []
    count = 0
    x = 0
    while x < 1:
        for n2 in reversed(lst2):
            middle = []
            for n1 in reversed(lst1):
                i = n1 * n2
                if count > 0:
                    i += count
                if i >= 16:
                    count = 0
                    while i >= 16:
                        i -= 16
                        count += 1
                else:
                    count = 0
                middle.append(i)
            result.insert(x, middle)
        x += 1
    return result

# функция сложения чисел списков списка
def addMultSum(v, w, x, y, z):
    result = []
    count = 0
    for n1, n2, n3, n4, n5 in zip(v[::-1], w[::-1], x[::-1], y[::-1], z[::-1]):
        i = n1 + n2 + n3 + n4 + n5
        if count == 1:
            i += 1
        if i >= 16:
            while i >= 16:
                i -= 16
            count = 1
        else:
            count = 0
        result.append(i)
    return result[::-1]

# доведение до формата
def getFormat(lst):
    result = []
    i = 0
    while i < len(lst):
        for key in lst:
            if key > 9:
                if key == 10:
                    key = 'A'
                    result.append(key)
                    i += 1
                elif key == 11:
                    key = 'B'
                    result.append(key)
                    i += 1
                elif key == 12:
                    key = 'C'
                    result.append(key)
                    i += 1
                elif key == 13:
                    key = 'D'
                    result.append(key)
                    i += 1
                elif key == 14:
                    key = 'E'
                    result.append(key)
                    i += 1
                elif key == 15:
                    key = 'F'
                    result.append(key)
                    i += 1
            else:
                result.append(key)
                i += 1
        i += 1
    return result

print('Произведем сложение и умножение над шестнадцатеричными числами')

num1 = input("Введите число в шестнадцатеричном формате: ")
num2 = input("Введите второе число в шестнадцатеричном формате: ")

num1 = overtake(num1)
num2 = overtake(num2)

num_for_sum1 = add_to_lst(num1)
num_for_sum2 = add_to_lst(num2)

num_for_sum1.reverse()
num_for_sum2.reverse()

num_for_sum1 = transition(num_for_sum1)
num_for_sum2 = transition(num_for_sum2)

result_sum = getSum(num_for_sum1, num_for_sum2)

result_sum = getFormat(result_sum)

print("----------------------------------------------")
print('Сумма:')
for i in result_sum:
    print(i, end="")
print("")
print("----------------------------------------------")

num_for_mult1 = add_to_lst(num1)
num_for_mult2 = add_to_lst(num2)

num_for_mult1 = transition(num_for_mult1)
num_for_mult2 = transition(num_for_mult2)

product_of_16 = add_product(num_for_mult1, num_for_mult2)

for i in product_of_16:
    i.reverse()

product_of_16.reverse()

# конечно тут надо общим циклом, но ...шел четвертый день, извилины выпрямлялись )))
for i in product_of_16[1:]:
    i.append(0)

for i in product_of_16[2:]:
    i.append(0)

for i in product_of_16[3:]:
    i.append(0)

product_of_16[4].append(0)

middle_product = addMultSum(product_of_16[0], product_of_16[1], product_of_16[2], product_of_16[3], product_of_16[4])
total_product = getFormat(middle_product)
print('Произведение:')
for i in total_product:
    print(i, end="")