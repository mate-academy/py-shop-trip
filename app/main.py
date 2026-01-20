import json
from app.print import (
    get_shopping_options, get_receipt, get_home, not_enough_money)
from app.work_with_data import (
    make_car_instance,
    make_list_of_shop_instances,
    make_list_of_customer_instances)


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        source_dict = json.load(f)

    fuel_price = source_dict["FUEL_PRICE"]
    customers = make_list_of_customer_instances(source_dict)
    shops = make_list_of_shop_instances(source_dict)
    for customer in customers:
        car = make_car_instance(customer)

        print(f"{customer.name} has {customer.money} dollars")

        shop_dict = {}
        for shop in shops:
            shop_dict[shop] = car.get_total_trip_cost(
                customer, shop, fuel_price)
            get_shopping_options(car, customer, shop, fuel_price)

        best_shop = min(shop_dict, key=shop_dict.get)
        if customer.money >= shop_dict[best_shop]:
            get_receipt(customer, best_shop)
            get_home(car, customer, best_shop, fuel_price)
        else:
            not_enough_money(customer)
