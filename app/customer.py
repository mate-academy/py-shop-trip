from __future__ import annotations

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, customer_info: dict, car: Car) -> None:
        self.name = customer_info.get("name")
        self.product_list = customer_info.get("product_cart")
        self.location = customer_info.get("location")
        self.home = customer_info.get("location")
        self.money = customer_info.get("money")
        self.car = car
        self.in_shop = None

    def choose_shop_out_of(self, shops: list) -> Shop | None:
        total_trip_costs = [
            round(shop.calculate_total_check(self.product_list)
                  + self.car.get_fuel_cost(self.location, shop.location), 2)
            for shop in shops
        ]

        for i in range(len(total_trip_costs)):
            print(
                f"{self.name}'s trip to the {shops[i].name} "
                f"costs {total_trip_costs[i]}"
            )

        if min(total_trip_costs) <= self.money:
            index = total_trip_costs.index(min(total_trip_costs))
            return shops[index]
        return None

    def drive_to(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}\n")
        self.location = shop.location
        self.in_shop = shop

    def buy_products(self) -> None:
        shop_expenses = self.in_shop.purchase_with_receipt(
            self.name,
            self.product_list
        )
        self.money -= shop_expenses

    def return_home(self) -> None:
        print(f"{self.name} rides home")
        self.money -= self.car.get_fuel_cost(self.location, self.home)
        self.location = self.home

    def check_wallet(self) -> None:
        print(f"{self.name} now has {self.money} dollars\n")
