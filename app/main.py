import json
import os

from app.customer import Customer
from app.shop import Shop


cur_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(cur_dir, "config.json")


def shop_trip() -> None:
    with open(config_path, "r") as file:
        config = json.load(file)

    customers = config["customers"]
    customers_list = [Customer(customer) for customer in customers]

    shops = config["shops"]
    shops_list = [Shop(shop) for shop in shops]

    for customer in customers_list:
        print(f"{customer.name} has {customer.money} dollars")

        total_price_dict = {}
        for shop in shops_list:
            distance = customer.calculate_distance(customer.location,
                                                   shop.location
                                                   )
            fuel_cost = customer.calculate_fuel_cost(
                customer.car.fuel_consumption,
                distance,
                config["FUEL_PRICE"]
            )
            product_price = customer.calculate_products_cost(
                customer.product_cart,
                shop.products
            )
            total_price_trip = round(fuel_cost * 2 + sum(product_price), 2)
            print(f"{customer.name}'s trip to the {shop.name}"
                  f" costs {total_price_trip}")

            total_price_dict[shop.name] = total_price_trip

        min_total_price = min(total_price_dict.values())
        shop_name_with_min_total_price = ""
        for key, value in total_price_dict.items():
            if value == min_total_price:
                shop_name_with_min_total_price = key

        if customer.money >= min_total_price:
            print(f"{customer.name} rides to {shop_name_with_min_total_price}")

            for shop in shops_list:
                if shop.name == shop_name_with_min_total_price:
                    customer.prints_purchase_receipt(shop.products)

            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{customer.money - min_total_price} dollars")
            print()
        else:
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")
