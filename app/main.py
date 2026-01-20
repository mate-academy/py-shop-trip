import json

from app.shop import Shop, ProductShop, ProductCart
from app.customer import Customer
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        content = json.load(config)

    price, from_customers, from_shops = content
    fuel_price = content[price]

    shops = []
    for shop in content[from_shops]:
        shops.append(
            Shop(
                shop["name"],
                shop["location"],
                [ProductShop(name, price) for name, price
                 in shop["products"].items()]
            )
        )

    customers = []
    for customer in content[from_customers]:
        customers.append(
            Customer(
                customer["name"],
                [ProductCart(name, quantity) for name, quantity
                 in customer["product_cart"].items()],
                customer["location"],
                customer["money"],
                Car(**customer["car"])
            )
        )

    for customer in customers:
        best_shop = customer.choose_trip(shops, fuel_price)
        if best_shop:
            customer.go_to_the_shop(best_shop)


if __name__ == "__main__":
    shop_trip()
