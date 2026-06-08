'''
Создайте класс ТРАНСПОРТ (информация, грузоподъемность). Дочерние классы: АВТОМОБИЛЬ, МОТОЦИКЛ (без коляски грузоподъемность),
ГРУЗОВИК (с прицепом грузоподъемность). Организуйте поиск по грузоподъемности.
'''


class Transport:
    def __init__(self, brand: str, model: str, capacity: float):
        self.brand = brand
        self.model = model
        self.capacity = capacity

    def __str__(self):
        return f"{self.brand} {self.model} (Грузоподъемность: {self.capacity} кг)"


class Car(Transport):
    def __init__(self, brand: str, model: str, capacity: float, body_type: str):
        super().__init__(brand, model, capacity)
        self.body_type = body_type

    def __str__(self):
        return f"Легковой автомобиль: {super().__str__()}, Кузов: {self.body_type}"


class Motorcycle(Transport):
    def __init__(self, brand: str, model: str, has_sidecar: bool = False):
        capacity = 150.0 if not has_sidecar else 300.0
        super().__init__(brand, model, capacity)
        self.has_sidecar = has_sidecar

    def __str__(self):
        sidecar_str = "с коляской" if self.has_sidecar else "без коляски"
        return f"Мотоцикл ({sidecar_str}): {super().__str__()}"


class Truck(Transport):
    def __init__(self, brand: str, model: str, base_capacity: float, has_trailer: bool = False):
        total_capacity = base_capacity
        if has_trailer:
            total_capacity += base_capacity * 0.7
        super().__init__(brand, model, total_capacity)
        self.has_trailer = has_trailer

    def __str__(self):
        trailer_str = "с прицепом" if self.has_trailer else "без прицепа"
        return f"Грузовик ({trailer_str}): {super().__str__()}"


def search_by_capacity(transport_list: list[Transport], min_capacity: float) -> list[Transport]:
    return [t for t in transport_list if t.capacity >= min_capacity]


fleet = [
    Car("Toyota", "Camry", 450.0, "Седан"),
    Motorcycle("Yamaha", "R1", has_sidecar=False),
    Motorcycle("Урал", "ИМЗ", has_sidecar=True),
    Truck("КаМАЗ", "65115", 15000.0, has_trailer=False),
    Truck("Scania", "R500", 20000.0, has_trailer=True)
]

print("=== ВЕСЬ ТРАНСПОРТ ===")
for vehicle in fleet:
    print(vehicle)

print("\n" + "=" * 50 + "\n")

search_limit = 300.0
print(f"=== ПОИСК ТРАНСПОРТА С ГРУЗОПОДЪЕМНОСТЬЮ ОТ {search_limit} КГ ===")
found_vehicles = search_by_capacity(fleet, search_limit)

for vehicle in found_vehicles:
    print(vehicle)
