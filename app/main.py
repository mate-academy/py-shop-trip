import json
from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)
    fuel_price = data.get("FUEL_PRICE")

    customers = []
    customers_data = data.get("customers")
    for customer in customers_data:
        person = Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(customer["car"]["brand"], customer["car"]["fuel_consumption"])
        )
        customers.append(person)

    shops_data = data.get("shops")
    shops = [Shop(**shop) for shop in shops_data]
    for customer in customers:
        customer.print_trip(fuel_price, shops)
