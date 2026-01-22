from __future__ import annotations
from app.customer import Customer
from app.car import Car, Location
from app.shop import Shop


class Trip:
    def __init__(self) -> None:
        self.customers = []
        self.shops = []
        self.fuel_price = None

    def get_trip_data(self, initial_data: dict) -> None:
        self.fuel_price = initial_data["FUEL_PRICE"]
        for cust in initial_data["customers"]:
            self.customers.append(
                Customer(
                    name=cust["name"],
                    product_cart=cust["product_cart"],
                    home_location=Location(*cust["location"]),
                    current_location=Location(*cust["location"]),
                    money=cust["money"],
                    car=Car(brand=cust["car"]["brand"],
                            fuel_consumption=cust["car"]["fuel_consumption"])
                )
            )
        for shop in initial_data["shops"]:
            self.shops.append(
                Shop(
                    name=shop["name"],
                    location=Location(*shop["location"]),
                    products=shop["products"]
                )
            )

    def go_trip(self) -> None:
        for customer in self.customers:
            cheapest_shop = customer.plan_trip(self.shops, self.fuel_price)
            if cheapest_shop:
                customer.shopping(cheapest_shop)
                customer.go_home(cheapest_shop, self.fuel_price)
