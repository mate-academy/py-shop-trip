import math
from app.car import Car


class Shop:
    shop_list = []

    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products
        self.__class__.shop_list.append(self)

    def cost_for_fuel(self, home_location: list, car: Car) -> float:
        distance = math.dist(self.location, home_location)
        result = round((2 * car.fuel_consumption
                        / 100 * distance * car.fuel_price), 2)
        return result

    def products_cost(self, product_cart: dict) -> float:
        result = 0
        for product, count in product_cart.items():
            result += count * self.products[product]
        return result
