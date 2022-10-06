from app.customer import Customer
from app.shop import Shop
from app.car import Car

import json


def shop_trip() -> None:
    with open("app/config.json") as file:
        content = json.load(file)

        for customer in content["customers"]:
            customer_instance = Customer(customer["name"], customer["money"])
            shop_instance = Shop(customer["product_cart"], content["shops"])
            car_instance = Car(
                content["FUEL_PRICE"],
                customer["car"]["fuel_consumption"],
                customer["name"]
            )
            customer_instance.money_amount()
            distance_to_shops = customer_instance.distance_calculation(
                customer["location"], content["shops"])
            cost_of_purchases = shop_instance.purchase_cost()
            most_profitable_trip = car_instance.cost_of_the_trip(
                distance_to_shops, cost_of_purchases)
            can_make_a_trip = customer_instance.can_make_a_trip(
                most_profitable_trip)

            if can_make_a_trip:
                shop_instance.purchase_receipt(
                    customer["name"],
                    customer["product_cart"],
                    most_profitable_trip
                )
                customer_instance.homecoming(most_profitable_trip)
