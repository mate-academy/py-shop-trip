import json

from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config_dict = json.load(file)

    price_for_liter = config_dict["FUEL_PRICE"]

    customers = []
    for customer in config_dict["customers"]:
        customers.append(Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]
            )
        ))

    shops = [Shop(
        name=shop["name"],
        location=shop["location"],
        products=shop["products"]
    ) for shop in config_dict["shops"]]

    for customer in customers:
        cheapest_shop = customer.choose_shop(price_for_liter, shops)
        if cheapest_shop:
            cheapest_shop.print_purchase_receipt(customer)
            customer.return_home()


if __name__ == "__main__":
    shop_trip()
