from __future__ import annotations
from math import sqrt
from app.customer import Customer


class Shop:

    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.products = products
        self.location = location
        self.name = name
        self.cost = 0

    def get_check_amount(self, product_cart: dict) -> int | float:
        return sum(
            self.get_product_price(product)
            * qty
            for product, qty
            in product_cart.items())

    def get_product_price(self, product_name: str) -> float:
        return self.products[product_name]

    def get_logistics_costs(
            self,
            customer: Customer,
            fuel_price: float) -> None:
        x1, y1 = self.location
        x2, y2 = customer.location
        distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        fuel_costs = ((distance
                      * customer.car.fuel_consumption
                      / 100)
                      * fuel_price
                      * 2
                      )
        return fuel_costs

    def get_total_cost_per_store(
            self,
            customer: Customer,
            fuel_price: float
    ) -> int | float:
        products_cost = self.get_check_amount(customer.product_cart)
        fuel_costs = self.get_logistics_costs(customer, fuel_price)
        return products_cost + fuel_costs

    @classmethod
    def create_shops(cls, data: dict) -> list[Shop]:
        """Create Shop instances from the provided data."""
        shops = []
        for shop_data in data["shops"]:
            shops.append(
                cls(
                    name=shop_data["name"],
                    products=shop_data["products"],
                    location=shop_data["location"]
                )
            )
        return shops
