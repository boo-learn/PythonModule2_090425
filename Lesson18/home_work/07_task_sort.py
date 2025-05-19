# Призеры олимпиады
# По результатам олимпиады участники награждаются дипломами.
# Набравшие одинаковые  баллы  получают дипломы  одинаковой степени.
# Призером олимпиады считается участник, получивший диплом  не хуже III степени.
# По результатам олимпиады определите количество призеров.
# Вход: натуральное число участников(N < 100) и далее N натуральных# чисел – результаты участников.
# Выход: одно число – число призеров.
# Пример:
# Вход
#
# 10 1 3 4 3 5 6 7 7 6 1
# Выход
# 5

# import random
# number_of_participants = int(input("Введите число участников: "))
# numbers = [random.randint(1, 100) for _ in range(number_of_participants)]
# print(numbers)
numbers = [10, 1, 3, 4, 3, 5, 6, 7, 7, 6, 1]
sorted_results = sorted(numbers, reverse=True)
print(sorted_results)

prize_winners = []
prize_winners.append(sorted_results[0])

for el in sorted_results:
    if el not in prize_winners:
        prize_winners.append(el)
    if len(prize_winners) == 3:
        break

print("Призовые баллы:", prize_winners)

count_prize_winners = 0
for el in sorted_results:
    if el in prize_winners:
        count_prize_winners += 1

print("Количество призёров:", count_prize_winners)
