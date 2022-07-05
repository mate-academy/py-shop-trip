import json
from dataclasses import dataclass


@dataclass()
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: dict
    fuel: float

    @classmethod
    def create_customer(cls, file_name: str):
        with open(file_name, "r") as f_json:
            info = json.load(f_json)
            lst = []
            for customer in info["customers"]:
                lst.append(cls(name=customer["name"],
                           product_cart=customer["product_cart"],
                           location=customer["location"],
                           money=customer["money"],
                           car=customer["car"],
                           fuel=2.4))
            return lst

    def distant(self, other):
        x_shop = other.location[0]
        x_customer = self.location[0]
        y_shop = other.location[1]
        y_customer = self.location[1]
        x = x_shop - x_customer
        y = y_shop - y_customer
        return round((((x ** 2) + (y ** 2)) ** 0.5) * 2, 2)

    def has_money(self):
        print(f"{self.name} has {self.money} dollars")

    def cost(self, other):
        total_groc = 0
        for key in self.product_cart.keys():
            total_groc += self.product_cart[key] * other.products[key]
            distant = self.distant(other)
            fuel_cost_1_km = self.car["fuel_consumption"] * self.fuel / 100
            fuel_cost = distant * fuel_cost_1_km
        total = round(total_groc + fuel_cost, 2)
        return total

    def to_shop(self, other):
        self.location = other.location
        print(f"{self.name} rides to {other.name}")

    def to_home(self):
        print(f"{self.name} rides home")

    def remain_money(self, other):
        return f"{self.name} now has {self.money - self.cost(other)} dollars"
