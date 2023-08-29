import json
import os
from app.car import Car
from app.customer import Customer
from app.shop import Shop
from app.func import distance, shopping


def shop_trip() -> None:
    if __name__ == "__main__":
        path = os.path.join(os.getcwd(), "config.json")
    else:
        path = os.path.join("app", "config.json")

    with open(path, "r") as config:
        config_dict = json.load(config)

    customers = []
    for customer in config_dict["customers"]:
        customers.append(
            Customer(customer["name"],
                     customer["product_cart"],
                     customer["location"],
                     customer["money"],
                     Car(customer["car"]["brand"],
                         customer["car"]["fuel_consumption"])
                     )
        )

    shops = [Shop(*shop.values()) for shop in config_dict.get("shops")]

    for customer in customers:
        cost_of_trips = {}
        for shop in shops:
            price = (
                shop.price_of_products(customer)
                + customer.riding_cost(distance(customer.location,
                                                shop.location),
                                       config_dict["FUEL_PRICE"])
            )
            cost_of_trips[price] = shop

        cheapest_shop = cost_of_trips[min(cost_of_trips.keys())]
        customer.needed_money = min(cost_of_trips.keys())
        shopping(customer, cheapest_shop, cost_of_trips)


# shop_trip()
