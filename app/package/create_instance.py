from app.customer import Customer
from app.shop import Shop


def create_customer(data: dict) -> Customer:
    return Customer(name=data["name"],
                    product_cart=data["product_cart"],
                    location=data["location"],
                    money=data["money"],
                    car=data["car"])


def create_shop(data: dict) -> Shop:
    return Shop(name=data["name"],
                location=data["location"],
                products=data["products"])
