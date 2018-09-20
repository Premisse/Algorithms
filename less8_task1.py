# Определение количества различных подстрок с использованием хеш-функции. Пусть дана строка S длиной N.
# Например, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
# Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или встроенную функцию hash()

import hashlib


# функция определелит по хэшу уникальные подстроки и добавит их в словарь в формате - подстрока: hash
def count_hash(array_of_subs):
    result = {}

    for i in array_of_subs:
        i_hash = hashlib.sha1(i.encode('utf-8')).hexdigest()
        if i_hash in result:
            continue
        else:
            result[i] = i_hash

    return result

S = input('Введите строку: ')
N = len(S)

i, j = 0, 1
result = []

while i < N:
    j = i + 1
    while j < N + 1:
        substr = S[i:j]
        result.append(substr)
        j += 1
    i += 1

result.remove(S)

subs = count_hash(result)

print(count_hash(result))
print(f'Уникальных подстрок в строке {S} - {len(subs)}')