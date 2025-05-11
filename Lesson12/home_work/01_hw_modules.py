# "Вычисление площади случайного треугольника"
# Сгенерируйте случайные координаты трех точек на плоскости.
# Используйте модуль math для вычисления длин сторон треугольника.
# Вычислите площадь треугольника, используя формулу Герона.
import math
import random

def points_distance(x1, y1, x2, y2):
    return math.dist([x1, y1], [x2, y2])

def triangle_area(a,b,c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

xa = random.randint(-20, 20)
ya = random.randint(-20, 20)
xb = random.randint(-20, 20)
yb = random.randint(-20, 20)
xc = random.randint(-20, 20)
yc = random.randint(-20, 20)

ab = points_distance(xa, ya, xb, yb)
bc = points_distance(xb, yb, xc, yc)
ac = points_distance(xa, ya, xc, yc)

area = triangle_area(ab, bc, ac)
print(f"Площадь треугольника: {area}")
