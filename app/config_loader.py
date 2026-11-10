from pathlib import Path
from json import load

from app.models.customer.customer import Customer
from app.models.shop.shop import Shop
from app.models.customer.car import Car


class ConfigLoader:
    def __init__(self) -> None:
        config_path = Path(__file__).parent / "config.json"
        self.customers: list[Customer]
        self.shops: list[Shop]
        self.car: list[Car]
        self.fuel_price: float

        with config_path.open("r", encoding="utf-8") as file_in:
            json_data = load(file_in)

        self.fuel_price = json_data["FUEL_PRICE"]

        self.customers = [
            Customer(
                name=c["name"],
                product_cart=c["product_cart"],
                location=c["location"],
                money=c["money"],
                car=Car(
                    brand=c["car"]["brand"],
                    fuel_consumption=c["car"]["fuel_consumption"]
                )
            )
            for c in json_data["customers"]
        ]

        self.shops = [
            Shop(
                name=s["name"],
                location=s["location"],
                products=s["products"],
            )
            for s in json_data["shops"]
        ]
