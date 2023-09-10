import os
import json
import datetime
from app.shop import Shop, Customer


def process_file() -> dict:
    with open(os.path.join("app", "config.json"), "r") as json_file:
        info = json.load(json_file)
        return info


def get_data() -> tuple:
    info = process_file()
    fuel_price = info["FUEL_PRICE"]
    customers = [
        Customer.deserialize_from_dict(customer)
        for customer in info["customers"]
    ]
    shops = [
        Shop.deserialize_from_dict(shop)
        for shop in info["shops"]
    ]
    return fuel_price, customers, shops


def print_customer_visit(
        customer: Customer,
        check: list[Shop, float]
) -> None:
    print(f"{customer.name} rides to {check[2].name}" + "\n")
    date_string = datetime.datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S"
    )
    print(f"Date: {date_string}" + "\n"
          f"Thanks, {customer.name}, for your purchase!" + "\n"
          "You have bought: ")
    for order in customer.orders:
        item_cost = check[2].products.get(
            order.product.name
        ).price * order.amount
        print(f"{order.amount} {order.product.name}s"
              f" for {item_cost} dollars")
    customer.money -= check[0]
    print(f"Total cost is {check[1]} dollars" + "\n"
          "See you again!\n\n"
          f"{customer.name} rides home" + "\n"
          f"{customer.name} now has {customer.money} dollars" + "\n")


def process_data() -> None:
    fuel_price, customers, shops = get_data()
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        check = []
        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            products_cost = shop.get_total_cost(customer)
            total = products_cost + trip_cost
            print(f"{customer.name}'s trip to the {shop.name} costs {total}")
            if not check:
                check.extend([total, products_cost, shop])
            else:
                if total < check[0]:
                    check = [total, products_cost, shop]
        if customer.money >= check[0]:
            print_customer_visit(customer, check)
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
