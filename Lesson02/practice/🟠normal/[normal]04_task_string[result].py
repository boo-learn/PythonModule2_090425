# Минимум 6 символов
# Должен содержать спецсимвол "#"
# Должен начинаться с большой буквы

password = input("Enter password: ")

if len(password) >= 6 and password.find("#") and password[0].isupper():


# 1. Минимум 6 символов
    print(len(password))

# 2. Должен содержать спецсимвол "#"
    print(password.find("#"))

# 3. Должен начинаться с большой буквы
    print(password[0].isupper())
else:
    print("incorect")