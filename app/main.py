import json
from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        source_dict = json.load(f)

    fuel_price = source_dict["FUEL_PRICE"]

    customers = [Customer(
        name=customer["name"],
        product_cart=customer["product_cart"],
        location=customer["location"],
        money=customer["money"],
        car=customer["car"]
    ) for customer in source_dict["customers"]]

    shops = [Shop(
        name=shop["name"],
        location=shop["location"],
        products=shop["products"]
    ) for shop in source_dict["shops"]]

    for customer in customers:
        car = Car(
            brand=customer.car["brand"],
            fuel_consumption=customer.car["fuel_consumption"]
        )

        customer.get_amount_of_money()

        shop_dict = {}
        for shop in shops:
            shop_dict[shop] = car.get_total_trip_cost(
                customer, shop, fuel_price
            )
            car.get_shopping_options(customer, shop, fuel_price)

        best_shop = min(shop_dict, key=shop_dict.get)
        if customer.money >= shop_dict[best_shop]:
            best_shop.get_best_option(customer)
            best_shop.get_receipt(customer)
            car.get_home(customer, best_shop, fuel_price)
        else:
            customer.not_enough_money()
