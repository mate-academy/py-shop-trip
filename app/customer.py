from __future__ import annotations

from app.car import Car
from app.shop import Shops


class Customers:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    @staticmethod
    def add_customer(customers: dict) -> list[Customers]:
        customers_list = []
        for customer in customers:
            customer_object = Customers(
                name=customer["name"],
                product_cart=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=Car(
                    brand=customer["car"]["brand"],
                    fuel_consumption=customer["car"]["fuel_consumption"]
                )
            )
            customers_list.append(customer_object)
        return customers_list

    @staticmethod
    def count_cost(
            customer: Customers,
            shop_list: list[Shops],
            fuel_price: float
    ) -> tuple:
        min_cost = 100_000
        cheapest_shop = ""
        cheapest_purchase = {}

        for shop_option in shop_list:
            purchase_note, total_cost = \
                shop_option.cost_of_products(customer.product_cart)

            trip_cost = customer.car.count_trip_cost(
                customer.location,
                shop_option.location,
                customer.car.fuel_consumption,
                fuel_price
            )
            total_cost = round(total_cost + trip_cost, 2)
            print(f"{customer.name}'s trip to the {shop_option.name} "
                  f"costs {total_cost}")

            if total_cost < min_cost:
                min_cost, cheapest_shop, cheapest_purchase = \
                    total_cost, shop_option, purchase_note
        return min_cost, cheapest_shop, cheapest_purchase
