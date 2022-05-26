# Реализуйте алгоритм перемешивания списка.

import random
l = list(map(int, input('Enter the list: ').split()))
lenght = len(l)
for i in range(lenght - 1, 0, -1):
    j = random.randint(0, i)
    l[i], l[j] = l[j], l[i]
print(l)