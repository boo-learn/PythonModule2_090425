# "Генерация простых множителей числа"
# Напишите генераторную функцию, которая принимает целое число n и генерирует его простые множители по одному.
# (Например, для 12 генератор должен выдавать 2, 2, 3
def gen_prime_factors(n):
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            yield divisor
            n //= divisor
        else:
            divisor += 1

for factor in gen_prime_factors(12):
    print(factor)
