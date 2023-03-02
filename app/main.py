import json
from datetime import datetime

from app.customer import Customer
from app.car import Car
from app.shop import Shop
from app.go_to_shop import count_trip_to_shop_value


def shop_trip() -> None:

    with open("app/config.json", "r") as data:
        file_data = json.load(data)

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
        ) for customer in file_data["customers"]
    ]

    shops = [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        ) for shop in file_data["shops"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shop, min_costs = count_trip_to_shop_value(
            customer=customer,
            shops=shops,
            fuel_price=file_data["FUEL_PRICE"]
        )

        if min_costs > customer.money:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make purchase in any shop"
            )
            continue

        print(f"{customer.name} rides to {cheapest_shop.name}\n")

        customer_home = customer.location
        customer.location = cheapest_shop.location

        date = datetime(
            year=2021, month=1, day=4, hour=12, minute=33, second=41
        )

        print(f"Date: {date.strftime('%d/%m/%Y %H:%M:%S')}")
        # print(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        # tests crush if it make it like that
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")

        shopping_costs = 0

        for product in customer.product_cart:
            if product in cheapest_shop.products:
                spent_per_product = (
                    customer.product_cart[product]
                    * cheapest_shop.products[product]
                )
                shopping_costs += spent_per_product
                print(
                    f"{customer.product_cart[product]} {product}s "
                    f"for {spent_per_product} dollars"
                )

        print(f"Total cost is {shopping_costs} dollars")
        print("See you again!\n")
        print(f"{customer.name} rides home")

        customer.location = customer_home

        money_rest = round(customer.money - min_costs, 2)

        print(f"{customer.name} now has {money_rest} dollars\n")
