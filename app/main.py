from app.shop import Shop
from app.customer import Customer
import datetime
import json
import math


def shop_trip() -> None:
    with open("config.json", "r") as file:
        json_dict = json.load(file)
    list_customers = [Customer(json_dict["customers"][i])
                      for i in range(len(json_dict["customers"]))]
    list_shops = [Shop(json_dict["shops"][i])
                  for i in range(len(json_dict["shops"]))]
    for customer in list_customers:
        dict_shops = {}
        print(f"{customer.name} has {customer.money} dollars")
        for shop in list_shops:
            way = (math.sqrt(((shop.location[0] - customer.location[0])**2
                             + (shop.location[1] - customer.location[1])**2))
                   * json_dict["FUEL_PRICE"]
                   * (customer.car.fuel_consumption) / 100)
            sum_products = sum([shop.products[product]
                                * customer.product_cart[product]
                                for product in customer.product_cart])
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
            for product in customer.product_cart:
                amount_of_product = customer.product_cart[product]
                price_for_product = customer_choice.products[product]
                if (price_for_product * amount_of_product
                        == int(customer_choice.products[product]
                               * amount_of_product)):
                    print(f"{amount_of_product} {product}s for "
                          f"{int((price_for_product * amount_of_product))}"
                          f" dollars")
                else:
                    print(f"{amount_of_product} {product}s "
                          f"for {price_for_product * amount_of_product}"
                          f" dollars")
                sum_products += price_for_product * amount_of_product

            print(f"Total cost is {sum_products} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {round(customer.money, 2)}"
                  f" dollars\n")
