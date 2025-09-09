import json
import datetime
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    with open("config.json", "r") as file:
        config = json.load(file)

    dict_of_client = {"customers": {}, "shops": {}}

    for shop in config["shops"]:
        dict_of_client["shops"].update({shop["name"]: Shop(**shop)})

    for customer in config["customers"]:
        dict_of_client["customers"].update({customer["name"]: Car(**customer)})

    for client in dict_of_client["customers"].values():
        full_shops = list(dict_of_client["shops"].values())
        shop_prices = [round(client.from_to_shop(config["FUEL_PRICE"], full_shops[index]) * 2 + client.check_price_products(shop), 2)
                       for index, shop in enumerate(full_shops)]

        min_shop_price = min(shop_prices)

        print(f"{client.name} has {client.money} dollars")

        for index, _shop in enumerate(shop_prices):
            print(f"{client.name} trip to the shop {full_shops[index].name} costs {shop_prices[index]}")

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
            f"You have bought: "
        )

        full_cost = []
        for key, value in client.product_cart.items():
            cost = shop.products[key] * client.product_cart[key]
            print(
                f"{value} {key} "
                f"for {cost} "
                f"dollars")
            full_cost.append(cost)

        print(
            f"Total cost is {sum(full_cost)} dollars\n"
            "See you again!\n"
        )
        # *** ----- ***

        client.money -= min_shop_price
        print(
            f"{client.name} rides home\n"
            f"{client.name} now has {round(client.money, 2)} dollars\n"
        )
