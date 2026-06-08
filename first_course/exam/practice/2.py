'''
Опишите класс Car, заданный маркой, моделью, годом выпуска и пробегом.

Включите в описание класса методы:
вывода информации о машине на экран,
проверки, нужно ли произвести техническое обслуживание (пробег больше 10 000 км с последнего ТО),
и свойство, позволяющее установить тип топлива (бензин, дизель и т. п.)
'''


class Car:
    def __init__(self, brand: str, model: str, year: int, mileage: int, last_to_mileage: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.last_to_mileage = last_to_mileage
        self._fuel_type = None

    def __str__(self) -> str:
        return (f"Автомобиль: {self.brand} {self.model} ({self.year} г.в.), "
                f"текущий пробег: {self.mileage} км.")

    def needs_maintenance(self) -> bool:
        if self.mileage < self.last_to_mileage:
            print("Ошибка: Текущий пробег не может быть меньше пробега на момент прошлого ТО!")
            return False

        miles_since_to = self.mileage - self.last_to_mileage
        return miles_since_to > 10000

    @property
    def fuel_type(self):
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, fuel: str):
        self._fuel_type = fuel


my_car = Car("Toyota", "Camry", 2021, 55000, 48000)

print(my_car)

if my_car.needs_maintenance():
    print("Срочно на сервис!")
else:
    print("Можно ехать, ТО пока не нужно.")

my_car.mileage = 59000
if my_car.needs_maintenance():
    print("Срочно на сервис!")

my_car.fuel_type = "Дизель"
print(f"Тип топлива: {my_car.fuel_type}")
