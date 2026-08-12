import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", encoding="utf-8") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    customers = [
        Customer(customer)
        for customer in data["customers"]
    ]
    shops = [
        Shop(shop)
        for shop in data["shops"]
    ]

    for customer in customers:
        cheapest_shop, cheapest_price = customer.find_cheapest_shop(
            shops, fuel_price
        )

        if cheapest_shop is not None and cheapest_price <= customer.money:
            print(f"{customer.name} rides to {cheapest_shop.name}")
            print()
            customer.change_location(cheapest_shop.location)
            cheapest_shop.buy_products(customer.name, customer.product_cart)
            print(f"{customer.name} rides home")
            customer.change_location(customer.prev_location)
            customer.money -= cheapest_price
            print(f"{customer.name} now has {customer.money} dollars")
            print()
        elif cheapest_price > customer.money:
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")
