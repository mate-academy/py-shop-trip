from app.customer import Customer
from app.shop import Shop
from app.car import Car


def create_list_of_customers_objects(customers_dict: dict) -> list[Customer]:
    return [
        Customer(
            name=customer.get("name"),
            product_cart=customer.get("product_cart"),
            location=customer.get("location"),
            money=customer.get("money"),
            car=create_car_object_from_dict(customer.get("car")),
        )
        for customer in customers_dict
    ]


def create_car_object_from_dict(car_dict: dict) -> Car:
    return Car(car_dict.get("brand"), car_dict.get("fuel_consumption"))


def create_list_of_shops_objects(shops_dict: dict) -> list:
    result = []

    for shop in shops_dict:
        result.append(
            Shop(
                shop.get("name"), shop.get("location"), shop.get("products")
            )
        )
    return result
