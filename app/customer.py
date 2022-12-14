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
    def count_cost(customer: Customers, shop_list: list[Shops], fuel_price: float) -> tuple:
        products_total_cost = 0
        min_cost = 100_000
        cheapest_shop = ""
        purchase_note = {}
        for shop in shop_list:
            for key in customer.product_cart:
                if key in shop.products:
                    one_product_total = shop.products[key] * customer.product_cart[key]
                    products_total_cost += one_product_total
                    purchase_note[key] = f"{customer.product_cart[key]} {key}s for {one_product_total} dollars"
            trip_cost = customer.car.count_trip_cost(
                customer.location,
                shop.location,
                customer.car.fuel_consumption,
                fuel_price
            )
            products_total_cost += trip_cost
            print(f"{customer.name}'s trip to the {shop.name} costs {round(products_total_cost, 2)}")
            if products_total_cost < min_cost:
                min_cost, cheapest_shop = products_total_cost, shop
            products_total_cost = 0
        return min_cost, cheapest_shop, purchase_note

