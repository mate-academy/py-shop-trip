import json

from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:

    with open("app/config.json", "r") as config_file:
        config_data = json.load(config_file)

    fuel_price = config_data["FUEL_PRICE"]
    customers_data = config_data["customers"]
    shops_data = config_data["shops"]

    customers = [Customer(**customer_data) for customer_data in customers_data]

    shops = [Shop(**shop_data) for shop_data in shops_data]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        min_trip_cost = float("inf")
        best_shop = None
        for shop in shops:
            min_trip_cost, best_shop = shop.choosing_shop(customer,
                                                          fuel_price,
                                                          min_trip_cost,
                                                          best_shop)
        if best_shop:
            best_shop.best_shop_visit(customer, min_trip_cost)

        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
