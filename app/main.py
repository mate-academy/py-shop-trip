import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop


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
                car=customer["car"]
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
        car = Car(
            brand=customer.car["brand"],
            fuel_consumption=customer.car["fuel_consumption"]
        )
        print(f"{customer.name} has {customer.money} dollars")

        shop_dict = {}

        for shop in shops:
            trip_expenses = (
                shop.shop_expenses(customer)
                + car.car_expenses(fuel_price, customer, shop)
            )
            print(f"{customer.name}'s trip to the {shop.name} costs "
                  f"{trip_expenses}")
            shop_dict[shop] = trip_expenses

        go_to = min(shop_dict, key=shop_dict.get)
        if go_to.shop_expenses(customer) <= customer.money:
            total_expenses = (
                go_to.shop_expenses(customer)
                + car.car_expenses(fuel_price, customer, go_to)
            )
            print(f"{customer.name} rides to {go_to.name}\n")
            go_to.shopping(customer)
            print(f"{customer.name} rides home\n"
                  f"{customer.name} now has "
                  f"{customer.money - total_expenses} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make purchase in any shop")
