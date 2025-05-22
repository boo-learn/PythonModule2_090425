def display_menu():
    """Отображает меню."""
    print("\nМеню:")
    print("1. Показать список товаров.")
    print("2. Добавить товар.")
    print("3. Удалить товар.")
    print("4. Обновить товар.")
    print("5. Найти товар по названию.")
    print("6. Вывести товары с ценой ниже заданной.")
    print("7. Вывести товары с количеством ниже заданного.")
    print("8. Выход. \n")


def show_items(items: list[dict]):
    for i, item in enumerate(items):
        print(f"{i} Название: {item["name"]}, Цена: {item["price"]}, Количество: {item["quantity"]}")


def add_item_to_inventory(items: list[dict]) -> None:
    """Добавляет товар в инвентарь"""
    name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара: "))
    new_item = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    items.append(new_item)


inventory = [
    {"name": "Ноутбук", "price": 1200, "quantity": 10},
    {"name": "Мышь", "price": 25, "quantity": 50},
    {"name": "Клавиатура", "price": 50, "quantity": 30},
]

# Menu
while True:
    display_menu()
    choice = input("Выберите действие: ")

    if choice == "1":
        show_items(inventory)
        input("Press Enter to continue")
    elif choice == "2":
        add_item_to_inventory(inventory)
