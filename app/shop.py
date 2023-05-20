from dataclasses import dataclass
from typing import List, Any
import datetime
from app.json_reader import data, fuel_price
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
    def create_shops() -> list:
        return [
            Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )
            for shop in data["shops"]
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
            fuel_price,
            customer.car["fuel_consumption"]
        )
        total_cost_per_shop = {self: round(total_cost + fuel_cost, 2)}
        return total_cost_per_shop

    @staticmethod
    def find_cheapest_shop(shops: list, customer: Customer) -> Any:
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
