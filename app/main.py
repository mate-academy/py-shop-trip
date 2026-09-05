import json
import os


from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    path = os.path.join("app", "config.json")
    with open(path, "r", encoding="utf-8") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]

    customers = [Customer.from_dict(customer_dict)
                 for customer_dict in config["customers"]]

    shops = [Shop.from_dict(shop_dict)
             for shop_dict in config["shops"]]

    for customer in customers:
        customer.money_print()
        bargain_shop = None

        for shop in shops:

            total_trip_cost = customer.calculate_full_trip_cost(shop,
                                                                fuel_price)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs "
                  f"{total_trip_cost}")

            if total_trip_cost <= customer.money and (
                bargain_shop is None or total_trip_cost < bargain_shop["cost"]
            ):
                bargain_shop = {"shop": shop, "cost": total_trip_cost}

        if bargain_shop:
            print(f"{customer.name} rides to "
                  f"{bargain_shop.get('shop').name}\n")
            customer.money -= (
                customer.calculate_full_trip_cost(bargain_shop["shop"],
                                                  fuel_price)
            )
            customer.shopping(bargain_shop["shop"])
            customer.ride_home()

        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
