import json
from os import path

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    _path = path.join("app", "config.json")
    with open(_path, "r") as file:
        data_from_file = json.load(file)
        try:

            fuel_price = data_from_file["FUEL_PRICE"]

        except KeyError as e:
            print(e, "not exist")

        try:
            customers_list = [
                Customer.create_customer(customer)
                for customer in data_from_file["customers"]
            ]
        except KeyError as e:
            print(e, "not exist")

        try:
            shops_list = [
                Shop.create_shop(shop)
                for shop in data_from_file["shops"]
            ]
        except KeyError as e:
            print(e, "not exist")

    for customer in customers_list:
        calculate_cost_for_every_shop = {
            shop: shop.calculate_total_product_cost(customer)
            + round(
                customer.car.calculate_cost_one_way(
                    fuel_price, customer.location, shop.location
                )
                * 2,
                2,
            )
            for shop in shops_list
        }

        print(f"{customer.name} has {customer.money} dollars")
        for shop, product_cost in calculate_cost_for_every_shop.items():
            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {product_cost}"
            )

        min_cost_shop = min(
            calculate_cost_for_every_shop.items(), key=lambda item: item[1]
        )
        if min_cost_shop[1] < customer.money:
            print(f"{customer.name} rides to {min_cost_shop[0].name}\n")
            print("Date: 04/01/2021 12:33:41")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            for product, quantity in customer.products.items():
                price = quantity * min_cost_shop[0].products[product]
                formate_price = f"{int(price)}" \
                    if price == int(price) else f"{price}"
                print(f"{quantity} {product + 's'} "
                      f"for {formate_price} dollars")
            print(
                f"Total cost is "
                f"{min_cost_shop[0].calculate_total_product_cost(customer)} "
                f"dollars"
            )
            print("See you again!\n")
            print(f"{customer.name} rides home")
            customer.money -= min_cost_shop[1]
            print(f"{customer.name} now has {customer.money} dollars\n")

        else:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )


shop_trip()
