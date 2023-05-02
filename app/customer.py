import json
from app.car import fuel_price


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def sum_products(self, product_shop: dict) -> float:
        cost_products = 0
        for name_product, quantity in self.product_cart.items():
            if name_product in product_shop:
                cost_products += quantity * product_shop[name_product]
        return cost_products

    def cost_trip(self, distance: float) -> float:
        return (self.car["fuel_consumption"] / 100
                ) * (distance * 2) * fuel_price


with open("app/config.json", "r") as file_json:
    customers = json.load(file_json)["customers"]


customers_list = [Customer(customer["name"],
                           customer["product_cart"],
                           customer["location"],
                           customer["money"],
                           customer["car"])
                  for customer in customers]
