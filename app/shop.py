from __future__ import annotations
from unittest.mock import patch
import datetime
from app.additional_functions import calculate_distance, calculate_product_cost
from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    @classmethod
    def from_config(cls, config_data: dict) -> Shop:
        return cls(
            config_data["name"],
            config_data["location"],
            config_data["products"]
        )

    def calculate_distance_to_shop(self, customer: Customer) -> float:
        return calculate_distance(self.location, customer.location)

    def calculate_product_cost(self, product_cart: dict) -> float:
        return calculate_product_cost(product_cart, self.products)

    def purchase_and_print_receipt(self, customer: Customer) -> None:
        with (patch("datetime.datetime") as mock_datetime):
            mock_datetime.now.return_value = (
                datetime.datetime(2021, 4, 1, 12, 33, 41))
        formatted_datetime = (
            datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(f"\nDate: {formatted_datetime}")
        print(f"Thanks, {customer.name}, for your purchase!"
              f"\nYou have bought:")

        product_cart = customer.product_cart

        for product, quantity in product_cart.items():
            cost_product = quantity * self.products[product]
            formatted_cost_product = str(cost_product).rstrip("0").rstrip(".")
            print(f"{quantity} {product}s for"
                  f" {formatted_cost_product} dollars")

        total_cost = self.calculate_product_cost(product_cart)
        print(f"Total cost is {total_cost} dollars"
              f"\nSee you again!")
