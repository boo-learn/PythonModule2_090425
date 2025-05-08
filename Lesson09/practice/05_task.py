# Дан список словарей, где каждый словарь представляет собой информацию о человеке (например, {'name': 'Иван', 'age': 30}).
# Напишите функцию, которая возвращает список имен из этого списка.

def is_name(human):
    return human.get("name", 0)

def list_of_names(humans):
    return list(map(is_name, humans))

# Проверка данных
humans = [
    {"name": 'Nico', "age": 29},
    {"name": 'Alex', "age": 49},
    {"name": 'Leo', "age": 18},
]
print(list_of_names(humans))
