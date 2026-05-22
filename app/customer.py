from app.utils import calculate_distance
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: tuple,
                 money: int,
                 car: Car) \
            -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = calculate_distance(self.location, shop.location)

        fuel_cost = self.car.calculate_fuel_cost(distance * 2, fuel_price)

        shopping_cost = shop.calculate_cost(self.product_cart)
        return round(fuel_cost + shopping_cost, 2)
