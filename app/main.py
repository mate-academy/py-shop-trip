import datetime
import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as config_file:
        config_info = json.load(config_file)

    customers_list = [Customer(**customer)
                      for customer in config_info["customers"]]
    shop_list = [Shop(**shop) for shop in config_info["shops"]]

    for customer in customers_list:
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shop_list:
            price_for_products_in_shop = (
                customer.product_cart.price_for_all(shop.products))
            shop_total_price = round((customer.location.distance(shop.location)
                                      * config_info["FUEL_PRICE"]
                                      * customer.car.fuel_consumption
                                      / 100 * 2 + price_for_products_in_shop),
                                     2)
            if (not customer.shop_lowest_price
                    or shop_total_price < customer.shop_lowest_price):
                customer.shop_lowest_product_price = price_for_products_in_shop
                customer.shop_lowest_price = shop_total_price
                customer.bargain_shop = shop

            print(f"{customer.name}'s trip "
                  f"to the {shop.name} costs {shop_total_price}")

        if customer.money >= customer.shop_lowest_price:
            customer.money -= customer.shop_lowest_price
            print(f"{customer.name} rides to {customer.bargain_shop.name}\n")
            print("Date:",
                  datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            print(f"{customer.product_cart.milk} milks for "
                  f"{customer.product_cart.price_for_milks(
                      customer.bargain_shop.products)} dollars")
            print(f"{customer.product_cart.bread} breads for "
                  f"{customer.product_cart.price_for_breads(
                      customer.bargain_shop.products)} dollars")
            print(f"{customer.product_cart.butter} butters for "
                  f"{customer.product_cart.price_for_butters(
                      customer.bargain_shop.products)} dollars")
            print(f"Total cost is "
                  f"{customer.shop_lowest_product_price} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
