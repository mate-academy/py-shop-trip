from math import sqrt


class Car:
    def __init__(self, fuel_consumption: int | float,
                 fuel_price: int | float,
                 shop: dict,
                 customer_location: list) -> None:
        self.fuel_consumption = fuel_consumption
        self.fuel_price = fuel_price
        self.shop = shop
        self.customer_location = customer_location

    def get_fuel_cost(self) -> int | float:
        distance_to_shop = sqrt(
            (self.shop.location[0] - self.customer_location[0]) ** 2
            + (self.shop.location[1] - self.customer_location[1]) ** 2)
        fuel_cost_to_shop = (distance_to_shop * self.fuel_consumption) / 100
        return (fuel_cost_to_shop * self.fuel_price) * 2
