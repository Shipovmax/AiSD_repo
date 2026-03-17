class MushroomsCollector:
    def __init__(self):
        # Create a separate list for each specific instance (basket).
        self.mushrooms = []

    def is_poisonous(self, mushroom_name):
        # The issue in the original condition was that a standalone string is always truthy.
        # Membership should be checked against a list or tuple.
        if mushroom_name in ("Fly Agaric", "Toadstool"):
            return True
        return False

    def add_mushroom(self, mushroom_name):
        if not self.is_poisonous(mushroom_name):
            self.mushrooms.append(mushroom_name)
        else:
            print("A poisonous mushroom cannot be added")

    def __str__(self):
        # Join list items with a comma and a space.
        return ", ".join(self.mushrooms)


# Usage example
collector_1 = MushroomsCollector()
collector_1.add_mushroom("Fly Agaric")
collector_1.add_mushroom("Aspen Bolete")
collector_1.add_mushroom("Porcini")
print(collector_1)

collector_2 = MushroomsCollector()
collector_2.add_mushroom("Chanterelle")
print(collector_1)
print(collector_2)
