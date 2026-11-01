from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list[int],
        car: Car,
        money: float,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.home_location = location.copy()
        self.car = car

    def distance_to(self, shop_location: list[int]) -> float:
        return (
            (shop_location[0] - self.location[0]) ** 2
            + (shop_location[1] - self.location[1]) ** 2
        ) ** 0.5

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.distance_to(shop.location)
        fuel_cost = self.car.price(distance, fuel_price)
        return shop.calculate_cost(self.product_cart) + fuel_cost * 2

    def ride(self, destination: list[int], fuel_price: float) -> None:
        distance = self.distance_to(destination)
        fuel_cost = self.car.price(distance, fuel_price)
        self.money -= fuel_cost
        self.location = destination.copy()
