from app.shop import Shop
from app.customer import Customer
import datetime
import json
import math


def shop_trip() -> None:
    with open("config.json", "r") as file:
        json_dict = json.load(file)
    costumers = [Customer(i) for i in json_dict["customers"]]
    shops_list = [Shop(i) for i in json_dict["shops"]]
    for customer in costumers:
        dict_shops = {}
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops_list:
            way = (math.sqrt(((shop.location[0] - customer.location[0])**2
                             + (shop.location[1] - customer.location[1])**2))
                   * json_dict["FUEL_PRICE"]
                   * (customer.car.fuel_consumption) / 100)
            sum_products = sum([shop.products[product[0]]
                                * product[1]
                                for product in customer.product_cart.items()])
            whole_trip = 2 * way + sum_products
            dict_shops[shop] = whole_trip
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {round(way*2, 2) + sum_products}")
        if customer.money < min(dict_shops.values()):
            print(f"{customer.name}"
                  f" doesn't have enough money to make a purchase in any shop")
        else:
            customer_choice = min(dict_shops, key=dict_shops.get)
            print(f"{customer.name} rides to {customer_choice.name}")
            print("\nDate: "
                  + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            print(f"Thanks,"
                  f" {customer.name}, for your purchase!\nYou have bought: ")
            sum_products = 0
            customer.money -= min(dict_shops.values())
            for product in customer.product_cart.items():
                amount_of_product = product[1]
                price_for_product = customer_choice.products[product[0]]
                if (price_for_product * amount_of_product
                        == int(customer_choice.products[product[0]]
                               * amount_of_product)):
                    print(f"{amount_of_product} {product[0]}s for "
                          f"{int((price_for_product * amount_of_product))}"
                          f" dollars")
                else:
                    print(f"{amount_of_product} {product[0]}s "
                          f"for {price_for_product * amount_of_product}"
                          f" dollars")
                sum_products += price_for_product * amount_of_product

            print(f"Total cost is {sum_products} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {round(customer.money, 2)}"
                  f" dollars\n")
