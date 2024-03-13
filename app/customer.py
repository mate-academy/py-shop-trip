from app.car import Car
from app.shop import Shop
from app.utils import calculate_distance


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: tuple,
            money: float,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance_to_shop = calculate_distance(self.location, shop.location)
        fuel_cost_to_shop = self.car.calculate_fuel_cost(distance_to_shop, fuel_price)
        total_product_cost = sum(shop.products[item] * quantity for item, quantity in self.product_cart.items())
        distance_to_home = calculate_distance(shop.location, self.location)
        fuel_cost_to_home = self.car.calculate_fuel_cost(distance_to_home, fuel_price)
        return fuel_cost_to_shop + total_product_cost + fuel_cost_to_home

    def update_location(self, new_location: tuple) -> None:
        self.location = new_location
