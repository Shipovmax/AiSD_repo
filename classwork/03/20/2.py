class Vehicle:
    """Базовый класс для любого транспортного средства."""

    def __init__(
        self, model: str, vin: str, fuel_capacity: float, load_capacity: float
    ):
        """Инициализация характеристик транспорта."""
        self.model = model
        self.vin = vin
        self.fuel_capacity = fuel_capacity
        self.load_capacity = load_capacity

    def info(self):
        """Возвращает общую информацию о транспорте."""
        return f"Транспорт: {self.model} (VIN: {self.vin})"

    def __str__(self) -> str:
        """Возвращает подробное строковое описание."""
        return f"{self.model} (VIN: {self.vin}), топливо: {self.fuel_capacity} л, груз: {self.load_capacity} кг"

    def __eq__(self, other: object) -> bool:
        """Сравнение транспортных средств по их грузоподъёмности."""
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self.load_capacity == other.load_capacity

    def __le__(self, other: object) -> bool:
        """Проверка, что грузоподъёмность текущего объекта не больше другого."""
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self.load_capacity <= other.load_capacity


class Car(Vehicle):
    """Класс для автомобилей."""

    def __init__(
        self,
        model: str,
        vin: str,
        fuel_capacity: float,
        load_capacity: float,
        seats: int,
    ):
        """Инициализация автомобиля с указанием количества мест."""
        super().__init__(model, vin, fuel_capacity, load_capacity)
        self.seats = seats

    def info(self):
        """Информация об автомобиле и местах."""
        return f"Автомобиль: {self.model}, мест: {self.seats}"

    def __str__(self) -> str:
        """Строковое описание автомобиля."""
        return f"{self.model} (VIN: {self.vin}), топливо: {self.fuel_capacity} л, груз: {self.load_capacity} кг, мест: {self.seats}"

    def __add__(self, other: "Car") -> "Car":
        """Объединение автомобиля с другим (как с прицепом)."""
        if not isinstance(other, Car):
            raise TypeError("К автомобилю можно добавить только другой экземпляр Car")

        # Создаем новый объект с той же моделью, но суммированными показателями бака и груза
        return Car(
            self.model,
            self.vin,
            self.fuel_capacity + other.fuel_capacity,
            self.load_capacity + other.load_capacity,
            self.seats,
        )


class Motorcycle(Vehicle):
    """Класс для мотоциклов."""

    def __init__(
        self,
        model: str,
        vin: str,
        fuel_capacity: float,
        load_capacity: float,
        has_sidecar: bool,
    ):
        """Инициализация мотоцикла с указанием наличия коляски."""
        super().__init__(model, vin, fuel_capacity, load_capacity)
        self.has_sidecar = has_sidecar

    def info(self):
        """Информация о мотоцикле и наличии коляски."""
        sidecar_status = "с коляской" if self.has_sidecar else "без коляски"
        return f"Мотоцикл: {self.model}, {sidecar_status}"

    def __str__(self) -> str:
        """Строковое описание мотоцикла."""
        sidecar_status = "с коляской" if self.has_sidecar else "без коляски"
        return f"{self.model} (VIN: {self.vin}), топливо: {self.fuel_capacity} л, груз: {self.load_capacity} кг, {sidecar_status}"

    def __gt__(self, other: "Motorcycle") -> bool:
        """Сравнение мотоциклов по запасу топлива."""
        if not isinstance(other, Motorcycle):
            return NotImplemented
        return self.fuel_capacity > other.fuel_capacity


# --- Тестирование системы согласно сценарию ---
if __name__ == "__main__":
    # 1. Создание объектов
    car1 = Car("Toyota Camry", "VIN123", 50.0, 500.0, 5)
    moto1 = Motorcycle("Honda CBR", "VIN456", 15.0, 150.0, False)

    # 2. Вывод строкового представления
    print(car1)  # Toyota Camry (VIN: VIN123), топливо: 50.0 л, груз: 500.0 кг, мест: 5
    print(
        moto1
    )  # Honda CBR (VIN: VIN456), топливо: 15.0 л, груз: 150.0 кг, без коляски

    # 3. Сравнения
    print(car1 == moto1)  # False
    print(car1 <= moto1)  # False

    # 4. Создание и объединение автомобилей
    car2 = Car("Ford Focus", "VIN789", 45.0, 400.0, 4)
    car3 = car1 + car2
    print(car3)  # Toyota Camry (VIN: VIN123), топливо: 95.0 л, груз: 900.0 кг, мест: 5

    # 5. Сравнение мотоциклов
    moto2 = Motorcycle("Yamaha R1", "VIN999", 20.0, 200.0, True)
    print(moto2 > moto1)  # True
