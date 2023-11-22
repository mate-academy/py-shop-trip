import json
import os
from decimal import Decimal

from app.car import Car
from app.customer import Customer
from app.fuel import Fuel
from app.product import Product
from app.product_cart import ProductCart
from app.shop import Shop


class DataManager:
    PATH = os.path.join(os.path.dirname(__file__), "config.json")

    def __init__(self, filepath: str = PATH) -> None:
        self.filepath = filepath
        self.data = self._get_data_json()

    def _get_data_json(self) -> dict:
        with open(self.filepath, "r") as file:
            return json.load(file)

    def create_customers(self) -> list[Customer]:
        customers = []
        for data_customer in self.data.get("customers", []):
            customer = Customer(
                name=data_customer.get("name"),
                product_cart=ProductCart(
                    data_customer.get("product_cart", [])
                ),
                location=data_customer.get("location"),
                money=data_customer.get("money"),
                car=Car(
                    brand=data_customer.get("car").get("brand"),
                    fuel_consumption=data_customer.get("car").get(
                        "fuel_consumption")
                ),
                fuel=Fuel(price=self.data.get("FUEL_PRICE", 0))
            )
            customers.append(customer)

        return customers

    def create_shops(self) -> list[Shop]:
        shops = []
        for data_shop in self.data.get("shops", []):
            shop = Shop(
                name=data_shop.get("name"),
                location=data_shop.get("location"),
                products=[]
            )

            product_data = data_shop.get("products", [])
            for name_product, price_product in product_data.items():
                product = Product(
                    name=name_product,
                    price=Decimal(str(price_product))
                )
                shop.products.append(product)
            shops.append(shop)
        return shops
