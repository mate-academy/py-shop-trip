import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop
from app.utils import (
    calc_distance,
    require_keys,
    fmt_money,
)


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        loaded_info = json.load(f)

    require_keys(
        loaded_info,
        ["FUEL_PRICE", "customers", "shops"]
    )

    fuel_price: float = loaded_info["FUEL_PRICE"]
    customers_data: list[dict] = loaded_info["customers"]
    shops_data: list[dict] = loaded_info["shops"]

    customers: list[Customer] = []
    for customer_dict in customers_data:
        if "car" not in customer_dict:
            customer_name = customer_dict.get(
                "name", "unknown customer"
            )
            raise ValueError(
                f"Car is missing for "
                f"{customer_name}"
            )

        car = Car(**customer_dict["car"])
        customer_payload = {
            k: v
            for k, v in customer_dict.items()
            if k != "car"
        }
        customer = Customer(car=car, **customer_payload)
        customers.append(customer)

    shops: list[Shop] = [
        Shop(**shop_dict) for shop_dict in shops_data
    ]

    for customer in customers:
        print(
            f"{customer.name} has "
            f"{fmt_money(customer.money)} dollars"
        )

        shop_costs: list[tuple[Shop, float]] = []

        for shop in shops:
            if not shop.can_sell(customer.product_cart):
                continue

            distance = calc_distance(
                customer.location, shop.location
            )
            products_cost = shop.cart_cost(customer.product_cart)
            fuel_cost = customer.car.round_trip_fuel_cost(
                distance, fuel_price
            )

            total_trip_cost = round(products_cost + fuel_cost, 2)
            shop_costs.append((shop, total_trip_cost))

            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {total_trip_cost:.2f}"
            )

        if not shop_costs:
            print(
                f"{customer.name} can't buy "
                f"all products in any shop"
            )
            continue

        best_shop, best_cost = min(shop_costs, key=lambda x: x[1])

        if not customer.can_afford(best_cost):
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )
            continue

        print(f"{customer.name} rides to {best_shop.name}")
        customer.go_to(best_shop.location)

        print()
        best_shop.print_receipt(customer)
        print()

        print(f"{customer.name} rides home")
        customer.go_home()

        customer.pay(best_cost)
        print(
            f"{customer.name} now has "
            f"{fmt_money(customer.money)} dollars"
        )
        print()
