# "Вычисление площади случайного треугольника"
# Сгенерируйте случайные координаты трех точек на плоскости.
# Используйте модуль math для вычисления длин сторон треугольника.
# Вычислите площадь треугольника, используя формулу Герона.

import random
import math

# Вычисляем расстояние между двумя точками
def distance(x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Вычисление сторон треугольника
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Вычисление площади треугольника по формуле Герона
def heron_square(a, b, c):
    s = (a + b + c) / 2  # полупериметр
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


# Генерация случайных координат
A = (random.uniform(0, 10), random.uniform(0, 10))
B = (random.uniform(0, 10), random.uniform(0, 10))
C = (random.uniform(0, 10), random.uniform(0, 10))

# Извлекаем координаты
xa, ya = random.uniform(0, 10), random.uniform(0, 10)
xb, yb = random.uniform(0, 10), random.uniform(0, 10)
xc, yc = random.uniform(0, 10), random.uniform(0, 10)


# Вычисление сторон треугольника
a = distance(xb, yb, xc, yc)  # BC
b = distance(xa, ya, xc, yc)  # AC
c = distance(xa, ya, xb, yb)  # AB


# Вычисление площади треугольника
square = heron_square(a, b, c)

# Вывод результатов
print(f"Координаты точек: A{A}, B{B}, C{C}")
print(f"Стороны: a={round(a, 2)}, b={round(b, 2)}, c={round(c, 2)}")
print(f"Площадь треугольника: {round(square, 2)}")
