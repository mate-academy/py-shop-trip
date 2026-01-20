import json
import os

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open(os.path.join("app", "config.json"), "r") as file:
        configs = json.load(file)

    fuel_price = configs["FUEL_PRICE"]
    customers = [
        Customer.from_dict(customer) for customer in configs["customers"]
    ]

    shops = [
        Shop.from_dict(shop) for shop in configs["shops"]
    ]

    for customer in customers:
        cheapest_price = customer.money
        cheapest_shop = None

        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            shopping_costs = customer.calculate_trip_cost(
                destination=shop.location,
                products=shop.products,
                fuel_price=fuel_price
            )
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {shopping_costs}")
            if shopping_costs < cheapest_price:
                cheapest_price = shopping_costs
                cheapest_shop = shop
        if cheapest_shop:
            print(f"{customer.name} rides to {cheapest_shop}\n")
            customer.location = cheapest_shop.location
            cheapest_shop.print_check(
                customer.name,
                customer.product_cart
            )
            customer.money -= cheapest_price
            print(f"{customer.name} rides home")
            customer.location = customer.home
            print(f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money to "
                  f"make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
