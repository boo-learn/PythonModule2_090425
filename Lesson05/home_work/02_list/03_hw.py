# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random
n = int(input("Введите количество элементов: "))
numbers = []
numbers_sum = 0

for num in range(n):
    random_number = random.randint(-100, 100)
    numbers.append(random_number)
print(numbers)

for i in numbers:
    if i > 0 and i % 2 == 0:
        numbers_sum += i
print(numbers_sum)
