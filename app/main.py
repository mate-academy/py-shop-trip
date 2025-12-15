import json

from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:

    with open("app/config.json", "r") as file_info:
        content = json.load(file_info)

    fuel_price = content["FUEL_PRICE"]
    customers = content["customers"]
    shops = content["shops"]

    list_of_customers = []
    list_of_shops = []

    for customer in customers:
        list_of_customers.append(Customer(
            name=customer["name"],
            products_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(brand=customer["car"]["brand"],
                    fuel_consumption=customer["car"]["fuel_consumption"])
        ))

    for shop in shops:
        list_of_shops.append(Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]))

    for customer in list_of_customers:
        print(f"{customer.name} has {customer.money} dollars")

        prices = {}
        for shop in list_of_shops:
            price_of_trip = customer.car.calculate_price_road(
                shop=shop,
                customer=customer,
                fuel_price=fuel_price
            )
            prices[price_of_trip] = shop

        lowest_shop = min(price for price in prices)

        if customer.money >= lowest_shop:
            print(f"{customer.name} rides to {prices[lowest_shop].name}\n")
            customer.go_to_location(prices[lowest_shop].location)
            prices[lowest_shop].print_check(customer)
            customer.money -= lowest_shop
            print(f"{customer.name} rides home")
            customer.go_home()
            print(f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
