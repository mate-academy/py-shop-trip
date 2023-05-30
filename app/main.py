from json import load

from app.calculate import can_afford_trip
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = load(file)
    fuel_price = data.get("FUEL_PRICE", 0)
    customers = []
    for customer in data.get("customers", []):
        customers.append(
            Customer(
                customer.get("name"),
                customer.get("product_cart"),
                customer.get("location"),
                customer.get("money"),
                customer.get("car"),
            )
        )
    shops = []
    for shop in data.get("shops", []):
        shops.append(
            Shop(
                shop.get("name"),
                shop.get("location"),
                shop.get("products")
            )
        )
    for customer in customers:
        can_afford_trip(customer, shops, fuel_price)
