## "Алгоритм Луна"

### Задание

Для шестнадцати значного номера банковской карты, определите корректность ее номера в соответствии с алгоритмом Луна. 

Про Алгоритм Луна можно почитать [тут](https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%9B%D1%83%D0%BD%D0%B0) или [тут](https://skobki.com/yazyk-c-proverka-nomera-kreditki/).

### Формат входных данных

Дано целое положительное шестнадцати значное число - номер банковской карты.

### Формат выходных данных

Вывести "Да", если номер карты является корректным или "Нет".

### Решение задачи

```python
card_number = int(input("Введите номер банковской карты: "))

str_card_number = str(card_number)
every_second = str_card_number[-2::-2]
remaining_numbers = str_card_number[-1::-2]
sum_of_multiplied_by_2 = 0

for number in every_second:
    result = int(number) * 2
    if result > 9:
        sum_of_multiplied_by_2 += sum(int(digit) for digit in str(result))
    else:
        sum_of_multiplied_by_2 += result

sum_of_remaining_numbers = sum(int(number) for number in remaining_numbers)
total = sum_of_multiplied_by_2 + sum_of_remaining_numbers

if total % 10 == 0:
    print("Да")
else:
    print("Нет")
```

---

### Подсказки

<details>
<summary>Подсказка-1</summary>
Для проверки результата можно воспользоваться
<a href="https://ilovecalc.com/calcs/maths/luhn-algorithm/1370/">
этим онлайн калькулятором
</a>
</details>

