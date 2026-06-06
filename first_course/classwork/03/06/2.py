class Car:
    def __init__(self, brand, model, production_year, mileage):
        self.brand = brand
        self.model = model
        self.production_year = production_year
        self.mileage = mileage
        self.__fuel_type = "gasoline"

    def __str__(self):
        return (
            f"brand {self.brand} model {self.model} "
            f"production year {self.production_year} vehicle mileage {self.mileage}"
        )

    def needs_service(self):
        if self.mileage > 10000:
            return "service is required"
        return "service is not required "

    @property
    def fuel_type(self):
        return self.__fuel_type

    @fuel_type.setter
    def fuel_type(self, fuel_type):
        self.__fuel_type = fuel_type


car_1 = Car("bmw", "x5m", 2024, 3000)
print(car_1)
print(car_1.needs_service())
print(car_1.fuel_type)
