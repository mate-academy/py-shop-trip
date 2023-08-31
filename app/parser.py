import json

from app.customer import Customer
from app.shop import Shop


class Parser:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def parse_customers(self) -> list["Customer"]:
        with open(self.filepath, "r") as f:
            data = json.load(f)
            customers_data = data.get("customers")
            customers = []
            for customer_dict in customers_data:
                customer = Customer(
                    name=customer_dict["name"],
                    product_cart=customer_dict["product_cart"],
                    location=customer_dict["location"],
                    money=customer_dict["money"],
                    car=customer_dict["car"],
                )
                customers.append(customer)
            Customer.fuel_price = data.get("FUEL_PRICE")
            return customers

    def parse_shops(self) -> list["Shop"]:
        with open(self.filepath, "r") as f:
            data = json.load(f)
            shops_data = data.get("shops")
            shops = []
            for shop_dict in shops_data:
                shop = Shop(
                    name=shop_dict["name"],
                    location=shop_dict["location"],
                    products=shop_dict["products"],
                )
                shops.append(shop)
            return shops
