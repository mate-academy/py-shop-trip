import json

from app.customer import Customer


def open_file(value):
    with open("app/config.json", "r") as file_out:
        data = json.load(file_out)
    data_shops = data["shops"]
    fuel = data["FUEL_PRICE"]
    data_customers = data["customers"]
    if value == "customers":
        return data_customers
    if value == "fuel":
        return fuel
    if value == "shops":
        return data_shops


class Shop:
    def __init__(self, name: str, location: list, products: dict):
        self.name = name
        self.location = location
        self.products = products

    def calculate_trip(self, customer: Customer):
        loc_shop = self.location
        loc_custom = customer.location

        x = (loc_shop[0] - loc_custom[0]) ** 2
        y = (loc_shop[1] - loc_custom[1]) ** 2
        road = (x + y) ** 0.5

        road *= customer.car["fuel_consumption"]
        road /= 100
        road *= open_file("fuel")
        road *= 2

        amount = 0
        for prod, num in customer.product_cart.items():
            for prod_, num_ in self.products.items():
                if prod == prod_:
                    amount += num * num_

        amount += road
        return round(amount, 2)


def make_instances(value):
    l_instances = []
    for i in value:
        if len(i) == 3:
            for j in value:
                l_instances.append(
                    Shop(j["name"], j["location"], j["products"])
                )
        if len(i) == 5:
            for j in value:
                l_instances.append(
                    Customer(
                        j["name"],
                        j["product_cart"],
                        j["location"],
                        j["money"],
                        j["car"],
                    )
                )
        return l_instances
