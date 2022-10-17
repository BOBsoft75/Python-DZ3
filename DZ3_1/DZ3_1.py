# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
num = int(input('Введите количество элементов списка: '))
numList = []
sum = 0
for i in range(num):
    numList.append(random.randrange(10))
print(f'Список: {numList}')
for i in range(1, len(numList), 2):
    sum = sum + numList[i]
print(f'{numList} -> сумма элементов на нечетных позициях: {sum}')
