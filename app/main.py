import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as file:
        config = json.load(file)

    fuel_price, customers_list, shops_list = (
        config["FUEL_PRICE"],
        config["customers"],
        config["shops"]
    )
    customers = Customer.list_read(customers_list)
    shops = Shop.list_read(shops_list)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        best_shop = Shop.find_best_shop(shops, customer, fuel_price)

        if best_shop is None:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make purchase in any shop"
            )
            continue

        shop_cost = customer.car.trip_fuel_cost(best_shop.location, fuel_price)
        shop_cost += best_shop.total_price(customer.product_cart)

        if customer.money < shop_cost:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make purchase in any shop"
            )
            continue

        customer.money -= shop_cost

        customer.make_purchase(best_shop)
