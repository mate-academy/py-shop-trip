import json
import datetime
from decimal import Decimal, getcontext
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    getcontext().prec = 10

    with open("app/config.json", "r") as config_file:
        config = json.load(config_file)

    fuel_price = Decimal(str(config["FUEL_PRICE"]))

    dict_of_client = {"customers": {}, "shops": {}}

    for shop_data in config["shops"]:
        dict_of_client["shops"].update({shop_data["name"]: Shop(**shop_data)})

    for customer_data in config["customers"]:
        dict_of_client["customers"].update({customer_data["name"]: Car(**customer_data)})

    two_places = Decimal('0.01')

    for client in dict_of_client["customers"].values():
        full_shops = list(dict_of_client["shops"].values())
        shop_prices = []
        for shop in full_shops:
            trip_cost = client.from_to_shop(fuel_price, shop) * Decimal('2')
            product_cost = client.check_price_products(shop)
            total_cost = (trip_cost + product_cost).quantize(two_places)
            shop_prices.append(total_cost)

        min_shop_price = min(shop_prices)

        print(f"{client.name} has {client.money} dollars")

        for index, _ in enumerate(shop_prices):
            print(f"{client.name}'s trip to the {full_shops[index].name} costs {shop_prices[index]}")

        if min_shop_price > client.money:
            print(f"{client.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            continue

        shop = full_shops[shop_prices.index(min_shop_price)]

        print(f"{client.name} rides to {shop.name}\n")
        client.location = shop.location

        # *** check ***
        print(
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {client.name}, for your purchase!\n"
            f"You have bought:"
        )

        full_cost = []
        for key, value in client.product_cart.items():
            cost = shop.products[key] * value
            if cost == int(cost):
                cost = int(cost)
            print(
                f"{value} {key}s "
                f"for {cost} "
                f"dollars")
            full_cost.append(cost)

        total_product_cost = sum(full_cost)
        print(
            f"Total cost is {total_product_cost} dollars\n"
            "See you again!\n"
        )
        # *** ----- ***

        client.money -= min_shop_price
        print(
            f"{client.name} rides home\n"
            f"{client.name} now has {client.money.quantize(two_places)} dollars\n"
        )
