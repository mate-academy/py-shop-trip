import json
from typing import Dict

from app.customer import Customer
from app.shop import Shop
from app.calculate_functions import (
    calculate_distance,
    calculate_fuel_cost,
    calculate_total_cost,
    calculate_product_cost
)
from app.generate_messages import (
    generate_product_cost_message, generate_return_message
)


class ShopTripCalculator:
    def __init__(self, config_file: str) -> None:
        self.loaded_json = self.load_config(config_file)
        self.fuel_price = self.loaded_json["FUEL_PRICE"]
        self.customers = [
            Customer.create_customer(customer)
            for customer in self.loaded_json["customers"]
        ]
        self.shops = [
            Shop.create_shop(shop) for shop in self.loaded_json["shops"]
        ]

    @staticmethod
    def load_config(config_file: str) -> Dict:
        with open(config_file, "r") as config_json:
            return json.load(config_json)

    def run(self) -> None:
        min_trip_cost = float("inf")
        cheapest_shop = None

        for customer in self.customers:
            trip_cost_for_every_shop = ""

            distances_to_shops = [
                (
                    calculate_distance(
                        customer.location, shop.location
                    ), shop
                ) for shop in self.shops
            ]

            for distance, shop in distances_to_shops:
                products_cost_at_shop = calculate_total_cost(
                    customer.product_cart, shop.products
                )
                fuel_to_shop = calculate_fuel_cost(
                    distance, customer.fuel_consumption, self.fuel_price
                )

                total_trip_cost = round(
                    (fuel_to_shop + products_cost_at_shop), 2
                )

                if total_trip_cost < min_trip_cost:
                    min_trip_cost = total_trip_cost
                    cheapest_shop = shop

                trip_cost_for_every_shop += (
                    f"{customer.name}'s trip to the {shop.name} "
                    f"costs {total_trip_cost}\n"
                )

            item_cost = calculate_product_cost(
                customer.product_cart, cheapest_shop.products
            )
            what_have_bought = generate_product_cost_message(item_cost)
            total_have_bought = calculate_total_cost(
                customer.product_cart, cheapest_shop.products
            )

            money_remainder = round(customer.money - min_trip_cost, 2)
            return_message = generate_return_message(
                customer,
                money_remainder,
                what_have_bought,
                total_have_bought,
                cheapest_shop
            )

            print(
                f"{customer.name} has {customer.money} dollars\n"
                f"{trip_cost_for_every_shop}"
                f"{return_message}"
            )
