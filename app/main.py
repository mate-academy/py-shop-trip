import json

from app.shop import Shop
from app.customer import Customer
from app.car import Car


def shop_trip() -> None:
    with (open("app/config.json", "r") as config):
        json_dict = json.load(config)

        fuel_price = json_dict["FUEL_PRICE"]

        shops = [Shop(shop["name"],
                      shop["location"],
                      shop["products"])
                 for shop in json_dict["shops"]]
        customers = [Customer(customer["name"],
                              customer["location"],
                              customer["money"],
                              Car(customer["car"]["brand"],
                                  customer["car"]["fuel_consumption"]),
                              customer["product_cart"]
                              ) for customer in json_dict["customers"]]

        for customer in customers:
            print(f"{customer.name} has {customer.money} dollars")
            price_to_buy = customer.money
            shop_to = None

            for shop in shops:
                cost = shop.get_price_of_products(
                    customer.product_cart) + customer.car.get_way_cost(
                    fuel_price, shop.location, customer.location) * 2

                print(f"{customer.name}\'s trip to "
                      f"the {shop.name} costs {round(cost, 2)}")

                if price_to_buy >= cost:
                    price_to_buy = cost
                    shop_to = shop

            if shop_to is not None:
                print(f"{customer.name} rides to {shop_to.name}")
                customer.location = shop.location

                shop_to.bought(customer.name, customer.product_cart)
                print(f"{customer.name} rides home")
                customer.money -= price_to_buy
                print(f"{customer.name} now has"
                      f" {round(customer.money, 2)} dollars\n")

            else:
                print(f"{customer.name} doesn\'t have "
                      f"enough money to make a purchase in any shop")
