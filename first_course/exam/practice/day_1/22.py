'''
Создайте класс Лифт (текущая грузоподъемность).
Реализуйте метод сравнения с максимальной грузоподъемностью и рекомендации по переполнению.
'''


class Lift:
    def __init__(self, max_capacity: float, current_load: float = 0.0):
        self.max_capacity = max_capacity
        self.current_load = current_load

    def check_load(self) -> str:
        if self.current_load < 0:
            return "Ошибка: Вес груза не может быть отрицательным!"

        if self.current_load <= self.max_capacity:
            return f"Запас по весу: {self.max_capacity - self.current_load} кг. Можно ехать."
        else:
            overweight = self.current_load - self.max_capacity
            return f"Перегруз! Вес превышен на {overweight} кг. Пожалуйста, выйдите из лифта."

    def __str__(self):
        return (f"Лифт (Макс. грузоподъемность: {self.max_capacity} кг)\n"
                f"Текущая нагрузка: {self.current_load} кг\n"
                f"{'-' * 40}")


lift = Lift(max_capacity=400.0)

lift.current_load = 250.0
print(lift)
print(lift.check_load())
print(f"{'-' * 40}\n")

lift.current_load = 450.0
print(lift)
print(lift.check_load())
