# Дан словарь и ключ.
# Напишите программу, которая возвращает значение по ключу.
# Если ключ отсутствует, возвращает "Ключ не найден".

my_dict = {"a": 0, "b": 2, "c": 3}
key = input("Enter key: ")
if key in my_dict:
    print(my_dict[key])
else:
    print("key not found")


