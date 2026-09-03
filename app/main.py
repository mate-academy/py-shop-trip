import json
import datetime
import math

from app.car import Car
from app.customer import Customer
from app.helpers import format_float
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)

    fuel_price = data["FUEL_PRICE"]
    customers = [
        Customer(car=Car(**c.pop("car")), **c)
        for c in data["customers"]
    ]
    shops = [Shop(**s) for s in data["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        total_price_per_shop = {}
        product_cost_per_shop = {}
        for shop in shops:
            c_loc = customer.location
            s_loc = shop.location

            shop_distance = math.sqrt(
                (c_loc[0] - s_loc[0]) ** 2 + (c_loc[1] - s_loc[1]) ** 2
            )
            car_cons = customer.car.fuel_consumption
            fuel_both_ways = shop_distance / 100 * car_cons * fuel_price * 2

            product_cost = sum(
                customer.product_cart[cart_item] * shop.products[cart_item]
                for cart_item in customer.product_cart
            )
            product_cost_per_shop[shop.name] = product_cost

            full_cost = fuel_both_ways + product_cost
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {full_cost:.2f}")
            total_price_per_shop[shop.name] = full_cost

        cheapest_shop = min(total_price_per_shop.values())
        if cheapest_shop > customer.money:
            print(
                f"{customer.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )
            continue
        shop_name = next(
            (k for k, v in total_price_per_shop.items() if v == cheapest_shop)
        )
        shop = next((s for s in shops if s.name == shop_name))
        print(f"{customer.name} rides to {shop.name}\n")

        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!\nYou have bought:")
        for item, quantities in customer.product_cart.items():
            print(
                f"{quantities} {item}s for "
                f"{format_float(quantities * shop.products[item])} dollars"
            )
        print(f"Total cost is {product_cost_per_shop[shop.name]:.1f} dollars")
        print("See you again!\n")

        customer.money -= cheapest_shop
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {customer.money:.2f} dollars\n")


if __name__ == "__main__":
    shop_trip()
