# "Поиск товара в списке словарей"
#
# Создайте список словарей, представляющих несколько товаров (минимум 4 товара).
# Напишите функцию, которая принимает название товара и список словарей в качестве аргументов.
# Функция должна возвращать словарь товара с указанным названием или None, если товар не найден.
# Вызовите функцию для поиска товара и выведите результат.

def find_item_by_name(items: list[dict], name: str) -> dict | None:
    for item in items:
<<<<<<< HEAD
        if item["name"].lower() ==name.lower():
            return item
    return None
items = [
    {"name": "paints", "price": 35, "quantity": 10},
    {"name": "hat", "price": 5, "quantity": 8},
    {"name": "shoes", "price": 8, "quantity": 100},
    {"name": "shirt", "price": 23, "quantity": 16}
]
print(find_item_by_name(items, "paints"))
print(find_item_by_name(items, "socks"))
print(find_item_by_name(items, "shoes"))

=======
        if item["name"].lower() == name.lower():
            return item

    return None

items = [
    {"name": "Брюки", "cost": 35, "quantity": 10},
    {"name": "Кепка", "cost": 5, "quantity": 8},
    {"name": "кеды", "cost": 8, "quantity": 100},
    {"name": "Рубашка", "cost": 12, "quantity": 16},
]

print(find_item_by_name(items, "Брюки"))
print(find_item_by_name(items, "Носки"))
print(find_item_by_name(items, "кепка"))
>>>>>>> 8af6c69ec3c36c1cceefae84eb65ee6b4d851b53
