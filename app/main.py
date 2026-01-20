import json
from shop import Shop
from customer import Customer
import datetime
from math import sqrt


def shop_trip() -> None:
    with open("app/config.json") as file:
        content = json.load(file)
        fuel_price = content["FUEL_PRICE"]
        for customer in content["customers"]:
            _customer = Customer(customer)
            print(f"{_customer.name} has {_customer.money} dollars")

            cheapest_trip = {}
            for shop_info in content["shops"]:
                cur_shop = Shop(shop_info)

                products_price = sum(
                    [
                        product[1] * cur_shop.shop_prod[product[0]]
                        for product in _customer.prod.items()
                    ]
                )

                distance = sqrt(
                    (
                        _customer.location[0] - cur_shop.location[0]
                    ) ** 2
                    + (
                        _customer.location[1] - cur_shop.location[1]
                    ) ** 2
                )

                fuel_price_to_shop = (
                    distance * fuel_price
                    * _customer.car.fuel_consumption / 100
                ) * 2

                total_price = round(products_price + fuel_price_to_shop, 2)
                print(
                    f"{_customer.name}'s trip to the "
                    f"{cur_shop.name} costs {total_price}"
                )
                cur_shop.prod_price = products_price
                cheapest_trip[total_price] = cur_shop

            if _customer.money - min(cheapest_trip.keys()) < 0:
                print(
                    f"{_customer.name} doesn't have enough money "
                    f"to make a purchase in any shop"
                )
            else:
                cheapest_shop = cheapest_trip[min(cheapest_trip.keys())]
                first_location = _customer.location
                _customer.location = cheapest_shop.location
                now = datetime.datetime.now()
                print(f"{_customer.name} rides to {cheapest_shop.name}\n")
                print(f"Date: {now.strftime('%d/%m/%Y %H:%M:%S')}")
                print(f"Thanks, {_customer.name}, for your purchase!")
                print("You have bought: ")
                for prod, num in _customer.prod.items():
                    print(f"{num} {prod}s "
                          f"for {cheapest_shop.shop_prod[prod] * num} dollars")

                print(f"Total cost is {cheapest_shop.prod_price} dollars")
                print("See you again!\n")
                print(f"{_customer.name} rides home")
                print(f"{_customer.name} now has "
                      f"{_customer.money - min(cheapest_trip.keys())} "
                      f"dollars\n")

                _customer.location = first_location
