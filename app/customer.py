from app.car import Car
from app.shop import Shop
from math import sqrt


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def calculate_distant(self, coords: list[int]) -> float:
        x_dist = self.location[0] - coords[0]
        y_dist = self.location[1] - coords[1]
        return sqrt(pow(x_dist, 2) + pow(y_dist, 2))

    def calculate_ride_price(
            self,
            coords: list[int],
            fuel_cost: float
    ) -> float:
        cost_for_ride = 2 * self.calculate_distant(coords)
        cost_for_ride *= self.car.fuel_consumption / 100 * fuel_cost
        return round(cost_for_ride, 2)

    def calculate_products_price(self, shop: Shop) -> float:
        products_price = 0
        for product, quantity in self.product_cart.items():
            products_price += shop.products[product] * quantity
        return products_price
