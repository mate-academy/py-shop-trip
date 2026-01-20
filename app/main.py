import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)
    fuel_price = config["FUEL_PRICE"]
    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(**customer["car"])
        )
        for customer in config["customers"]
    ]
    shops = [
        Shop(**shop)
        for shop in config["shops"]
    ]

    for customer in customers:
        customer.initial_money()
        price_shop_list = {}
        for shop in shops:
            price_trip = customer.price_way_to_shop_or_home(
                shop.location, fuel_price
            ) + shop.calculate_product_price(customer)
            print(f"{customer.name}'s "
                  f"trip to the {shop.name} "
                  f"costs {round(price_trip, 2)}")
            price_shop_list[price_trip] = shop
        min_price = min(price_shop_list)
        cheap_shop = price_shop_list[min_price]

        if customer.money >= min_price:
            print(f"{customer.name} rides to {cheap_shop.name}\n")
            home = customer.location
            customer.location = cheap_shop.location
            cheap_shop.print_check(customer)
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{round(customer.money - min_price, 2)}"
                  f" dollars\n")
            customer.location = home
        else:
            print(f"{customer.name} "
                  f"doesn't have enough money"
                  f" to make a purchase in any shop")
