# Дан готовый код
def is_long_word(word):
    return len(word) > 5


words = ["apple", "banana", "kiwi", "orange", "grape"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(long_words)

# Задача: перепишите код, используя lambda-функцию
long_words = list(filter(lambda word: len(word) > 5, words))
print(long_words)