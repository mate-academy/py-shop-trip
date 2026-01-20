import json

import app.calculations as calculations
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:

    with open("app/config.json", "r") as file:
        cs_list = json.load(file)
    fuel_price = cs_list["FUEL_PRICE"]
    shops = []
    for shop in cs_list["shops"]:
        shops.append(Shop(shop))

    for customer in cs_list["customers"]:
        customer = Customer(customer)
        print(f"{customer.name} has {customer.money} dollars")
        nearest_shop = []
        for shop in shops:
            for product in customer.product_cart:
                if product not in shop.products:
                    continue
            total = 0
            receipt = {}
            trip_dist = calculations.get_distance(shop, customer)
            ride = customer.fuel_consumption * fuel_price
            fuel_cost = trip_dist / 100 * ride
            total, receipt = calculations.purchases(
                total, receipt, customer, shop)
            trip_cost = round(fuel_cost * 2 + total, 2)
            # Ugly indentations - because of flake8.
            print(
                f"{customer.name}'s trip to the",
                f"{shop.name} costs {trip_cost}")
            if not nearest_shop:
                nearest_shop = shop
                nearest_shop.trip_cost = trip_cost
            else:
                if trip_cost < nearest_shop.trip_cost:
                    nearest_shop = shop
                    nearest_shop.trip_cost = trip_cost
        budget = customer.money - nearest_shop.trip_cost
        if 0 > budget:
            print(
                f"{customer.name} doesn't have enough money",
                "to make a purchase in any shop")
        else:
            print(f"{customer.name} rides to {nearest_shop.name}\n")
            total, receipt = calculations.purchases(
                0, None, customer, nearest_shop)
            print(calculations.get_receipt(receipt, customer, total))
            print(f"\n{customer.name} rides home")
            print(f"{customer.name} now has {budget} dollars\n")


if __name__ == "__main__":
    pass
