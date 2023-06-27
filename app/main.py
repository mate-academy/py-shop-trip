import json

from app.shop import Shop
from app.customer import Customer


def get_data_from_file() -> dict:
    with open("app/config.json", "r") as config_file:
        config_data = json.load(config_file)
    return config_data


def shop_trip() -> None:

    config_data = get_data_from_file()
    fuel_price = config_data["FUEL_PRICE"]
    customers_data = config_data["customers"]
    shops_data = config_data["shops"]

    customers = [Customer(**customer_data) for customer_data in customers_data]

    shops = [Shop(**shop_data) for shop_data in shops_data]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        trip_cost = 0
        min_trip_cost = float("inf")
        best_shop = None
        for shop in shops:
            trip_cost = shop.calculate_shopping_cost(customer, fuel_price)
            print(f"{customer.name}'s trip to "
                  f"the {shop.name} costs {trip_cost}")

            if trip_cost < min_trip_cost and trip_cost <= customer.money:
                min_trip_cost = trip_cost
                best_shop = shop
        if best_shop:
            print(f"{customer.name} rides to {best_shop.name}")
            best_shop.customer_receipt(customer)
            customer.money -= min_trip_cost
            print(f"\n{customer.name} rides home\n"
                  f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
