# Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.

from collections import Counter, OrderedDict


# def make_tree(left, right):
#     return (left, right, append(value(left), value(right)), weight(left)+weight(right))

class MyNode:
    def __init__(self, value, weight, left=None, right=None):
        self.value = value
        self.weight = weight
        self.left = left
        self.right = right

    def newNode(self, weight):
        return node(weight, None, None)

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


s = 'Aleksey the best'

count_s = Counter(s)
print(count_s)

count_s = sorted(count_s.items(), key = lambda x: x[1])
print(count_s)

# тут запуталась, как правильно подсчитать
for i in count_s:
    new_node = []
    new_weight = list(count_s[i][1]) + list(count_s[i + 1][1])
    new_node.append(new_weight)
    new_node.append(count_s[i][0])
    new_node.append(count_s[i + 1][0])
    print(new_node)


# x = MyNode()
#
# x.newNode()


# буду пересдавать эту задачу, 