import json
import datetime
import os
from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    path_file = os.path.abspath(".")
    path_file = os.path.join(path_file, "app", "config.json")
    with open(path_file) as config_file:
        config_data = json.load(config_file)
    fuel_price = config_data["FUEL_PRICE"]
    shop_list = []
    customers_list = []
    for index_shop in range(len(config_data["shops"])):
        shop_list.append(Shop(
            config_data["shops"][index_shop]["name"],
            config_data["shops"][index_shop]["location"],
            config_data["shops"][index_shop]["products"]
        ))
    for index in range(len(config_data["customers"])):
        customers_list.append(Customer(
            config_data["customers"][index]["name"],
            config_data["customers"][index]["product_cart"],
            config_data["customers"][index]["location"],
            config_data["customers"][index]["money"],
            Car(
                config_data["customers"][index]["car"]["brand"],
                config_data["customers"][index]["car"]["fuel_consumption"]
            ),
            []
        ))

    for bayer in customers_list:
        print(f"{bayer.name} has {bayer.money} dollars")
        min_cost = 0
        for shop in shop_list:
            distance = bayer.trac_distance(shop.location)
            trac_cost = round(
                distance * fuel_price * bayer.car.fuel_consumption / 100, 2
            )
            cost_food = shop.cost_food(bayer)
            total_cost = cost_food + trac_cost
            bayer.shop_info.append([total_cost, shop])
            print(f"{bayer.name}'s trip to the {shop.name} costs {total_cost}")
            if min_cost == 0 or total_cost < min_cost:
                min_cost = total_cost
                best_shop = shop
                cost_only_food = min_cost - trac_cost
        if min_cost > bayer.money:
            print(f"{bayer.name} doesn't have enough "
                  f"money to make purchase in any shop")
            continue
        print(f"{bayer.name} rides to {best_shop.name}\n")

        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %I:%M:%S')}")
        print(f"Thanks, {bayer.name}, for you purchase!")
        print("You have bought: ")
        for product in bayer.product_cart.keys():
            how_mach = bayer.product_cart[product]
            print(f"{how_mach} {product}s for "
                  f"{how_mach * best_shop.products[product]} dollars")
        print(f"Total cost is {round(cost_only_food, 2)} dollars")
        print("See you again!\n")
        print(f"{bayer.name} rides home")
        have_money = round(bayer.money - min_cost, 2)
        print(f"{bayer.name} now has {have_money} dollars\n")
