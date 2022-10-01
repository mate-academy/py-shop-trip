import json

from app.customer import Customer

with open("config.json", "r") as f:
    data = json.load(f)
data_shops = data["shops"]
fuel = data["FUEL_PRICE"]


class Shop:
    def __init__(self, name: str,
                 location: list,
                 products: dict):
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

        amount = 0
        for prod, num in customer.product_cart.items():
            for prod_, num_ in self.products.items():
                if prod == prod_:
                    amount += num * num_

        amount += road
        return round(amount, 2)


shops = []
for store in data_shops:
    shops.append(Shop(store["name"],
                      store["location"],
                      store["products"]))
