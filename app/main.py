import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as file_in:
        data = json.load(file_in)
        fuel_price = data["FUEL_PRICE"]
        customer_data = [Customer(customer) for customer in data["customers"]]
        shop_data = [Shop(shop) for shop in data["shops"]]

        for customer in customer_data:
            print(f"{customer.name} has {customer.money} dollars")
            customer.choose_shop(shop_data, fuel_price)
            if customer.choosen_shop:
                customer.choosen_shop.print_receipt(customer)
                print(f"{customer.name} rides home")
                print(f"{customer.name} now "
                      f"has {customer.money - customer.best_price} dollars\n")
            else:
                return
