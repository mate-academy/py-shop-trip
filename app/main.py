import json

from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        data_dict = json.load(config)
    for customer in data_dict["customers"]:
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"],
                data_dict["FUEL_PRICE"]
            )
        )
    for shop in data_dict["shops"]:
        Shop(shop["name"], shop["location"], shop["products"])

    for customer in Customer.customers.values():
        print(f"{customer.name} has {customer.money} dollars")
        for shop in Shop.shops.values():
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {customer.shop_trip_cost(shop)}")
        optimal_shop = customer.get_optimal_shop(list(Shop.shops.values()))
        if optimal_shop is not None:
            customer.go_shopping(optimal_shop)
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make purchase in any shop")
