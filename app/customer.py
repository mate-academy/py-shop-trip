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
    def create_customer(customers: dict) -> list[Customers]:
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
    def count_cost(customer: Customers, shop_list: list[Shops]):
        result = 0
        for shop in shop_list:
            for key in customer.product_cart:
                if key in shop.products:
                    result += shop.products[key] * customer.product_cart[key]
            print(f"{customer.name}'s trip to the {shop.name} costs {result}")


