from app.shop import Shop
from app.customer import Customer
import datetime
import json
import math


def shop_trip() -> None:
    with open("config.json", "r") as file:
        json_dict = json.load(file)
    custumers = [Customer(costumer_inf)
                 for costumer_inf in json_dict["customers"]]
    shops = [Shop(shop_inf) for shop_inf in json_dict["shops"]]
    for customer in custumers:
        home_location = customer.location.copy()
        dict_shops = {}
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
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
            customer.location = customer_choice.location
            print(f"{customer.name} rides to {customer_choice.name}\n"
                  f"\nDate: "
                  f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
                  f"\nThanks, "
                  f"{customer.name}, for your purchase!\nYou have bought: ")
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
            customer.location = home_location
            print(f"Total cost is {sum_products} dollars\n"
                  f"See you again!\n"
                  f"\n{customer.name} rides home"
                  f"\n{customer.name} now has {round(customer.money, 2)}"
                  f" dollars\n")
