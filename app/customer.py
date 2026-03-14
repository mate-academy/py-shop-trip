import math
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict[str, int],
            location: list[int],
            money: int | float,
            car: Car
    ) -> None:

        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def total_cost_calculation(
            self,
            fuel_price: float,
            shop: Shop
    ) -> float | int:

        amount = math.sqrt(
            (shop.location[0] - self.location[0])**2
            + (shop.location[1] - self.location[1])**2
        )

        distance = (self.car.fuel_calculation(amount, fuel_price)) * 2
        return shop.cart_cost_calculation(self.product_cart) + distance
