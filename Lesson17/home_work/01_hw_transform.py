# У вас есть список цен товаров.
# Вам нужно применить скидку в 10% к каждому товару, цена которого превышает 100 единиц, и вывести новые цены.

prices = [50, 120, 80, 150, 90, 200]
is_over_100 = list(filter(lambda n: n > 100, prices))
discount_10per = list(map(lambda n: n * 0.9, is_over_100))
# print(is_over_100)
print(discount_10per)
