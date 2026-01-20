import json
from pathlib import Path

from app.car import Car
from app.customer import Customer
from app.shop import Shop

current_file = Path(__file__).parent / "config.json"


def shop_trip() -> None:
    with open(current_file) as js_data:
        data: dict = json.load(js_data)

        fuel_price = data["FUEL_PRICE"]

        customers = [
            Customer(
                name=customer["name"],
                product_cart=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=Car(**customer["car"]),
            )
            for customer in data["customers"]
        ]
        shops = [
            Shop(
                name=shops["name"],
                location=shops["location"],
                products=shops["products"],
            )
            for shops in data["shops"]
        ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        min_price_shop = None
        lowest_price = float("inf")
        for shop in shops:
            user_info = customer.calculate_distance_price(shop, fuel_price)
            print(user_info["msg"])
            if user_info["price"] < lowest_price:
                min_price_shop = shop
                lowest_price = user_info["price"]

        if customer.money > lowest_price:
            print(f"{customer.name} rides to {min_price_shop.name}\n")
            print(customer.check_out_in_shop(min_price_shop))
            print()
            print(f"{customer.name} rides home")
            print(
                f"{customer.name} now has "
                f"{customer.money - lowest_price} dollars\n"
            )
        else:
            print(
                f"{customer.name} doesn't have enough"
                f" money to make a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
