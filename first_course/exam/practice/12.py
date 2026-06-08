'''
Создайте класс Задача (название, описание, статус).
Реализуйте метод изменения статуса и вывод информации через __str__.
'''


class Task:
    def __init__(self, name: str, about: str, status: str):
        self.name = name
        self.about = about
        self.status = status

    def __str__(self):
        return f"Задача: {self.name}\nОписание: {self.about}\nСтатус: {self.status}\n{'-' * 30}"

    def change_status(self, value: str):
        self.status = value


print("================================")
task1 = Task("Написать код", "Реализовать классы для учета задач", "В процессе")
print(task1)

task1.change_status("Завершено")
print("=== ПОСЛЕ ИЗМЕНЕНИЯ СТАТУСА ===")
print(task1)
