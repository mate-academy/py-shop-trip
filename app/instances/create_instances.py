from app.instances.customer import Customer
from app.instances.shop import Shop


def transform_json_to_instances(data: dict) -> dict:
    processed_data = {}

    for key, value in data.items():
        if key == "FUEL_PRICE":
            processed_data["FUEL_PRICE"] = value
        if key == "customers":
            processed_data["customers"] = create_customer_instances(value)
        if key == "shops":
            processed_data["shops"] = create_shop_instances(value)

    return processed_data


def create_customer_instances(customers_list: list) -> list:
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


def create_shop_instances(shops_list: list) -> list:
    return [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
        for shop in shops_list
    ]
