# Телефонная база
# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67

phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]


phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]
list_of_numbers = [phone.replace("-", "") for phone in phones]
# print(list_of_numbers)
# sorted_list = sorted(list_of_numbers)
# print(sorted_list)

i = 0
while i < len(list_of_numbers) - 1:
    m = i
    j = i + 1
    while j < len(list_of_numbers):
        if list_of_numbers[j] < list_of_numbers[m]:
            m = j
        j += 1
    list_of_numbers[i], list_of_numbers[m] = list_of_numbers[m], list_of_numbers[i]
    i += 1

print(list_of_numbers)
