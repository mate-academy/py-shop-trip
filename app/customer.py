from __future__ import annotations

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            products_want: dict,
            location: list,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.products_want = products_want
        self.location = location
        self.money = money
        self.car = car
        self.home = location

    def calculate_distance_amount(self, shop: Shop) -> float:
        shop_x, shop_y = shop.location
        cust_x, cust_y = self.location
        distance = ((shop_x - cust_x) ** 2 + (shop_y - cust_y) ** 2) ** 0.5
        return distance

    def calculate_all_trip(self, shop: Shop, fuel: float) -> float:
        distance = self.calculate_distance_amount(shop)
        all_trip_fuel_price = (distance * 2 / 100 * self.car.fuel) * fuel

        all_price_in_shop = shop.total_price(self.products_want)

        result = round(all_trip_fuel_price + all_price_in_shop, 2)
        print(f"{self.name}'s trip to the {shop.name} costs {result}")
        return result, shop

    def ride_to_cheapest_shop(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}")
        self.location = shop.location

    def ride_to_home(self) -> None:
        self.location = self.home
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars")

    def __str__(self) -> str:
        return f"Customer(name={self.name}, car={self.car})"

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def make_customers(cls, customers: list) -> list:
        return [
            cls.from_dict(customer)
            for customer in customers
        ]

    @classmethod
    def from_dict(cls, item: dict) -> Customer:
        return cls(
            name=item["name"],
            products_want=item["product_cart"],
            location=item["location"],
            money=item["money"],
            car=Car.from_dict(item=item["car"])
        )
