# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.

def right_format(number):
    hours = (number % (3600 * 24)) // 3600
    minutes = (number % 3600) // 60
    seconds = number % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"


number = int(input("Введите число в секундах: "))
print("Введенное количество секунд в формате “hh:mm:ss”:", right_format(number))


# Пример:
# 29143 секунд → 08:05:43
