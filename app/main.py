import json

from os import path

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    project_dir = path.dirname(path.dirname(path.abspath(__file__)))
    config_file = path.join(project_dir, "app/config.json")
    with open(config_file, "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    customers = [
        Customer(
            c["name"], c["product_cart"], c["location"], c["money"],
            Car(c["car"]["brand"], c["car"]["fuel_consumption"])
        ) for c in config["customers"]
    ]
    shops = [
        Shop(s["name"], s["location"], s["products"]) for s in config["shops"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        trip_costs = {
            shop.name: customer.calculate_trip_cost(shop, fuel_price)
            for shop in shops
        }
        for shop_name, cost in trip_costs.items():
            print(f"{customer.name}'s trip to the {shop_name} costs {cost}")

        cheapest_shop = min(trip_costs, key=trip_costs.get)
        if trip_costs[cheapest_shop] <= customer.money:
            chosen_shop = next(
                shop for shop in shops if shop.name == cheapest_shop
            )
            print(f"{customer.name} rides to {chosen_shop.name}")
            print()
            chosen_shop.print_receipt(customer)
            customer.money -= trip_costs[cheapest_shop]
            print(f"{customer.name} rides home")
            print(
                f"{customer.name} now has {round(customer.money, 2)} dollars"
            )
            print()
        else:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
