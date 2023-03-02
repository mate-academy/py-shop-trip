from datetime import datetime
import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)
        for customer_data in data["customers"]:
            customer = Customer(**customer_data)
            print(f"{customer.name} has {customer.money} dollars")
            closest = {}
            shop_names = {}
            for shop_data in data["shops"]:
                shop = Shop(**shop_data)
                fuel = customer.car["fuel_consumption"]
                prod_total = sum(a * b for a, b in zip(
                    shop.prod_price(),
                    customer.product_cart.values()
                ))
                fuel_total = round(
                    customer.fuel_shop(
                        fuel, customer.dist_shop(shop.location)
                    ), 2
                )
                expenses = prod_total + fuel_total
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
                    f"enough money to make a purchase in any shop"
                )
                break
            print()
            print(f"Date: {datetime.now():%d/%m/%Y %H:%M:%S}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            total_costs = 0
            for product_name, product_count in customer.product_cart.items():
                if product_name in shop_names[closest_shop_name]:
                    product_price = shop_names[closest_shop_name][product_name]
                    product_total_cost = product_price * product_count
                    total_costs += product_total_cost
                    print(
                        f"{product_count} {product_name}s "
                        f"for {product_total_cost} dollars"
                    )
            print(f"Total cost is {total_costs} dollars")
            print("See you again!")
            print()
            print(f"{customer.name} rides home")
            print(
                f"{customer.name} now has "
                f"{customer.money - min(closest.values())} dollars"
            )
            print()
