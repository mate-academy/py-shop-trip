from __future__ import annotations
from typing import List


from app.classes.class_point import Point
from app.classes.class_shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            home_location: Point | List[int, int],
            money: int | float,
            car_fuel_consumption: float | int,
            product_cart: dict
    ) -> None:
        self.name = name
        self.money = money
        self.car_fuel_consumption = car_fuel_consumption / 100
        self.product_cart = product_cart
        self.current_location = home_location
        if isinstance(home_location, list):
            self.current_location = Point.create_point(home_location)
        self.home_location = self.current_location

    def shopping(self, shop: Shop, fuel_prise: int | float) -> int | float:
        count = 0
        the_cost_of_trip = (self.current_location.get_distance(shop.location)
                            * self.car_fuel_consumption
                            * fuel_prise)
        for product, price in self.product_cart.items():
            count += price * shop.products_prices[product]
        count += the_cost_of_trip * 2
        return round(count, 2)

    def change_location(
            self,
            new_location: Point | List[int, int]
    ) -> None:
        self.current_location = new_location

    def shopping_details(self, shop: Shop) -> None:
        self.change_location(shop.location)
        count = 0
        print("You have bought:")
        for product, price in self.product_cart.items():
            total_price = price * shop.products_prices[product]
            if total_price % 1 == 0:
                total_price = int(total_price)
            count += total_price
            print(
                f"{self.product_cart[product]} {product}s "
                f"for {total_price} dollars"
            )
        print(f"Total cost is {count} dollars\n"
              f"See you again!\n")
        self.change_location(self.home_location)

    def balance_of_money(
            self,
            shop: Shop,
            fuel_price: int | float
    ) -> int | float:
        return round(self.money - self.shopping(shop, fuel_price), 2)

    def __repr__(self) -> str:
        return (f"Shop name: {self.name}\n"
                f"Location: {self.current_location}\n"
                f"Customer has {self.money}$\n"
                f"Car eat {self.car_fuel_consumption}L fuel per 100 km\n"
                f"Customer want to buy {self.product_cart}\n")

    @classmethod
    def crate_customer(cls, dict_data: dict) -> Customer:
        return cls(
            name=dict_data["name"],
            home_location=dict_data["location"],
            money=dict_data["money"],
            car_fuel_consumption=dict_data["car"]["fuel_consumption"],
            product_cart=dict_data["product_cart"]
        )
