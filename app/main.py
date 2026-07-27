import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as source:
        data_source = json.load(source)

    customers = [
        Customer(**customer) for customer in data_source.get("customers")
    ]
    shops = [Shop(**shop) for shop in data_source.get("shops")]
    for customer in customers:
        customer_home = customer.location
        best_price_shop = customer.best_shop_choosing(shops)
        if best_price_shop:
            best_price_shop.purchase_receipt(customer)
            customer.location = customer_home
            customer.shopping_done(best_price_shop)


if __name__ == "__main__":
    shop_trip()
