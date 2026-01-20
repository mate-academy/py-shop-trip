import json
import os
from decimal import Decimal, ROUND_HALF_UP
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def _to_decimal(value):
    return Decimal(str(value))


def fmt_two(value):
    d = _to_decimal(value).quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
    return format(d, "f")


def fmt_min(value):
    d = _to_decimal(value).normalize()
    s = format(d, "f")
    if s.endswith(".0"):
        return s[:-2]
    return s


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    fuel_price = _to_decimal(config["FUEL_PRICE"])

    customers = []
    for data in config["customers"]:
        car = Car(
            brand=data["car"]["brand"],
            fuel_consumption=_to_decimal(data["car"]["fuel_consumption"])
        )
        customer = Customer(
            name=data["name"],
            location=tuple(data["location"]),
            money=_to_decimal(data["money"]),
            cart=data["product_cart"],
            car=car
        )
        customers.append(customer)

    shops = [
        Shop(
            name=shop["name"],
            location=tuple(shop["location"]),
            products={k: _to_decimal(v) for k, v in shop["products"].items()}
        )
        for shop in config["shops"]
    ]

    for customer in customers:
        print(f"{customer.name} has {int(customer.money)} dollars")
        costs = []
        for shop in shops:
            cost = customer.trip_cost(shop, fuel_price)
            print(
                f"{customer.name}'s trip to the {shop.name} costs "
                f"{fmt_two(cost)}"
            )
            costs.append((cost, shop))

        costs.sort(key=lambda x: x[0])
        for cost, shop in costs:
            if cost <= customer.money:
                print(f"{customer.name} rides to {shop.name}")
                customer.go_to(shop.location)
                shop.print_receipt(customer.name, customer.cart, fmt_min)
                customer.go_home()
                customer.money -= cost
                print(f"{customer.name} rides home")
                print(
                    f"{customer.name} now has {fmt_two(customer.money)} "
                    "dollars\n"
                )
                break
        else:
            print(
                f"{customer.name} doesn't have enough money to make a "
                "purchase in any shop\n"
            )
