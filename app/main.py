import json
from os import path

from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    project_dir = path.dirname(path.dirname(path.abspath(__file__)))
    config_file = path.join(project_dir, "app/config.json")
    with open(config_file, "r") as file:
        info_in_file = json.load(file)
    itterable = 0
    shop_list = []
    for shop in info_in_file["shops"]:
        shop_list.append(Shop(
            shop["name"],
            shop["location"],
            shop["products"])
        )
    for human in info_in_file["customers"]:
        customer = Customer(
            human["name"],
            human["product_cart"],
            human["location"],
            human["money"],
            human["car"]
        )

        print(f"{customer.name} has {customer.money} dollars")
        customer_info = customer.customer_trip_to_shop(shop_list, info_in_file)
        if customer_info is False:
            break
        car_to_buy = Car(
            customer.car["fuel_consumption"],
            info_in_file["FUEL_PRICE"],
            shop_list[itterable],
            customer.location
        )
        temper_res = shop_list[itterable].get_spent_money(
            customer,
            car_to_buy.get_fuel_cost(),
            False)
        shop_list[itterable].get_price_product(customer)
        print(f"\n{customer.name} rides home")
        print(f"{customer.name} now has "
              f"{round(customer.money - temper_res, 2)} dollars\n")
        itterable += 1
