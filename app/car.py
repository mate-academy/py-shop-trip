from math import dist


class Car:
    def __init__(
            self,
            car: dict
    ) -> None:
        self.brand = car["brand"]
        self.fuel_consumption = car["fuel_consumption"]

    def trip_cost(
            self,
            customer_location: list,
            shop_location: list,
            fuel_price: float
    ) -> float:
        distance = dist(customer_location, shop_location)

        return self.fuel_consumption / 100 * distance * 2 * fuel_price
