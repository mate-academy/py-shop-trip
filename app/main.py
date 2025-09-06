import json
from datetime import datetime
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    with open("config.json", "r") as file:
        config = json.load(file)

    dict_of_client = {"customers": {}, "shops": {}}

    for shop in config["shops"]:
        dict_of_client["shops"].update({shop["name"]: Shop(**shop)})
    # print(dict_of_client["shops"])

    for customer in config["customers"]:
        dict_of_client["customers"].update({customer["name"]: Car(**customer)})
    # print(dict_of_client["customers"])

    for client in dict_of_client["customers"].values():
        full_shops = list(dict_of_client["shops"].values())
        shop_prices = [client.check_price_products(shop)
                       for shop in full_shops]

        min_shop_price = min(shop_prices)
        shop = full_shops[shop_prices.index(min_shop_price)]

        print(f"{client.name} has {client.money} dollars")
        if min_shop_price > client.money:
            print(f"{client.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            continue

        print(f"{client.name} bought to the {shop.name} "
              f"costs {min_shop_price}")

        way_price = client.from_to_shop(config["FUEL_PRICE"], shop)

        if min_shop_price + way_price * 2 > client.money:
            print(f"{client.name} doesn't have enough money "
                  f"to get to the store")
            continue

        print(f"{client.name} trip to the {shop.name} "
              f"costs {min_shop_price + way_price}")

        client_back_location = client.location
        print(f"{client.name} went to the store {shop.name}")

        client.location = shop.location
        client.money -= way_price

        print(f"{client.name} arrived to the store\n")
        client.money -= min_shop_price

        # *** Check ***
        print(
            f"Date: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n"
            f"Thanks, {client.name}, for your purchase\n"
            f"You have bought: \n"
        )

        for key, value in client.product_cart.items():
            print(f"{value} {key} "
                  f"for {shop.products[key] * client.product_cart[key]} "
                  f"dollars")

        print(f"Total cost is {min_shop_price} dollars\n"
              "See you again!\n")

        print(f"{client.name} moved home")
        client.money -= way_price
        client.location = client_back_location
        print(f"{client.name} arrived home\n"
              f"{client.name} now has {client.money} dollars\n")
