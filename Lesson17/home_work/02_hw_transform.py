# У вас есть список строк.
# Вам нужно получить список длин всех строк, которые имеют длину более 3 символов.

words = ["cat", "dog", "elephant", "mouse", "bird", "ant"]
over_3_char = list(filter(lambda words: len(words) > 3, words))
print(over_3_char)
