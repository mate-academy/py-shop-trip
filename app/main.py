import json
import os
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    try:
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   "..", "config.json")
        if not os.path.exists(config_path):
            config_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "config.json")

        with open(config_path, "r") as file:
            config = json.load(file)

    except FileNotFoundError:
        print("Error: config.json not found. Check the file path.")
        return

    fuel_price = config["FUEL_PRICE"]

    customers = [Customer.from_dict(data) for data in config["customers"]]
    shops = [Shop.from_dict(data) for data in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        cheapest_trip_cost = float("inf")
        cheapest_shop = None

        for shop in shops:
            current_trip_cost = customer.calculate_trip_cost(
                shop,
                fuel_price
            )
            print(
                f"{customer.name}'s trip to the {shop.name} costs {current_trip_cost:.2f}")

            if current_trip_cost < cheapest_trip_cost:
                cheapest_trip_cost = current_trip_cost
                cheapest_shop = shop

        if cheapest_trip_cost != float(
                "inf") and customer.money >= cheapest_trip_cost:

            customer.make_trip(cheapest_shop, cheapest_trip_cost)
        else:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
