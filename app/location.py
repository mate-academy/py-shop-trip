from decimal import Decimal


class Location:
    def __init__(self, x_axis: int, y_axis: int) -> None:
        self.x_axis = x_axis
        self.y_axis = y_axis

    def calculate_distance(
        self,
        to_location: "Location"
    ) -> Decimal:
        return (
            ((self.x_axis - to_location.x_axis) ** 2
             + (self.y_axis - to_location.y_axis) ** 2)
            ** Decimal("0.5")
        )
