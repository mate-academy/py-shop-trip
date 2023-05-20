from __future__ import annotations
from dataclasses import dataclass
from typing import List
import datetime
from app.json_reader import read_file
from app.car import Car
from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: List[int]
    products: dict

    def __hash__(self) -> int:
        return hash(self.name)

    @staticmethod
    def create_shops() -> list[Shop]:
        return [
            Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )
            for shop in read_file()[0]["shops"]
        ]

    def calculate_shop_trip(self, customer: Customer) -> dict:
        total_cost = sum(
            [
                round(
                    (
                        customer.product_cart[product] * self.products[product]
                    ), 2
                )
                for product in customer.product_cart
            ]
        )
        fuel_cost = Car.calculate_fuel_cost(
            customer.location,
            self.location,
            read_file()[1],
            customer.car["fuel_consumption"]
        )
        total_cost_per_shop = {self: round(total_cost + fuel_cost, 2)}
        return total_cost_per_shop

    @staticmethod
    def find_cheapest_shop(shops: list[Shop], customer: Customer) -> Shop:
        total_cost_per_shop_all_shops = {}
        for shop in shops:
            total_cost_per_shop_all_shops.update(
                Shop.calculate_shop_trip(shop, customer)
            )
        for shop in shops:
            shop_trip_cost = Shop.calculate_shop_trip(shop, customer)
            if shop_trip_cost[shop] == min(
                    total_cost_per_shop_all_shops.values()
            ):
                return shop

    @staticmethod
    def calculate_all_shop_trips(shops: list[Shop], customer: Customer):
        all_shop_trips = []
        for shop in shops:
            shop_trip_cost = Shop.calculate_shop_trip(shop, customer)
            all_shop_trips.append(shop_trip_cost[shop])
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {shop_trip_cost[shop]}")
        return min(all_shop_trips)

    def generate_receipt(self, customer: Customer) -> None:
        total_cost = 0
        print(
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought: "
        )
        for item in customer.product_cart:
            if customer.product_cart[item] == 1:
                print(
                    f"{customer.product_cart[item]} {item} for "
                    f"{customer.product_cart[item] * self.products[item]} "
                    f"dollars"
                )
            else:
                print(
                    f"{customer.product_cart[item]} {item}s for "
                    f"{customer.product_cart[item] * self.products[item]} "
                    f"dollars"
                )
            total_cost += customer.product_cart[item] * self.products[item]
        print(f"Total cost is {total_cost} dollars\n"
              f"See you again!\n")
