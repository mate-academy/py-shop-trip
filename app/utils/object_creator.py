from app.customer import Customer
from app.shop import Shop


def create_customers(customers_data: dict) -> list:
    return [Customer(customer_data) for customer_data in customers_data]


def create_shops(shops_data: dict) -> list:
    return [Shop(shop_data) for shop_data in shops_data]
