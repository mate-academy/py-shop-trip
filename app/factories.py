from app.customer import Customer
from app.shop import Shop
from app.types.types import CustomerData, ShopData


def create_customers(customers: list[CustomerData]) -> list[Customer]:
    return [
        Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=(
                int(customer["location"][0]),
                int(customer["location"][1])
            ),
            money=customer["money"],
            car=customer["car"]
        )
        for customer in customers
    ]


def create_shops(shops: list[ShopData]) -> list[Shop]:
    return [
        Shop(
            name=shop["name"],
            location=(
                int(shop["location"][0]),
                int(shop["location"][1])
            ),
            products=shop["products"]
        )
        for shop in shops
    ]
