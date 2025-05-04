# Данные о сотрудниках в программе хранятся в словаре
staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 47800
    },
]
# Вычислите:
max_salary = 0
max_salary_employee = {}

for person in staff:
    if person["salary"] > max_salary:
        max_salary = person["salary"]
        max_salary_employee = person

print("Имя и Фамилия сотрудника с самой высокой зарплатой:", max_salary_employee["name"], max_salary_employee["surname"] )

min_salary = staff[0]["salary"]
min_salary_employee = staff[0]

for person in staff:
    if person["salary"] < min_salary:
        min_salary = person["salary"]
        min_salary_employee = person

print("Имя и Фамилия сотрудника с самой низкой зарплатой:", min_salary_employee["name"], min_salary_employee["surname"])

total_salary = 0

for person in staff:
    total_salary += person["salary"]

average_salary = total_salary / len(staff)

print("Среднеарифметическуя зарплату всех сотрудников:", average_salary)

same_surname_count = {}

for person in staff:
    surname = person["surname"]
    if surname in same_surname_count:
        same_surname_count[surname] += 1
    else:
        same_surname_count[surname] = 1

for surname, count in same_surname_count.items():
    if count > 1:
        print(f"Фамилия '{surname}' встречается {count} раза ")

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")

# TODO: your code here
