import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)
        for i in data["customers"]:
            customer = Customer(
                i["name"],
                i["product_cart"],
                i["location"],
                i["money"],
                Car(i["car"]["brand"], i["car"]["fuel_consumption"])
            )
            customer.get_money()
            list_of_shops = []
            for shop in data["shops"]:
                shop_instance = Shop(
                    shop["name"], shop["location"], shop["products"])
                list_of_shops.append(
                    customer.trip_to_shop(shop_instance, data["FUEL_PRICE"])
                )
            the_cheapest_shop = min(list_of_shops, key=lambda x: x[0])
            if the_cheapest_shop[0] < customer.money:
                print(f"{customer.name} rides to {the_cheapest_shop[1].name}")
            else:
                print(f"{customer.name} doesn't have enough money "
                      f"to make a purchase in any shop")
                continue
            print("")
            print("Date: 04/01/2021 12:33:41")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            customer.list_of_bought_stuff(the_cheapest_shop[1])
            print("")
            print(f"{customer.name} rides home")
            current_money = customer.money - the_cheapest_shop[0]
            print(f"{customer.name} now has {current_money} dollars")
            print("")
