# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
num = int(input('Введите количество элементов списка: '))
numList = []
newList = []
for i in range(num):
    numList.append(random.uniform(0, 10))
    # numList.append(round(((float(random.randrange(0, 10, 1))) + (float(random.randrange(0, 100, 1)))/100), 2))
for i in range(num):
    newList.append((numList[i] - int(numList[i])))
maxElement = max(newList)
minElement = min(newList)
print(f'{numList} => {(maxElement - minElement)}')
