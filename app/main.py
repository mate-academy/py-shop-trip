import json
from .car import Car
from .customer import Customer
from .shop import Shop


def shop_trip() -> None:
    with open("config.json", "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    customers_data = config["customers"]
    shops_data = config["shops"]

    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        ) for shop in shops_data
    ]
    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]
            )
        ) for customer in customers_data
    ]

    for customer in customers:
        print(f"\n{customer.name} has {customer.money} dollars")
        cheapest_trip_cost = float("inf")
        chosen_shop = None

        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {trip_cost:.2f}"
            )
            if trip_cost < cheapest_trip_cost:
                cheapest_trip_cost = trip_cost
                chosen_shop = shop

        if cheapest_trip_cost <= customer.money:
            print(f"{customer.name} rides to {chosen_shop.name}")
            customer.update_location(chosen_shop.location)
            customer.buy_products(chosen_shop)
            customer.update_location(customer.location)
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money:.2f} dollars")
        else:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase "
                "in any shop"
            )
