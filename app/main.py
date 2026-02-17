from app.customer import Customer
from app.car import Car


def shop_trip() -> None:
    import json
    import os
    from app.shop import Shop
    base_path = os.path.dirname(__file__)
    config_path = os.path.join(base_path, "config.json")
    with open(config_path, "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    all_shops = []
    for shop_data in data["shops"]:
        new_shop = Shop(
            name=shop_data["name"],
            location=shop_data["location"],
            products=shop_data["products"]
        )
        all_shops.append(new_shop)

    for cust_data in data["customers"]:
        customer_car = Car(
            brand=cust_data["car"]["brand"],
            fuel_consumption=cust_data["car"]["fuel_consumption"]
        )

        customer = Customer(
            name=cust_data["name"],
            product_cart=cust_data["product_cart"],
            location=cust_data["location"],
            money=cust_data["money"],
            car=customer_car
        )
        print(f"{customer.name} has {customer.money} dollars")
        customer.choose_shop(all_shops, fuel_price)
