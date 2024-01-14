import json
import os

from app.customer.customer import Customer
from app.shop import Shop

main_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(main_path, "config.json")


def shop_trip() -> None:
    with open(file_path) as config:
        info = json.load(config)

    customers = [Customer(customer) for customer in info["customers"]]
    shops = [Shop(shop) for shop in info["shops"]]
    fuel_price = info["FUEL_PRICE"]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        cheapest_shop = None
        cheapest_trip_cost = 0

        for shop in shops:
            cost = customer.calculate_trip_cost(fuel_price, shop)

            print(f"{customer.name}'s trip to the {shop.name} costs {cost}")
            if not cheapest_shop or cost < cheapest_trip_cost:
                cheapest_shop = shop
                cheapest_trip_cost = cost

        if customer.money < cheapest_trip_cost:
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")
            continue

        print(f"{customer.name} rides to {cheapest_shop.name}\n")
        cheapest_shop.products_purchase(customer)

        print(f"{customer.name} rides home")
        customer.location = customer.home_location

        customer.money -= cheapest_trip_cost
        print(f"{customer.name} now has {customer.money} dollars\n")


if __name__ == "__main__":
    shop_trip()
