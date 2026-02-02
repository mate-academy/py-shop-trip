import json
from decimal import Decimal

from app.car import Car
from app.customer import Customer
from app.shop import Shop
from app.products import Products


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    for customer in data["customers"]:
        Customer(customer["name"],
                 Products(Decimal(str(customer["product_cart"]["milk"])),
                          Decimal(str(customer["product_cart"]["bread"])),
                          Decimal(str(customer["product_cart"]["butter"]))
                          ),
                 customer["location"],
                 Decimal(customer["money"]),
                 Car(customer["car"]["brand"],
                     Decimal(customer["car"]["fuel_consumption"]))
                 )
    Customer.fuel_price = Decimal(data["FUEL_PRICE"])

    for shop in data["shops"]:
        Shop(shop["name"],
             shop["location"],
             Products(Decimal(str(shop["products"]["milk"])),
                      Decimal(str(shop["products"]["bread"])),
                      Decimal(str(shop["products"]["butter"])))
             )

    for customer in Customer.customers:
        shop_to_ride = customer.check_trip_availability()
        if shop_to_ride:
            customer.get_receipt(shop_to_ride)
            customer.arrive_home()
