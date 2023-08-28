from app.shop import Shop
from app.car import Car


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list,
        money: float | int,
        car: Car,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.lowest_trip_cost = None

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.calculate_distance(shop.location)
        fuel_needed = (distance / 100) * self.car.fuel_consumption
        trip_cost = (2 * fuel_needed * fuel_price) + sum(
            self.product_cart[item] * shop.products.get(item, 0)
            for item in self.product_cart
        )
        return round(trip_cost, 2)

    def calculate_distance(self, destination: list) -> float | int:
        return (
            (destination[0] - self.location[0]) ** 2
            + (destination[1] - self.location[1]) ** 2
        ) ** 0.5
