import json

with open("/Users/bythewaters/py-shop-trip/app/config.json", "r") as config:
    info_customer = json.load(config)


class Info:
    def __init__(self, info: dict = info_customer) -> None:
        self.info = info

    def names_customers(self) -> list:
        return [
            name["name"] for name in self.info["customers"]
        ]

    def cars_customer(self) -> dict:
        return {
            car["name"]: car["car"]["fuel_consumption"]
            for car in self.info["customers"]
        }

    def shops_location(self) -> dict:
        return {
            shop["name"]: shop["location"]
            for shop in self.info["shops"]
        }

    def customer_location(self) -> dict:
        return {
            customer["name"]: customer["location"]
            for customer in self.info["customers"]
        }

    def customer_product_cart(self) -> dict:
        return {
            customer_product["name"]: customer_product["product_cart"]
            for customer_product in self.info["customers"]
        }

    def shops_price(self) -> dict:
        return {
            shop_price["name"]: shop_price["products"]
            for shop_price in self.info["shops"]
        }
