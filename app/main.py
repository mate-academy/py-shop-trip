import json
from app.customer import Customer
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json") as file:
        trip_data = json.load(file)
    customers = trip_data["customers"]
    stores = trip_data["shops"]
    for customer in customers:
        customer_instance = Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"]
        )
        car = Car(
            brand=customer["car"]["brand"],
            fuel_consumption=customer["car"]["fuel_consumption"]
        )
        customer_instance.amount_of_money_at_start()
        customer_instance.cost_of_all_trips(
            stores=stores,
            fuel_consumption=car.fuel_consumption,
            fuel_price=trip_data["FUEL_PRICE"]
        )
        customer_instance.choose_the_shop()
