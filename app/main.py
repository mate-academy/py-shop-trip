from app.customer import Customer
from app.shop import Shop
from app.car import Car

import json


def shop_trip() -> None:
    with open("app/config.json", "r") as read_file:
        data = json.load(read_file)
        fuel_price = data["FUEL_PRICE"]
        customers = data["customers"]
        shops = data["shops"]

        for customer in customers:
            Customer.load_from_dict(customer)

            customer_car = Car(
                fuel_price,
                Customer.car["fuel_consumption"],
                Customer.location
            )

            shops_and_trip_cost = {}
            shops_cost = {}

            print(f"{Customer.name} has {Customer.money} dollars")
            for shop_data in shops:
                shop = Shop(
                    shop_data["name"],
                    shop_data["location"],
                    shop_data["products"]
                )

                shops_cost[shop.shop_name] \
                    = shop.calculate_product(Customer.product_cart)

                trip_cost = shop.sum_of_products(shops_cost[shop.shop_name]) \
                    + customer_car.calculate_distance(shop.shop_location)

                shops_and_trip_cost[shop.shop_name] = round(trip_cost, 2)

                print(f"{Customer.name}'s trip to the "
                      f"{shop.shop_name} costs {round(trip_cost, 2)}")

            cheapest_shop = \
                Customer.cheapest_trip(shops_and_trip_cost)

            if shops_and_trip_cost[cheapest_shop] > Customer.money:
                print(f"{Customer.name} doesn't have enough money "
                      f"to make purchase in any shop")
                continue

            print(f"{Customer.name} rides to {cheapest_shop}\n")

            ideal_shop = shops_cost[cheapest_shop]
            Customer.info_output(
                Customer,
                ideal_shop,
                Shop.sum_of_products(ideal_shop)
            )
            spend_money = shops_and_trip_cost[cheapest_shop]
            print(f"{Customer.name} rides home\n{Customer.name}"
                  f" now has {Customer.money - spend_money} dollars\n")
