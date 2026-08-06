import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        data = json.load(config_file)
    Car.set_fuel_price(data.get("FUEL_PRICE", 0.0))
    customers = [
        Customer.from_dict(customer) for customer in data.get("customers", [])
    ]
    shops = [Shop.from_dict(shop) for shop in data.get("shops", [])]

    for customer in customers:
        print("{} has {} dollars".format(customer.name, customer.money))
        for shop in shops:
            cost = customer.shopping_cost(shop)
            print(
                "{}'s trip to the {} costs {}".format(
                    customer.name, shop.name, cost
                )
            )
        customer.go_shopping()
