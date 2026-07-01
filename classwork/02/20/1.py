import math
from dataclasses import dataclass


@dataclass
class Cone:
    radius: float
    height: float

    def __post_init__(self):
        """Validate object data after initialization."""
        if self.radius <= 0 or self.height <= 0:
            raise ValueError("Radius and height must be greater than zero.")

    @property
    def slant_height(self) -> float:
        """Cone slant height (l)."""
        return math.hypot(self.radius, self.height)

    @property
    def area(self) -> float:
        """Total surface area."""
        return math.pi * self.radius * (self.radius + self.slant_height)

    @property
    def volume(self) -> float:
        """Cone volume."""
        return (1 / 3) * math.pi * (self.radius**2) * self.height


try:
    cone = Cone(5, 12)
    print(cone)
    print(f"Area: {cone.area:.2f}")
    print(f"Volume: {cone.volume:.2f}")
    print(f"Slant height: {cone.slant_height:.2f}")

except ValueError as error:
    print(f"Error: {error}")
