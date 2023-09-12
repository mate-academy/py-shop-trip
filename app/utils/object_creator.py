from app.customer import Customer
from app.shop import Shop


def create_customers(customers_data: dict) -> list:
    customers_objects = []
    for customer_data in customers_data:
        customer = Customer(customer_data)
        customers_objects.append(customer)
    return customers_objects


def create_shops(shops_data: dict) -> list:
    shops_objects = []
    for shop_data in shops_data:
        shop = Shop(shop_data)
        shops_objects.append(shop)
    return shops_objects
