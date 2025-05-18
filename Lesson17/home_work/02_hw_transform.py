# У вас есть список строк.
# Вам нужно получить список длин всех строк, которые имеют длину более 3 символов.

words = ["cat", "dog", "elephant", "mouse", "bird", "ant"]

string_lengths = list(map(len, filter(lambda word: len(word) > 3, words)))

print(string_lengths)
