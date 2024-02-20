import json
import math

from app.customer import Customer
from app.car import Car
from app.shop import Shop
from app.trip import Trip


def shop_trip() -> None:
    customer_instances = []
    shop_instances = []
    with open("app/config.json", "rb") as config:
        data_config = dict(json.load(config))
        Car.fuel_price = data_config["FUEL_PRICE"]

        for customer in data_config.get("customers"):
            car = Car(
                brand=customer["car"]["brand"],
                fuel_consumption=customer["car"]["fuel_consumption"]
            )
            customer_instance = Customer(
                name=customer["name"],
                product_cart=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=car
            )
            customer_instances.append(customer_instance)

        for shop in data_config.get("shops"):
            shop_instance = Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )
            shop_instances.append(shop_instance)

    for customer in customer_instances:
        trip_instances = []

        for shop in shop_instances:
            trip_distance = math.sqrt(
                (shop.location[0] - customer.location[0]) ** 2
                + (shop.location[1] - customer.location[1]) ** 2
            )

            trip_price = (
                (
                    customer.car.fuel_consumption
                    * customer.car.fuel_price
                    * trip_distance / 100
                ) * 2
            )
            total_milk_cost = (
                customer.product_cart["milk"] * shop.products["milk"]
            )
            total_bread_cost = (
                customer.product_cart["bread"] * shop.products["bread"]
            )
            total_butter_cost = (
                customer.product_cart["butter"] * shop.products["butter"]
            )
            trip_instances.append(
                Trip(
                    shop_name=shop.name,
                    trip_price=trip_price,
                    total_milk_cost=total_milk_cost,
                    total_bread_cost=total_bread_cost,
                    total_butter_cost=total_butter_cost
                )
            )

        if not Customer.customer_chose_shop(
            customer=customer,
            trip_instances=trip_instances
        ):
            continue

        Shop.shop_receipt(
            customer=customer,
            trip_instances=trip_instances
        )

        Customer.customer_rides_home(
            customer=customer,
            trip_instances=trip_instances
        )
