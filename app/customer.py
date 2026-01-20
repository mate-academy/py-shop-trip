import math

from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int | float,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_cost_trip(
            self,
            shop: Shop,
            fuel_price: float | int
    ) -> float | int:
        distance = math.sqrt((shop.location[0] - self.location[0]) ** 2
                             + (shop.location[1] - self.location[1]) ** 2)
        fuel_cost = (
            distance * fuel_price * self.car["fuel_consumption"] / 100 * 2
        )
        products_cost = sum(
            self.product_cart[product] * shop.products[product]
            for product in self.product_cart)
        cost_trip = fuel_cost + products_cost
        return round(cost_trip, 2)
