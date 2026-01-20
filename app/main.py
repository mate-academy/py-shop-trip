import json
from datetime import datetime
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip(path: str = "config.json") -> None:
    with open(path) as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    shops = [Shop(**shop_data) for shop_data in config["shops"]]
    customers = [
        Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=Car(**customer_data["car"]),
        )
        for customer_data in config["customers"]
    ]

    for idx, customer in enumerate(customers):
        print(f"{customer.name} has {customer.money} dollars")

        trip_options = []
        for shop in shops:
            total_price = customer.calculate_trip_cost(shop, fuel_price)
            if total_price is not None:
                print(f"{customer.name}'s trip to the {shop.name} "
                      f"costs {total_price:.2f}")
                trip_options.append((total_price, shop))
            else:
                print(f"{customer.name}'s trip to the {shop.name} "
                      f"cannot be completed")

        if not trip_options:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            if idx < len(customers) - 1:
                print()
            continue

        trip_options.sort(key=lambda x: x[0])
        best_price, best_shop = trip_options[0]

        if customer.money < best_price:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            if idx < len(customers) - 1:
                print()
            continue

        print(f"{customer.name} rides to {best_shop.name}")
        print()
        customer.buy(best_shop,
                     fuel_price, date=datetime(2021, 1, 4, 12, 33, 41))
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {customer.money:.2f} dollars")

        if idx < len(customers) - 1:
            print()
