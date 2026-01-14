from __future__ import annotations
from dataclasses import dataclass
from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: float
    car: Car

    @classmethod
    def create_customer_list(cls, customers: list[dict]) -> list[Customer]:
        customers_list = []
        for customer in customers:
            customers_list.append(
                Customer(
                    customer["name"],
                    customer["product_cart"],
                    customer["location"],
                    customer["money"],
                    Car.create_car(customer["car"])
                )
            )
        return customers_list

    def check_products_availability(self, shops: list[Shop]) -> list[Shop]:
        shops_with_available_products = []
        products = [key for key in self.product_cart.keys()]
        for shop in shops:
            if all(product in shop.products for product in products):
                shops_with_available_products.append(shop)
        return shops_with_available_products

    def calculate_trip_cost(
            self,
            shops: list[Shop],
            fuel_price: float
    ) -> dict:
        trip_cost = {}
        for shop in shops:
            driving_cost = self.car.calculate_drive_cost(
                self.location,
                shop.location,
                fuel_price
            ) * 2
            cart_cost = sum(
                shop.calculate_cart_cost(self.product_cart).values()
            )
            total = round(cart_cost + driving_cost, 2)
            trip_cost.update({total: shop})
        return trip_cost
