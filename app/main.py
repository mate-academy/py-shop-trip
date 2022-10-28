import json
from decimal import Decimal
from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json", "r") as file_config:
        data = json.load(file_config)
        fuel_price: Decimal = Decimal(str(data["FUEL_PRICE"]))
        customers_list: list = [
            Customer(
                name=customer["name"],
                product_cart=customer["product_cart"],
                location=customer["location"],
                money=Decimal(f"{customer['money']}"),
                car=Car(brand=customer["car"]["brand"],
                        fuel_consumption=customer["car"]["fuel_consumption"])
            ) for customer in data["customers"]
        ]
        shops_list: list = [
            Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            ) for shop in data["shops"]
        ]

        for customer in customers_list:
            print(f"{customer.name} has {customer.money} dollars")
            profitable_shop = \
                customer.determination_min_trip_cost(shops_list, fuel_price)
            if customer.money < profitable_shop["trip_cost"]:
                print(f"{customer.name} doesn't have enough money "
                      f"to make purchase in any shop")
            else:
                print(f"{customer.name} rides to "
                      f"{profitable_shop['shop'].name}")
                customer.location = profitable_shop["shop"].location
                customer.print_purchase_receipt(profitable_shop["shop"])
                print(f"{customer.name} rides home")
                cost_remainder = customer.money - profitable_shop["trip_cost"]
                print(f"{customer.name} now has {cost_remainder} dollars\n")
