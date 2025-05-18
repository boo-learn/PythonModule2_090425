# У вас есть список цен товаров.
# Вам нужно применить скидку в 10% к каждому товару, цена которого превышает 100 единиц, и вывести новые цены.

prices = [50, 120, 80, 150, 90, 200]

discounted_prices = list(map(lambda price: price * 0.9 if price > 100 else price, prices))

print(discounted_prices)
