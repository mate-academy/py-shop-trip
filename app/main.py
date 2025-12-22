import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)
        fuel_price = data["FUEL_PRICE"]

    shops = Shop.create_shops("app/config.json")
    for customer_data in data["customers"]:
        customer = Customer(**customer_data)
        print(f"{customer.name} has {customer.money} dollars")
        closest = {}
        for shop in shops:
            if not shop.is_all_products_exist(customer.product_cart):
                continue
            fuel = customer.car["fuel_consumption"]
            expenses = (customer.product_total
                        (shop.products) + customer.fuel_expenses(
                            fuel, shop.location, fuel_price
                        )
                        )
            closest[shop.name] = expenses
            print(
                f"{customer.name}'s trip "
                f"to the {shop.name} costs {expenses}"
            )
        closest_shop_name = min(closest, key=closest.get)
        if customer.money > closest[closest_shop_name]:
            print(f"{customer.name} rides to {closest_shop_name}")
        else:
            print(
                f"{customer.name} doesn't have "
                f"enough money to make a purchase in any shop"
            )
            continue

        preferred_shop = next(
            filter(lambda shp: shp.name == closest_shop_name, shops)
        )
        print()
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")
        customer.shop_choice(preferred_shop)
        print("See you again!")
        print()
        print(f"{customer.name} rides home")
        print(
            f"{customer.name} now has "
            f"{customer.money - min(closest.values())} dollars"
        )
        print()
