from app.mixins.navigator_mixin import NavigatorMixin


class Car(NavigatorMixin):
    def __init__(
            self,
            brand: str,
            fuel_consumption: float
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_fuel_cost(
            self,
            start_point: list[int],
            end_point: list[int],
            fuel_price: float
    ) -> float:
        distance = self.calculate_distance(start_point, end_point)
        return self.fuel_consumption / 100 * distance * fuel_price
