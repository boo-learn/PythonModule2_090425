# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def circles(x1, y1, r1, x2, y2, r2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if r1 >= r2:
        return distance + r2 <= r1
    else:
        return distance + r1 <= r2

print(circles(0, 0, 5, 3, 0, 2))
