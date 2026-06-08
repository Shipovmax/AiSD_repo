'''
Создайте класс Автомобиль (марка, модель, год выпуска, скорость).
Реализуйте методы изменения скорости, вывод информации и сравнение скорости двух авто через __eq__.
'''


class Car:
    def __init__(self, brand: str, model: str, year: int, speed: float = 0.0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def change_speed(self, value: float):
        self.speed += value
        if self.speed < 0:
            self.speed = 0.0

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.speed == other.speed
        return False

    def __str__(self):
        return (f"Автомобиль: {self.brand} {self.model} ({self.year} г.в.)\n"
                f"Текущая скорость: {self.speed} км/ч\n"
                f"{'-' * 30}")


car1 = Car("BMW", "M5", 2023, 120.0)
car2 = Car("Audi", "RS6", 2024, 100.0)

print(car1)
print(car2)

print(f"Скорости равны? {car1 == car2}\n")

car2.change_speed(20.0)
print("=== ПОСЛЕ ИЗМЕНЕНИЯ СКОРОСТИ AUDI ===")
print(car2)

print(f"Скорости равны? {car1 == car2}")
