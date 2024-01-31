import json
from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    try:
        with open("app/config.json", "r") as file:
            config = json.load(file)
    except FileNotFoundError:
        print("No Such File!")

    customers_data = config.get("customers")
    customers = [
        Customer(
            name=customer_data.get("name"),
            product_cart=customer_data.get("product_cart"),
            location=customer_data.get("location"),
            money=customer_data.get("money"),
            car=Car(
                brand=customer_data.get("car").get("brand"),
                fuel_consumption=customer_data.get("car").get
                ("fuel_consumption")
            )
        ) for customer_data in customers_data
    ]

    shops_data = config.get("shops")

    shops = [Shop(
        name=shop.get("name"),
        location=shop.get("location"),
        products=shop.get("products")
    ) for shop in shops_data]

    fuel_price = config.get("FUEL_PRICE")

    for customer in customers:
        customer.find_cheapest_shop(shops, fuel_price)


if __name__ == "__main__":
    shop_trip()
