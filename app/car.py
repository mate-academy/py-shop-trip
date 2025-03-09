from math import dist


class Car:
    def __init__(
            self,
            car: dict
    ) -> None:
        self.brand = car["brand"]
        self.fuel_consumption = car["fuel_consumption"]

    def _calculate_cost_per_km(
            self,
            fuel_price: int | float
    ) -> int | float:
        return (self.fuel_consumption / 100) * fuel_price

    @staticmethod
    def _calculate_distance(
            customer_location: list,
            shop_location: list
    ) -> int | float:
        return dist(customer_location, shop_location)

    def calculate_fuel_cost(
            self,
            fuel_price: int | float,
            customer_location: list,
            shop_location: list
    ) -> int | float:
        cost_per_km = self._calculate_cost_per_km(fuel_price)
        distance = (
            self._calculate_distance(customer_location, shop_location)
            * 2
        )

        return round(cost_per_km * distance, 2)
