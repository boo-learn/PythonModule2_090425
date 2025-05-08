# Дан список словарей, где каждый словарь представляет собой информацию о человеке (имя, возраст).
# Напишите функцию, которая возвращает новый список, содержащий только те словари, где возраст человека больше 18.

def is_up_18(human):
    return human.get("age", 0) > 18

def list_up_18(humans):
    return list(filter(is_up_18, humans))

# Проверка данных
humans = [
    {"name": 'Nico', "age": 29},
    {"name": 'Alex', "age": 49},
    {"name": 'Leo', "age": 18},
]
print(list_up_18(humans))
