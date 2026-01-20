from app.instances.customer import Customer
from app.instances.shop import Shop


def transform_json_to_instances(data: dict) -> dict:
    return {
        "FUEL_PRICE": data["FUEL_PRICE"],
        "customers": create_customer_instances(data["customers"]),
        "shops": create_shop_instances(data["shops"])
    }


def create_customer_instances(customers_list: list[dict]) -> list[Customer]:
    return [
        Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            home_location=customer["location"],
            money=customer["money"],
            car=customer["car"]
        )
        for customer in customers_list
    ]


def create_shop_instances(shops_list: list[dict]) -> list[Shop]:
    return [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
        for shop in shops_list
    ]
