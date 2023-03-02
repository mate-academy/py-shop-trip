import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)
        fuel_price = data["FUEL_PRICE"]
        for customer_data in data["customers"]:
            customer = Customer(**customer_data)
            print(f"{customer.name} has {customer.money} dollars")
            closest = {}
            shop_names = {}
            for shop_data in data["shops"]:
                shop = Shop(**shop_data)
                fuel = customer.car["fuel_consumption"]
                customer.product_total(shop.products)
                customer.fuel_expenses(fuel, shop.location, fuel_price)
                expenses = (
                    customer.product_total(shop.products)
                    + customer.fuel_expenses(fuel, shop.location, fuel_price)
                )
                closest[shop.name] = expenses
                shop_names[shop.name] = shop.products
                print(
                    f"{customer.name}'s trip "
                    f"to the {shop.name} costs {expenses}"
                )
            if customer.money > expenses:
                closest_shop_name = min(closest, key=closest.get)
                print(f"{customer.name} rides to {closest_shop_name}")
            else:
                print(
                    f"{customer.name} doesn't have "
                    f"enough money to make purchase in any shop"
                )
                break
            print()
            print("Date: 04/01/2021 12:33:41")
            print(f"Thanks, {customer.name}, for you purchase!")
            print("You have bought: ")
            customer.shop_choice(shop_names, closest_shop_name)
            print("See you again!")
            print()
            print(f"{customer.name} rides home")
            print(
                f"{customer.name} now has "
                f"{customer.money - min(closest.values())} dollars"
            )
            print()
