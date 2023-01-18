import json

from app.customer import Customer
from app.purchase import receipt
from app.shop import Shop


def shop_trip() -> None:
    customers = []
    shops = []
    try:
        with open("app/config.json", "r") as config:
            data = json.load(config)
            customers = Customer.read_customer_json(data["customers"])
            shops = Shop.read_shop_json(data["shops"])
            fuel_price = data["FUEL_PRICE"]
    except FileNotFoundError:
        print("File do not found")

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        total_cost_in_shop = {}
        for shop in shops:
            total_cost = (
                customer.cost_for_trip_to_the_shop(shop, fuel_price)
                + customer.product_cost(shop)
            )
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_cost}")
            total_cost_in_shop.update({total_cost: shop.name})

        min_cost = min(total_cost_in_shop)
        if min_cost <= customer.money:
            print(f"{customer.name} rides to {total_cost_in_shop[min_cost]}\n")
            for shop in shops:
                if shop.name == total_cost_in_shop[min_cost]:
                    receipt(customer, shop)
                    print(f"{customer.name} now has "
                          f"{customer.money - min_cost} dollars\n")
            continue
        print(f"{customer.name} doesn't have enough money "
              f"to make purchase in any shop")
