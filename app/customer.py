import math
from app.car import Car


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict[str, int],
        location: tuple[float, float],
        money: float,
        car: dict[str, float],
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    def calculate_trip_cost(self, shop: str, fuel_price: float) -> float:
        distance_to_shop = self.calculate_dist(self.location, shop.location)
        fuel_cost_to_shop = self.car.fuel_cost(distance_to_shop, fuel_price)
        fuel_cost_back = self.car.fuel_cost(distance_to_shop, fuel_price)
        total_fuel_cost = fuel_cost_to_shop + fuel_cost_back
        total_product_cost = self.calculate_product_cost(shop.products)
        return total_fuel_cost + total_product_cost

    def calculate_dist(
        self, loc1: tuple[float, float], loc2: tuple[float, float]
    ) -> float:
        return math.dist(loc1, loc2)

    def calculate_product_cost(self, shop_products: dict[str, float]) -> float:
        return sum(
            shop_products[product] * quantity
            for product, quantity in self.product_cart.items()
            if product in shop_products
        )
