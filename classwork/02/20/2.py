import math
from dataclasses import dataclass


@dataclass
class Triangle:
    side_a: float
    angle_beta: float
    angle_gamma: float

    def __post_init__(self) -> None:
        """Validate input data after object creation."""
        if self.side_a <= 0:
            raise ValueError("Side length must be a positive number.")
        if self.angle_beta <= 0 or self.angle_gamma <= 0:
            raise ValueError("Angles must be greater than 0 degrees.")
        if self.angle_beta + self.angle_gamma >= 180:
            raise ValueError("The sum of two angles must be less than 180 degrees.")

    @property
    def angle_alpha(self) -> float:
        """Calculate the third angle (opposite side a)."""
        return 180 - (self.angle_beta + self.angle_gamma)

    @property
    def _radians(self) -> tuple[float, float, float]:
        """Internal helper for converting all angles to radians."""
        return (
            math.radians(self.angle_alpha),
            math.radians(self.angle_beta),
            math.radians(self.angle_gamma),
        )

    @property
    def side_b(self) -> float:
        """Calculate side b using the law of sines."""
        rad_a, rad_b, _ = self._radians
        return (self.side_a * math.sin(rad_b)) / math.sin(rad_a)

    @property
    def side_c(self) -> float:
        """Calculate side c using the law of sines."""
        rad_a, _, rad_g = self._radians
        return (self.side_a * math.sin(rad_g)) / math.sin(rad_a)

    @property
    def triangle_type(self) -> str:
        """Determine the triangle type by angles and sides."""
        angles = sorted([self.angle_alpha, self.angle_beta, self.angle_gamma])

        # 1. Classification by angles.
        if any(math.isclose(angle, 90) for angle in angles):
            angle_kind = "right"
        elif any(angle > 90 for angle in angles):
            angle_kind = "obtuse"
        else:
            angle_kind = "acute"

        # 2. Classification by sides (angles).
        if math.isclose(angles[0], angles[2]):
            return "equilateral"  # No further checks are needed if all angles are equal.

        if math.isclose(angles[0], angles[1]) or math.isclose(angles[1], angles[2]):
            side_kind = "isosceles"
        else:
            side_kind = "scalene"

        return f"{angle_kind}, {side_kind}"


# --- Test block ---
try:
    # Example 1: right isosceles triangle.
    triangle = Triangle(side_a=10, angle_beta=45, angle_gamma=45)

    print(f"Figure information: {triangle}")
    print(f"Third angle (alpha): {triangle.angle_alpha}°")
    print(f"Sides: b = {triangle.side_b:.2f}, c = {triangle.side_c:.2f}")
    print(f"Type: {triangle.triangle_type}")

    print("-" * 30)

    # Example 2: error validation check.
    # triangle_error = Triangle(10, 90, 90)

except ValueError as error:
    print(f"Validation error: {error}")
