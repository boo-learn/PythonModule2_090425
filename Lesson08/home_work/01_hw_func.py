# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    str_number = str(ticket_number)
    if len(str_number) != 6:
        return False

    first_numbers = str_number[:3]
    last_numbers = str_number[3:]

    first_sum = sum(int(digit) for digit in first_numbers )
    second_sum = sum(int(digit) for digit in last_numbers)

    return first_sum == second_sum


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
