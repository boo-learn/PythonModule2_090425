# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

lengths = []
longest_name = []

for name in names:
    length = len(name)
    lengths.append(length)

max_length = max(lengths)

for name in names:
    if len(name) == max_length:
        longest_name.append(name)

print(longest_name)
