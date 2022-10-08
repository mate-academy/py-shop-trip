from app.shop import Shop
from app.customer import Customer
from app.car import Car
import json


def shop_trip() -> None:
    with open("app/config.json") as file:
        content = json.load(file)
        for customer in content["customers"]:
            customer_obj = Customer(customer["name"], customer["money"])
            shop_obj = Shop(customer["product_cart"], content["shops"])
            car_obj = Car(
                content["FUEL_PRICE"],
                customer["car"]["fuel_consumption"],
                customer["name"]
            )
            customer_obj.print_money()
            distance_to_shops = customer_obj.distance_calculation(
                customer["location"], content["shops"])
            cost_of_purchases = shop_obj.purchase_cost()
            most_profitable_trip = \
                car_obj.trip_cost(distance_to_shops, cost_of_purchases)
            can_make_a_trip = customer_obj.can_make_a_trip(most_profitable_trip)

            if can_make_a_trip:
                shop_obj.purchase_receipt(customer["name"],
                                          customer["product_cart"],
                                          most_profitable_trip)
                customer_obj.return_home(most_profitable_trip)
