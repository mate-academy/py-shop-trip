import json

from pathlib import Path

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = Path(__file__).parent / "config.json"
    if not config_path.exists():
        raise FileNotFoundError(f"Cannot find config.json at {config_path}")

    with open(config_path) as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]

    shops = [Shop(shop["name"], shop["location"], shop["products"])
             for shop in config["shops"]]

    customers_data = config["customers"]
    for i, cust_data in enumerate(customers_data):
        car_info = cust_data["car"]
        car = Car(car_info["brand"], car_info["fuel_consumption"])
        customer = Customer(cust_data["name"], cust_data["location"],
                            cust_data["money"], cust_data["product_cart"], car)

        print(f"{customer.name} has {customer.money} dollars")

        costs = [(shop, round(customer.trip_cost(shop, fuel_price), 2))
                 for shop in shops]
        for shop, cost in costs:
            print(f"{customer.name}'s trip to the {shop.name} costs {cost}")

        costs.sort(key=lambda x: x[1])
        for shop, cost in costs:
            if cost <= customer.money:
                customer.go_to_shop(shop, fuel_price, cost)
                break
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")

        if i < len(customers_data) - 1:
            print()


if __name__ == "__main__":
    shop_trip()
