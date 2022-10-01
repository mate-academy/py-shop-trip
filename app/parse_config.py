from .classes.places import Shop
from .classes.people import Customer
from .classes.transport import Car


def parse_config(config: dict) -> tuple[list[Customer], list[Shop], int]:
    customers = [
        Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                customer["car"]["brand"], customer["car"]["fuel_consumption"]
            ),
        )
        for customer in config["customers"]
    ]

    shops = [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"],
        )
        for shop in config["shops"]
    ]

    fuel_price = config["FUEL_PRICE"]

    return customers, shops, fuel_price
