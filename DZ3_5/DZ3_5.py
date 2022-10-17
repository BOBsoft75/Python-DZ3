# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Введите число k: '))

def fibonacci(n):
    fib_num = []
    a, b = 1, 1
    for i in range(num):
        fib_num.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(num+1):
        if a > 0:
            fib_num.insert(0, a * -1)
        else:
            fib_num.insert(0, a)
        a, b = b, a - b
    return fib_num

fib_num = fibonacci(num)
print(f'k = {num}: {fibonacci(num)}')
