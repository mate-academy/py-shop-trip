from math import dist
from app.shop import Shop


class Customer:
    def __init__(self, data: dict) -> None:
        self.name: str = data["name"]
        self.cart: dict[str, int] = data["product_cart"]
        self.location: list[float] = data["location"]
        self.home_location: list[float] = list(self.location)
        self.money: float = data["money"]
        self.fuel_consumption: float = data["car"]["fuel_consumption"]

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance_to_shop = dist(self.home_location, shop.location)
        distance_back_home = dist(shop.location, self.home_location)
        total_distance = distance_to_shop + distance_back_home
        fuel_used = (self.fuel_consumption / 100) * total_distance
        return fuel_used * fuel_price

    def can_afford(self, shop: Shop, fuel_price: float) -> bool:
        total_cost = (
            self.calculate_trip_cost(shop, fuel_price)
            + shop.calculate_cart_total(self.cart)
        )
        return self.money >= total_cost

    def go_to_shop(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}")
        self.location = list(shop.location)

    def back_to_home(self) -> None:
        self.location = list(self.home_location)
        print(f"{self.name} rides home")

    def buy_products(self, shop: Shop, fuel_price: float) -> None:
        fuel_cost = self.calculate_trip_cost(shop, fuel_price)
        product_cost = shop.calculate_cart_total(self.cart)
        total_cost = fuel_cost + product_cost
        self.money -= total_cost

        shop.print_receipt(self.name, self.cart)
