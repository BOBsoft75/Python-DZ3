# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
num = int(input('Введите количество элементов списка: '))
numList = []
newList = []
for i in range(num):
    numList.append(random.randrange(10))
for i in range(num):
    if i < len(numList)-i-1:
        newList.append(numList[i] * numList[len(numList)-i-1])
    elif i == len(numList)-i-1:
        newList.append(numList[i] * numList[i])
        break
print(f'{numList} -> {newList}')
