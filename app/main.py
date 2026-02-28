import json

from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json", "rb") as json_file:
        data = json.load(json_file)
    list_customers = []
    list_car = []
    for one_customer in data["customers"]:
        list_customers.append(Customer(one_customer["name"],
                                       one_customer["product_cart"],
                                       one_customer["location"],
                                       one_customer["money"],
                                       one_customer["car"]
                                       ["fuel_consumption"]))
        list_car.append(Car(one_customer["name"],
                            one_customer["car"]["fuel_consumption"]))
    list_shop = []
    for shop in data["shops"]:
        list_shop.append(Shop(shop["name"],
                              shop["location"],
                              shop["products"]))
    for index_for_car, customer in enumerate(list_customers):
        full_price = []
        print(f"{customer.name} has {customer.money} dollars")
        for shop in list_shop:
            this_shop_price_drive = (
                list_car[index_for_car].
                calculate_round_trip_fuel_cost(
                    customer.location, shop.location,
                    data["FUEL_PRICE"])
            )
            this_shop_price = shop.purchase(customer.product_cart)
            sum_total = round(sum(this_shop_price.values())
                              + this_shop_price_drive, 2)
            print(f"{customer.name}\'s trip to the {shop.name} "
                  f"costs {sum_total:.2f}")
            full_price.append(sum_total)
        min_price = min(full_price)
        cheaper_store = list_shop[full_price.index(min_price)]
        if customer.money - min_price >= 0:
            temp, customer.location = customer.location, cheaper_store.location
            customer.make_purchase(cheaper_store)
            print(f"{customer.name} rides home")
            customer.location = temp
            customer.money -= min_price
            print(f"{customer.name} now has {customer.money:.2f} dollars\n")
        else:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
