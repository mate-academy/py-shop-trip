import json

from pathlib import Path

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = Path(__file__).resolve().parent / "config.json"
    with open(config_path, "r", encoding="utf-8") as json_file:
        raw_data = json.load(json_file)
        fuel_price = raw_data["FUEL_PRICE"]
        shops = []
        customers = []

        for shop in raw_data["shops"]:
            shop = Shop(shop["name"], shop["location"], shop["products"])
            shops.append(shop)

        for customer in raw_data["customers"]:
            customer = Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(customer["car"]["brand"],
                    customer["car"]["fuel_consumption"]),
            )
            customers.append(customer)

        for customer in customers:
            print(f"{customer.name} has {customer.money} dollars")
            cheapest_shop, trip_cost = customer.choose_cheapest_shop(
                shops,
                fuel_price
            )

            if customer.money < trip_cost:
                print(f"{customer.name} "
                      f"doesn't have enough money "
                      f"to make a purchase in any shop")
            else:
                print(f"{customer.name} rides to {cheapest_shop.name}\n")
                cheapest_shop.print_receipt(customer)
                customer.money -= trip_cost
                print(f"{customer.name} rides home")
                print(f"{customer.name} now has {customer.money} dollars\n")
