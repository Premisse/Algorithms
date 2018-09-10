# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

import collections

print("Определим среднюю прибыль предприятий за год, а так же самое сильное и самое слабое звено")
count = int(input("Сколько предприятий будем учитывать: "))

companies = []
total = 0
middle = 0
i = 0
while i < count:

    param = ['name', 'profit_1', 'profit_2', 'profit_3', 'profit_4', 'total_profit']
    Data = collections.namedtuple('Company', param)

    name = input("Введите наименование {} предприятия: ".format(i + 1))
    profit_1 = float(input("Введите прибыль за 1 квартал: "))
    profit_2 = float(input("Введите прибыль за 2 квартал: "))
    profit_3 = float(input("Введите прибыль за 3 квартал: "))
    profit_4 = float(input("Введите прибыль за 4 квартал: "))

    total_profit = profit_1 + profit_2 + profit_3 + profit_4
    total = total_profit + total
    Company = Data(name, profit_1, profit_2, profit_3, profit_4, total_profit)
    comp = Company._asdict()
    companies.append(comp)
    i += 1

middle = total / count

winners = []
loosers = []
j = 0
while j < count:
    if companies[j]['total_profit'] >= middle:
        winners.append(companies[j]['name'])
    else:
        loosers.append(companies[j]['name'])
    j += 1
print(f'Средняя прибыль за год составила {middle}')
print("Прибыль выше среднего у предприятий: ")
for line in winners:
    print(line)

print("Прибыль ниже среднего у предприятий: ")
for line in loosers:
    print(line)