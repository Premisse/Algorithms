# Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.


# На этот раз полный провал )) Могу только само решето продемонстрировать:

def sieve(n):
    arr = [0] * n
    for i in range(n):
        arr[i] = i
    arr[1] = 0
    num = 2
    while num < n:
        if arr[num] != 0:
            j = num * 2
            while j < n:
                arr[j] = 0
                j = j + num
        num += 1

    sieve = []
    for i in arr:
     if arr[i] != 0:
            sieve.append(arr[i])
    del arr
    return sieve

# print(sieve(20))

# попытка была такова: без рекурсии
# не поняла как создать решето не до числа, а до его индекса

import math

def find(inum):
    arr = []
    for i in range(inum):
        limit = int(math.sqrt(inum))
        while i <= limit:
            if inum % 2 == 0:
                i += 1
                continue
            else:
                arr.append(i)
    return arr

print(find(5))
