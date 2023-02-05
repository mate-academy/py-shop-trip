import json
from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as shop_trip_file:
        source_dict = json.load(shop_trip_file)

    fuel_price = source_dict["FUEL_PRICE"]
    customers = [
        Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                brand=customer["car"]["brand"],
                fuel_consumption=customer["car"]["fuel_consumption"]
            )
        )
        for customer in source_dict["customers"]
    ]
    shops = [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
        for shop in source_dict["shops"]
    ]

    for customer in customers:
        customer.money_info()

        shop_dict = {}
        for shop in shops:
            total_expenses = customer.car.total_expenses(
                customer,
                shop,
                fuel_price
            )
            shop_dict[shop] = total_expenses
            customer.car.trip_info(customer, shop, fuel_price)

        go_to = min(shop_dict, key=shop_dict.get)
        if shop_dict[go_to] <= customer.money:
            go_to.shopping(customer)
            customer.car.come_back_info(customer, go_to, fuel_price)
        else:
            customer.less_money_info()
