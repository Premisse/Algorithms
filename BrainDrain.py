# Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.

from collections import Counter, namedtuple


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return 'Node [' + str(self.data) + ']'


class Tree:
    def __init__(self, cargo, data, left=None, right=None):
        self.cargo = cargo
        self.data = data
        self.left = left
        self.right = right

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def height(self, node):
        if node == None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            if lheight > rheight:
                return (lheight + 1)
            else:
                return (rheight + 1)


# функция позволяет взять ключ как int
def node_keys(dict):
    for key, value in dict.items():
        return key

# функция позволяет взять значение
def node_values(dict):
    for key, value in dict.items():
        return value

# обойдем дерево в поисках кода для каждого символа
def getByteString(arr):
    global byteString

    for i in range(len(arr)):
        if len(arr) > 1:
            byteString += str(i)
        if type(arr[i]) == str:
            for j in range(len(result)):
                if result[j][0] == arr[i]:
                    result[j][1] = byteString
                    byteString = byteString[0:-1]
                    break
        else:
            getByteString(arr[i])
    byteString = byteString[0: -1]


s = 'Aleksey the best!'

print('*'*100)
print(f'Закодируем по Хаффману строку: {s}')
print('*'*100)

count_s = Counter(s)
count_s = sorted(count_s.items(), key=lambda x: x[1])

# преобразуем кортежи в словари для удобства
leafes = []
for i in count_s:
    new_leaf = {}
    new_leaf[i[1]] = i[0]
    leafes.append(new_leaf)

# положим полученные значения в словарь
dictionary = leafes[:]

# подготовим 'словарь' для ключей
result = []
for i in dictionary:
    for k, val in i.items():
        x = []
        x.append(val)
        x.append(k)
        result.append(x)

# построим дерево
count = 0
while count < len(leafes) + 2:
    for i in leafes[:-1:2]:
        node = {}
        j = leafes.index(i) + 1
        j = leafes[j]

        i_key = node_keys(i)
        j_key = node_keys(j)
        node_key = i_key + j_key
        i_value = node_values(i)
        j_value = node_values(j)
        node_value = []
        node_value.append(i_value)
        node_value.append(j_value)
        node[node_key] = node_value

        all_nodes = len(leafes) - 1
        c = 0
        while c < all_nodes + 1:
            x = None
            for y in leafes:
                y_key = node_keys(y)

                if y_key <= node_key and y != leafes[-1]:
                    c += 1
                    continue
                elif y_key > node_key and y == leafes[-1]:
                    x = y_key
                    leafes.insert(leafes.index(y), node)
                    break
                elif y_key == node_key and y == leafes[-1]:
                    leafes.append(node)
                    break
                else:
                    if y == leafes[-1]:
                        leafes.append(node)
                        break
                    else:
                        x = y_key
                        leafes.insert(leafes.index(y), node)
                        break
            left = Node(i)
            right = Node(j)
            tree = Tree(node_key, node_value, left, right)

            leafes.remove(j)
            leafes.remove(i)
            c += 1

    if len(leafes) == 1:
        break

print(f'Получили дерево вида: {tree.data}')
print('*'*100)

print('Словарь по частоте встречаемости символа:')
for i, j in enumerate(result):
    print(f'{j[0]} -- {j[1]}', end=', ')
print()
print('*'*100)

for i in range(len(result)):
    byteString = str(i)
    try:
        getByteString(tree[i])
        res = result
    except IndexError:
        pass

print('Эта фраза в закодированном виде: ')
for i, v in enumerate(res):
    print(v[1], end=' ')

print()
print('*'*100)
print('Код каждого символа: ')
for i, v in enumerate(res):
    print(f'{v[0]} --- {v[1]}', sep='\n')
print('*'*100)

# все равно без try except не вышло, это мне надо еще неделю медитировать над задачкой ))