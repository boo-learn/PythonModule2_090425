# У вас есть список строк, некоторые из которых содержат email-адреса.
# Вам нужно извлечь все email-адреса и привести их к нижнему регистру.
# email-адреса содержат символ '@'.

log_entries = ["User logged in: john.doe@example.com", "Error occurred", "New user registered: Jane_Smith@Example.ORG",
    "Another log", "Contact us at support@test.co.uk"]

words = [word for data in log_entries for word in data.split()]
# print(words)
emails = list(filter(lambda data: '@' in data, words))
lower_emails = list(map(lambda data: data.lower(), emails))

print(lower_emails)
