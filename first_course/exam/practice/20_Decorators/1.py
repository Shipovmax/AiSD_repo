'''
Напишите декоратор для функции func(), которая выводит данные школьника и его оценку по ИТ в виде таблицы.
Декоратор должен фильтровать только тех, чья оценка выше 4.5.
'''


def filter_high_grades(func):
    def wrapper(students_data):
        filtered_data = [student for student in students_data if student[2] > 4.5]
        func(filtered_data)

    return wrapper


@filter_high_grades
def print_it_grades(students):
    header = f"| {'Имя':<12} | {'Фамилия':<12} | {'Оценка ИТ':<9} |"
    divider = f"|{'-' * 14}|{'-' * 14}|{'-' * 11}|"

    print(header)
    print(divider)

    for name, surname, grade in students:
        print(f"| {name:<12} | {surname:<12} | {grade:<9.2f} |")


school_database = [
    ("Иван", "Петров", 4.8),
    ("Анна", "Сидорова", 4.2),
    ("Алексей", "Смирнов", 4.6),
    ("Елена", "Козлова", 3.9),
    ("Дмитрий", "Иванов", 5.0)
]

print("=== ШКОЛЬНИКИ С ОЦЕНКОЙ ПО ИТ ВЫШЕ 4.5 ===")
print_it_grades(school_database)
