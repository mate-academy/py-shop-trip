import math
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict[str, int],
            location: list[int],
            money: float,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def distance_to(self, shop: Shop) -> float:
        x_diff_squared = (self.location[0] - shop.location[0]) ** 2
        y_diff_squared = (self.location[1] - shop.location[1]) ** 2
        result = math.sqrt(x_diff_squared + y_diff_squared)
        return result

    def calculate_total_trip_cost(
            self,
            shop: Shop,
            fuel_price: float
    ) -> float:
        distance = self.distance_to(shop)
        fuel_cost = self.car.calculate_fuel_cost(distance, fuel_price)
        products_cost = shop.calculate_products_cost(self.product_cart)
        total_cost = fuel_cost * 2 + products_cost
        return total_cost
