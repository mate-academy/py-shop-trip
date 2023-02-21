from __future__ import annotations
import datetime

from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: float,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    @staticmethod
    def customers_maker(
            customers_in_dict: dict
    ) -> dict[Customer]:
        customers_instances = {}

        for customer in customers_in_dict:
            customers_instances[customer.get("name")] = Customer(
                name=customer.get("name"),
                product_cart=customer.get("product_cart"),
                location=customer.get("location"),
                money=customer.get("money"),
                car=Car(
                    brand=customer.get("car").get("brand"),
                    fuel_consumption=customer.get("car").get(
                        "fuel_consumption")
                )
            )
        return customers_instances

    @staticmethod
    def print_customer_trip(
            customer: Customer,
            cheapest_trip: dict,
            min_cost: float
    ) -> None:
        print(
            f"{customer.name} rides to "
            f"{cheapest_trip.get('shop').name}\n")
        print((datetime.datetime.now()).strftime("Date: %d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")

        for product_dict in cheapest_trip.get("purchased_products"):
            for product in product_dict:
                total = product_dict[product].get("price") * product_dict[
                    product].get("amount")

                print(
                    f"{product_dict[product].get('amount')} "
                    f"{product}s for "
                    f"{total} dollars"
                )
        print(
            f"Total cost is "
            f"{cheapest_trip.get('products_total_price')} dollars"
        )

        customer.money -= min_cost

        print("See you again!\n")
        print(f"{customer.name} rides home")
        print(
            f"{customer.name} now has {customer.money} dollars\n")
