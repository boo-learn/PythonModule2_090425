# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.
import math

<<<<<<< HEAD
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

xa = int(input("Введите координату х для точки а: "))
ya = int(input("Введите координату y для точки а: "))
xb = int(input("Введите координату х для точки b: "))
yb = int(input("Введите координату y для точки b: "))
xc = int(input("Введите координату х для точки c: "))
yc = int(input("Введите координату y для точки c: "))

ab = distance(xa, ya, xb, yb)
bc = distance(xb, yb, xc, yc)
ac = distance(xa, ya, xc, yc)

min_length = min(ab, bc, ac)
if min_length == ab:
    print(f"Самый короткий отрезок: AB ({ab})")
elif min_length == bc:
    print(f"Самый короткий отрезок: BC ({bc})")
else:
    print(f"Самый короткий отрезок: AC ({ac})")

print("Самый короткий отрезок:", ...)  # Выводим название отрезка, например “АС”.
=======
def distance(xa, ya, xb, yb, xc, yc):
    AB = math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)
    BC = math.sqrt((xb - xc) ** 2 + (yb - yc) ** 2)
    AC = math.sqrt((xa - xc) ** 2 + (ya - yc) ** 2)
    my_dict = {"AB": AB,"BC": BC, "AC": AC}
    min_key = min(my_dict, key = my_dict.get)
    return min_key

print("Самый короткий отрезок:",  distance(2, 4, 2, 9, 5, 7))  # Выводим название отрезка, например “АС”.
>>>>>>> patch-1
