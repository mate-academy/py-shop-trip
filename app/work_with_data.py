from app.car import Car
from app.customer import Customer
from app.shop import Shop


def make_list_of_customer_instances(customers_dict: dict) -> list:
    customers = [Customer(
        name=customer["name"],
        product_cart=customer["product_cart"],
        location=customer["location"],
        money=customer["money"],
        car=customer["car"]
    ) for customer in customers_dict["customers"]]
    return customers


def make_list_of_shop_instances(shops_dict: dict) -> list:
    shops = [Shop(
        name=shop["name"],
        location=shop["location"],
        products=shop["products"]
    ) for shop in shops_dict["shops"]]
    return shops


def make_car_instance(customer: Customer) -> Car:
    car = Car(
        brand=customer.car["brand"],
        fuel_consumption=customer.car["fuel_consumption"]
    )
    return car
