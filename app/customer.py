from __future__ import annotations

from app.car import Car
from app.location import Location
from app.product import Product
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: list[Product],
            location: Location,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.shop_trips = {}

    def go_to_the_shop(self, shops: list[Shop]) -> Shop:
        self.amount_of_money()
        for shop in shops:
            self.get_shop_trip_cost(shop)

        shop = self.drive_to_beneficial_shop()
        return shop

    def drive_home(self) -> None:
        self.money -= (min(self.shop_trips))
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")

    def amount_of_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def drive_to_beneficial_shop(self) -> Shop | None:
        if min(self.shop_trips) > self.money:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            return None

        cheapest_shop = self.shop_trips[min(self.shop_trips)]
        print(f"{self.name} rides to {cheapest_shop.name}\n")
        return cheapest_shop

    def get_shop_trip_cost(self, shop: Shop) -> None:
        distance_price = self.get_distance_price(shop.location)
        products_price = Product.calculate_total_cost(
            self.product_cart, shop.products
        )
        cost_of_trip = round(distance_price + float(products_price), 2)
        print(f"{self.name}'s trip to the {shop.name} costs {cost_of_trip}")
        self.shop_trips[cost_of_trip] = shop

    def get_distance_price(self, shop_location: Location) -> float:
        return (
            self.location.calculate_distance(shop_location) * 2
            * Car.fuel_price * (self.car.fuel_consumption / 100)
        )

    @classmethod
    def get_customer_from_dict(cls, custom: dict) -> Customer:
        return cls(
            custom["name"],
            Product.get_products(product_cart=custom["product_cart"]),
            Location.get_location(*custom["location"]),
            custom["money"],
            Car(**custom["car"])
        )

    def __str__(self) -> str:
        return (
            f"Name: {self.name}\n"
            f"Product cart: {self.product_cart}\n"
            f"Location: {self.location}\n"
            f"Money: {self.money}\n"
            f"Car: {self.car}\n"
        )
