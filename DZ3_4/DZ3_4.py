# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите число в десятичной системе: '))

def decToBin(n):
    if (n > 1):
        decToBin(n//2)
    print(n % 2, end=' ')

print(f'{num} -> ', end=' ')
decToBin(num)
