import json

from app.customer import Customer


with open("app/config.json", "r") as file_out:
    data = json.load(file_out)
DATA_SHOPS = data["shops"]
FUEL = data["FUEL_PRICE"]
DATA_CUSTOMERS = data["customers"]


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_trip(self, customer: Customer) -> float:
        loc_shop = self.location
        loc_custom = customer.location

        x_coor = (loc_shop[0] - loc_custom[0]) ** 2
        y_coor = (loc_shop[1] - loc_custom[1]) ** 2
        road = (x_coor + y_coor) ** 0.5

        road *= customer.car["fuel_consumption"]
        road /= 100
        road *= FUEL
        road *= 2

        amount = 0
        for prod, num in customer.product_cart.items():
            for prod_, num_ in self.products.items():
                if prod == prod_:
                    amount += num * num_

        amount += road
        return round(amount, 2)


def make_instances(value: dict) -> list:
    l_instances = []
    for i in value:
        if len(i) == 3:
            for key in value:
                l_instances.append(
                    Shop(key["name"], key["location"], key["products"])
                )
        if len(i) == 5:
            for key in value:
                l_instances.append(
                    Customer(
                        key["name"],
                        key["product_cart"],
                        key["location"],
                        key["money"],
                        key["car"],
                    )
                )
        return l_instances
