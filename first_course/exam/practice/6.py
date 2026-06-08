'''
Создайте класс АВТОМОБИЛЬ с методами вывода информации и проверки соответствия условиям.

Реализуйте дочерние классы:

ЛЕГКОВОЙ АВТОМОБИЛЬ (марка, модель, год выпуска, тип кузова)
ГРУЗОВОЙ АВТОМОБИЛЬ (марка, модель, год выпуска, грузоподъемность)
АВТОБУС (марка, модель, год выпуска, количество мест)
'''


class Car:
    def __init__(self, brand: str, model: str, year_create: int):
        self.brand = brand
        self.model = model
        self.year_create = year_create

    def __str__(self):
        return (f"Марка: {self.brand}\n"
                f"Модель: {self.model}\n"
                f"Год выпуска: {self.year_create}")


class LightCar(Car):
    def __init__(self, brand: str, model: str, year_create: int, body_type: str):
        super().__init__(brand, model, year_create)
        self.body_type = body_type

    def __str__(self):
        return super().__str__() + f"\nТип кузова: {self.body_type}"


class HeavyCar(Car):
    def __init__(self, brand: str, model: str, year_create: int, load_capacity: float):
        super().__init__(brand, model, year_create)
        self.load_capacity = load_capacity

    def __str__(self):
        return super().__str__() + f"\nГрузоподъемность: {self.load_capacity} т"


class Bus(Car):
    def __init__(self, brand: str, model: str, year_create: int, seats_count: int):
        super().__init__(brand, model, year_create)
        self.seats_count = seats_count

    def __str__(self):
        return super().__str__() + f"\nКоличество мест: {self.seats_count}"


sedan = LightCar("Toyota", "Camry", 2022, "Седан")
print(sedan)

print("-" * 20)

truck = HeavyCar("КаМАЗ", "65115", 2020, 15.0)
print(truck)
