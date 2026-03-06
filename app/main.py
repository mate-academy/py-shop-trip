import json
import os

from app.customer import Customer
from app.shop import Shop

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")


def shop_trip() -> None:
    with (open(CONFIG_PATH, "r") as f):
        config = json.load(f)
        fuel_price = config["FUEL_PRICE"]

        customers = [Customer(c_data) for c_data in config["customers"]]

        shops = [Shop(s_data) for s_data in config["shops"]]

        for customer in customers:
            print(f"{customer.name} has {customer.money} dollars")
            best_shop = None
            min_trip_cost = float("inf")  # Починаємо з нескінченності
            location_of_customer = customer.location

            for shop in shops:
                products_cost = shop.get_products_cost(customer.product_cart)
                fuel_cost = customer.get_fuel_cost(shop.location, fuel_price)

                current_trip_cost = products_cost + fuel_cost

                print(f"{customer.name}'s trip to the {shop.name}"
                      f" costs {current_trip_cost:.2f}")

                if current_trip_cost < min_trip_cost:
                    min_trip_cost = current_trip_cost
                    best_shop = shop
                    cheapest_products_cost = products_cost

            if best_shop and customer.money >= min_trip_cost:
                print(f"{customer.name} rides to {best_shop.name}\n")
                customer.location = best_shop.location

                best_shop.print_receipt(customer, cheapest_products_cost)

                print(f"{customer.name} rides home")
                customer.money -= min_trip_cost
                customer.location = location_of_customer

                print(f"{customer.name} now has "
                      f"{customer.money:.2f} dollars\n")
            else:
                print(f"{customer.name} doesn't have enough"
                      f" money to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
