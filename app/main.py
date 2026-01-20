import os
import json
from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    shops = [Shop(s["name"], tuple(s["location"]),
                  s["products"]) for s in config["shops"]]
    customers = [
        Customer(
            c["name"],
            tuple(c["location"]),
            c["money"],
            c["product_cart"],
            Car(c["car"]["brand"], c["car"]["fuel_consumption"]),
        )
        for c in config["customers"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            if trip_cost is not None:
                print(f"{customer.name}'s trip to the "
                      f"{shop.name} costs {trip_cost:.2f}")
        best_shop = customer.choose_best_shop(shops, fuel_price)
        if best_shop:
            customer.go_shopping(best_shop, fuel_price)
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
