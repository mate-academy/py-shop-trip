import json
from shop import Shop
from customer import Customer
import datetime
from math import sqrt


def shop_trip() -> None:
    with open("app/config.json") as file:
        content = json.load(file)
        fuel_price = content["FUEL_PRICE"]
        customers = content["customers"]
        for customer in customers:
            _customer = Customer()
            _customer.name = customer["name"]
            _customer.prod = customer["product_cart"]
            _customer.location = customer["location"]
            _customer.money = customer["money"]
            _customer.car = customer["car"]
            print(f"{_customer.name} has {_customer.money} dollars")

            shops = content["shops"]
            cheapest_trip = {}
            for shop in shops:
                cur_shop = Shop()
                cur_shop.name = shop["name"]
                cur_shop.location = shop["location"]
                cur_shop.shop_prod = shop["products"]

                milk, bread, butter = [
                    _customer.prod["milk"] * cur_shop.shop_prod["milk"],
                    _customer.prod["bread"] * cur_shop.shop_prod["bread"],
                    _customer.prod["butter"] * cur_shop.shop_prod["butter"],

                ]

                products_price = sum([milk, bread, butter])

                distance = sqrt(
                    (_customer.location[0] - cur_shop.location[0]) ** 2
                    + (_customer.location[1] - cur_shop.location[1]) ** 2)

                fuel_price_to_shop = (distance
                                      * fuel_price
                                      * _customer.car["fuel_consumption"] / 100
                                      ) * 2

                total_price = round(products_price + fuel_price_to_shop, 2)
                print(
                    f"{_customer.name}'s trip to the "
                    f"{cur_shop.name} costs {total_price}"
                )

                cheapest_trip[total_price] = (
                    cur_shop.name, milk, bread, butter, cur_shop.location
                )

            if _customer.money - min(cheapest_trip.keys()) < 0:
                print(
                    f"{_customer.name} doesn't have enough money "
                    f"to make a purchase in any shop"
                )
            else:
                cheapest_shop = cheapest_trip[min(cheapest_trip.keys())]
                print(f"{_customer.name} rides to {cheapest_shop[0]}\n")
                first_location = _customer.location
                _customer.location = cheapest_shop[4]
                now = datetime.datetime.now()
                print(f"Date: {now.strftime('%d/%m/%Y %H:%M:%S')}")
                print(f"Thanks, {_customer.name}, for your purchase!")
                print(
                    f"You have bought: \n"
                    f"{_customer.prod['milk']} milks "
                    f"for {cheapest_shop[1]} dollars\n"
                    f"{_customer.prod['bread']} breads "
                    f"for {cheapest_shop[2]} dollars\n"
                    f"{_customer.prod['butter']} butters "
                    f"for {cheapest_shop[3]} dollars"
                )
                print(f"Total cost is {sum(cheapest_shop[1:-1])} dollars")
                print("See you again!\n")
                print(f"{_customer.name} rides home")
                _customer.location = first_location
                print(f"{_customer.name} now has "
                      f"{_customer.money - min(cheapest_trip.keys())} "
                      f"dollars\n")
