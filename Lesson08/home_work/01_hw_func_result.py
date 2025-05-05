# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    ticket_str = str(ticket_number)

    # Проверка, что счастливый номер состоит из ровно 6 цифр для сравнения
    if len(ticket_str) != 6 or not ticket_str.isdigit():
        return False

    # Добавил or not метод .isdigit() чтобы проверить, что строка содержит только цифры

    first_half = ticket_str[:3]  # Индексы 0,1,2
    second_half = ticket_str[3:] # Индексы 3,4,5

    sum_first = sum(int(digit) for digit in first_half)
    sum_second = sum(int(digit) for digit in second_half)

    return sum_first == sum_second


# Тестируем функцию
print(lucky_ticket(123006)) # Ответ True
print(lucky_ticket(12321)) # Ответ False
print(lucky_ticket(436751)) # Ответ True

print(lucky_ticket("НеЦифра12332")) # False
print(lucky_ticket(1254211)) # Ответ False
print(lucky_ticket(111333)) # Ответ False


# /home/nick/development/PythonModule2_090425/Lesson08/home_work/01_hw_func_result.py
# python3 01_hw_func_result.py