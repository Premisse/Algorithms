# Ссылка на блок-схемы:
# https://drive.google.com/file/d/12xTQSyUeeSIWUDkwn3nWW-KHMmj31Rxy/view?usp=sharing

# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

for i in range(32, 128):
    print("{} - {}".format(i, chr(i)), end=' ')
    if i % 10 == 0:
        print()
