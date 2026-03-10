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
            car_data: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car_data["brand"], car_data["fuel_consumption"])
        self.home_location = location

    def get_distance_to(self, target_location: list[int]) -> float:
        x1, y1 = self.location
        x2, y2 = target_location
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        dist_to_shop = self.get_distance_to(shop.location)
        fuel_to_shop = self.car.get_fuel_cost(dist_to_shop, fuel_price)

        products_cost = shop.get_products_cost(self.product_cart)

        return (fuel_to_shop * 2) + products_cost

    def go_shopping(self, shop: Shop, trip_cost: float) -> None:
        self.location = shop.location
        shop.print_receipt(self.name, self.product_cart)
        self.location = self.home_location
        self.money -= trip_cost
