import json
import os

from app.customer import Customer
from app.shop import Shop
from app.services import calculate_trip_price


def shop_trip() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "config.json")

    with open(
        config_path, "rb"
    ) as file:
        config = json.load(file)

    customer_list = Customer.get_customer_list(config)
    shop_list = Shop.get_shop_list(config)
    fuel_price = config.get("FUEL_PRICE")
    result = []

    for customer in customer_list:
        result.append(f"\n{customer.name} has {customer.money} dollars\n")
        shop_choice = None

        for shop in shop_list:
            trip_price = calculate_trip_price(customer, shop, fuel_price)
            receipt_cost = shop.get_receipt(customer)[1]
            whole_price = receipt_cost + trip_price * 2

            if not shop_choice:
                shop_choice = (shop, whole_price)

            if shop_choice[1] > whole_price:
                shop_choice = (shop, whole_price)

            result.append(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {round(whole_price, 2)}\n"
            )

        shop, trip_price = shop_choice
        customer.travel_to_shop(shop.location)

        if customer.money < trip_price:
            result.append(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop\n"
            )
            continue

        receipt, cost = shop.get_receipt(customer)

        result.append(
            f"{customer.name} rides to {shop.name}\n"
            f"\n{receipt}"
            f"\n{customer.name} rides home\n"
            f"{customer.name} now has "
            f"{round(customer.money - trip_price, 2)} dollars\n"
        )
        customer.travel_to_home()

    print("".join(result).strip("\n"))
