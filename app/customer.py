from math import sqrt


class Customer:
    fuel_price = None

    def __init__(self, customer: dict) -> None:
        self.name: str = customer["name"]
        self.product_cart = customer["product_cart"]
        self.current_location = customer["location"]
        self.home_location = customer["location"]
        self.car_brand = customer["car"]["brand"]
        self.fuel_consumption = customer["car"]["fuel_consumption"]
        self.money = customer["money"]
        self.purchases = None

    def calculate_trip_cost(self, location: list) -> float:
        distance: float = sqrt(
            (location[0] - self.home_location[0]) ** 2
            + (location[1] - self.home_location[1]) ** 2
        )
        fuel_used: float = distance * (self.fuel_consumption / 100)
        return fuel_used * self.fuel_price

    def make_purchases(self, purchases_total_price: float) -> None:
        self.money -= purchases_total_price

    def go_to_shop(self, shop_name: str, shop_location: list) -> None:
        self.current_location = shop_location
        print(f"{self.name} rides to {shop_name}\n")

    def go_home(self) -> None:
        self.current_location = self.home_location
        print(
            f"{self.name} rides home\n"
            f"{self.name} now has {round(self.money, 2)} dollars\n"
        )

    @classmethod
    def set_fuel_price(cls, price: float | int) -> None:
        cls.fuel_price = price
