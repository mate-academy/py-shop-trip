import json
from decimal import Decimal
from typing import Any
from app.customer import Customer
from app.shop import Shop
import datetime


def shop_trip() -> Any:
    data = None
    with open("app/config.json", "r") as file:
        data = json.load(file)

    customers = [
        Customer(**element)
        for element in data["customers"]
    ]

    shops = [
        Shop(**element)
        for element in data["shops"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        shop_trip_costs = []

        for shop in shops:
            fuel_cost = customer.get_fuel_price(
                shop_location=shop.location,
                fuel_price=data["FUEL_PRICE"]
            )
            shop_price = (shop.get_products_price
                          (customer_cart=customer.product_cart))
            full_price = (Decimal(fuel_cost + shop_price)
                          .quantize(Decimal("0.01")))
            shop_trip_costs.append((full_price, shop))

            print(f"{customer.name}'s trip to "
                  f"the {shop.name} costs {full_price}")

        min_price, best_shop = min(shop_trip_costs, key=lambda x: x[0])

        if min_price <= customer.money:
            print(f"{customer.name} rides to {best_shop.name}\n")
            customer.location = best_shop.location
            print(f"""Date: {datetime.datetime.now()
                  .strftime("%d/%m/%Y %H:%M:%S")}"""
                  )
            print(f"Thanks, {customer.name}, for your purchase!")
            best_shop.bough_info(customer_cart=customer.product_cart)
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{customer.money - min_price} dollars\n")
        else:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
    return None
