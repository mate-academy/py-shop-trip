from app.customer import Customer
from app.car import Car
from app.shop import Shop
import json


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        config_data = json.load(config_file)
        fuel_price = config_data["FUEL_PRICE"]
        customers = config_data["customers"]

        customer_data = [
            Customer
            (
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car
                (
                    customer["car"]["brand"],
                    customer["car"]["fuel_consumption"]
                )
            )
            for customer in customers
        ]

        shops = config_data["shops"]
        shop_data = [
            Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
            for shop in shops
        ]

        for customer in customer_data:
            customer.primary_amount_of_money()

            shops_cost = {}
            for shop in shop_data:
                products_cost = shop.calculate_purchase_cost(customer)
                fuel_cost = customer.car.calculate_fuel_cost(
                    shop.calculate_distance_to_customer(customer), fuel_price
                )
                trip_cost = round(products_cost + fuel_cost * 2, 2)

                print(f"{customer.name}'s trip to the "
                      f"{shop.name} costs {trip_cost}")

                shops_cost.update({trip_cost: shop})
                min_shop = shops_cost[min(shops_cost)]

            if customer.money >= min(shops_cost):
                min_shop.print_rides_to_shop(customer)
                min_shop.print_receipt(customer)
                customer.print_rides_home()
                customer.money -= min(shops_cost)
                customer.final_amount_of_money()

            else:
                print(f"{customer.name} doesn't have enough "
                      f"money to make a purchase in any shop")
