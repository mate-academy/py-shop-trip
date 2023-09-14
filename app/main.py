import json
import os

from app.customer import Customer
from app.shop import Shop

app_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(app_dir, "config.json")


def shop_trip() -> None:
    with open(config_path, "r") as config_file:
        config = json.load(config_file)
    fuel_price, customers, shops = config.values()
    customers = [Customer(data) for data in customers]
    shops = [Shop(data) for data in shops]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        min_trip_cost = float("inf")
        best_shop = None

        for shop in shops:
            distance = customer.calculate_distance(
                customer.location, shop.location
            )
            trip_cost = customer.calculate_fuel_cost(
                distance, fuel_price, customer.car.fuel_consumption
            )

            purchase_cost = shop.calculate_purchase_cost(
                customer.product_cart
            )
            total_cost = 2 * trip_cost + purchase_cost

            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {total_cost:.2f}"
            )

            if total_cost < min_trip_cost and total_cost <= customer.money:
                min_trip_cost = total_cost
                best_shop = shop

        if best_shop:
            print(f"{customer.name} rides to {best_shop.name}\n")
            customer.location = best_shop.location
            best_shop.purchase_products(
                customer.name, customer.product_cart
            )

            customer.money -= min_trip_cost
            print(f"\n{customer.name} rides home")
            print(f"{customer.name} now has {customer.money:.2f} dollars\n")
        else:
            print(
                f"{customer.name} doesn't have enough"
                f" money to make a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
