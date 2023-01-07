import json

from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as data_in:
        data_from_file = json.load(data_in)
        fuel_coast = Car(fuel_price=data_from_file["FUEL_PRICE"])
        customers = [
            Customer(customer) for customer in data_from_file["customers"]
        ]
        shops = [Shop(shop) for shop in data_from_file["shops"]]

        for customer in customers:
            customer_home = customer.location.copy()
            print(f"{customer.name} has {customer.money} dollars")
            dict_shop_and_coast = {}
            for shop in shops:
                coast_to_shop = customer.coast_of_trip_to_shop(
                    shop,
                    fuel_coast
                )
                dict_shop_and_coast[coast_to_shop] = shop
                print(f"{customer.name}'s trip to "
                      f"the {shop.name} costs {coast_to_shop}")

            list_keys = [key for key in dict_shop_and_coast]
            minimal_coast = list_keys[0]
            for key in dict_shop_and_coast:
                if key < minimal_coast:
                    minimal_coast = key

            if customer.money >= minimal_coast:
                print(f"{customer.name} rides to "
                      f"{dict_shop_and_coast[minimal_coast].name}")
                print()
                customer.location = dict_shop_and_coast[minimal_coast].location
                print("Date: 04/01/2021 12:33:41")
                print(f"Thanks, {customer.name}, for you purchase!")
                print("You have bought: ")
                total_coast_of_products = 0
                for product in customer.product_cart:
                    coast_of_product = customer.product_cart[product] * \
                        dict_shop_and_coast[minimal_coast].products[product]
                    print(
                        f"{customer.product_cart[product]} {product}s for"
                        f" {coast_of_product} dollars"
                    )
                    total_coast_of_products += \
                        customer.product_cart[product] * \
                        dict_shop_and_coast[minimal_coast].products[product]
                print(f"Total cost is {total_coast_of_products} dollars")
                customer.money -= minimal_coast
                print("See you again!")
                print()
                print(f"{customer.name} rides home")
                customer.location = customer_home
                print(f"{customer.name} now has {customer.money} dollars")
                print()
            else:
                print(f"{customer.name} doesn't have enough"
                      f" money to make purchase in any shop")
