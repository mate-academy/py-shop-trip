import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        config = json.load(config_file)
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
            price_for_trip = customer.calculate_way_price(
                shop.location, fuel_price
            ) + shop.calculate_product_price(customer)
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {round(price_for_trip, 2)}")
            price_shop_list[price_for_trip] = shop
        min_price = min(price_shop_list)
        cheapest_shop = price_shop_list[min_price]

        if customer.money >= min_price:
            print(f"{customer.name} rides to "
                  f"{cheapest_shop.name}\n")
            home_location = customer.location
            customer.location = cheapest_shop.location
            cheapest_shop.print_receipt(customer)
            print(f"{customer.name} rides home\n{customer.name} now has "
                  f"{round(customer.money - min_price, 2)} dollars\n")
            customer.location = home_location
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
