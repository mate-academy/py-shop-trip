import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:

    with open("app/config.json", "r") as file:

        data = json.load(file)
        fuel_price = data["FUEL_PRICE"]
        customers = data["customers"]

        customers_instances = []
        for customer in customers:
            cus = Customer(customer["name"],
                           customer["product_cart"],
                           customer["location"],
                           customer["money"],
                           Car(customer["car"]["brand"],
                               customer["car"]["fuel_consumption"]
                               ))

            customers_instances.append(cus)

        shops = data["shops"]
        shop_instances = [
            Shop(shop["name"],
                 shop["location"],
                 shop["products"]
                 ) for shop in shops
        ]

        for customer in customers_instances:

            customer.money_start()

            shops_cost = {}
            for shop in shop_instances:
                products_cost = shop.products_cost(customer)
                fuel_cost = customer.car.fuel_cost(shop.distance(customer),
                                                   fuel_price)
                trip_cost = round(products_cost + fuel_cost * 2, 2)

                print(f"{customer.name}'s trip to the "
                      f"{shop.name} costs {trip_cost}")

                shops_cost.update({trip_cost: shop})
                min_shop = shops_cost[min(shops_cost)]

            if customer.money >= min(shops_cost):
                min_shop.ride_to_shop(customer)
                min_shop.print_receipt(customer)
                customer.ride_to_home()
                customer.money -= min(shops_cost)
                customer.money_end()

            else:
                print(f"{customer.name} doesn't have enough "
                      f"money to make a purchase in any shop")