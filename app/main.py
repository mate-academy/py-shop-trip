from __future__ import annotations
import json
import math
from car import Car
from customer import Customer
from receipt import print_receipt
from shop import Shop


def shop_trip() -> None:
    with open("config.json", "r", encoding="utf-8") as file:
        cfg = json.load(file)

    fuel_price = float(cfg["FUEL_PRICE"])

    customers: list[Customer] = []
    for customer_data in cfg["customers"]:
        customers.append(
            Customer(
                name=customer_data["name"],
                product_cart={
                    k: int(v) for k, v in customer_data["product_cart"].items()
                },
                location=[
                    float(customer_data["location"][0]),
                    float(customer_data["location"][1]),
                ],
                money=float(customer_data["money"]),
                car=Car(
                    brand=customer_data["car"]["brand"],
                    fuel_consumption=float(
                        customer_data["car"]["fuel_consumption"]
                    ),
                ),
            )
        )

    shops: list[Shop] = []
    for shop_data in cfg["shops"]:
        shops.append(
            Shop(
                name=shop_data["name"],
                location=[
                    float(shop_data["location"][0]),
                    float(shop_data["location"][1]),
                ],
                products={k: float(v) for k, v in shop_data["products"].items()},
            )
        )

    for customer in customers:
        balance = (
            int(customer.money)
            if float(customer.money).is_integer()
            else customer.money
        )
        print(f"{customer.name} has {balance} dollars")

        options: list[tuple[Shop, float, float, float, float]] = []
        for shop in shops:
            one_way_km = math.hypot(
                shop.location[0] - customer.location[0],
                shop.location[1] - customer.location[1],
            )

            round_km = one_way_km * 2.0
            liters = (round_km / 100.0) * customer.car.fuel_consumption
            fuel_cost = liters * fuel_price

            goods_cost = 0.0
            for prod_name, qty in customer.product_cart.items():
                if qty <= 0:
                    continue
                if prod_name not in shop.products:
                    continue
                goods_cost += qty * shop.products[prod_name]

            full_cost = fuel_cost + goods_cost

            print(
                f"{customer.name}'s trip to the {shop.name} costs "
                f"{full_cost:.2f}"
            )

            options.append(
                (shop, full_cost, fuel_cost, goods_cost, one_way_km)
            )

        best_shop, best_full, best_fuel, best_goods, _ = min(
            options, key=lambda tup: tup[1]
        )

        if best_full > customer.money:
            print(
                f"{customer.name} doesn't have enough money to make a "
                f"purchase in any shop"
            )
            print()
            continue

        print(f"{customer.name} rides to {best_shop.name}")
        customer.location = list(best_shop.location)

        print_receipt(customer, best_shop, products_cost=best_goods)

        print(f"{customer.name} rides home")
        customer.location = list(customer.home_location)

        customer.money = round(customer.money - best_full, 2)
        print(f"{customer.name} now has {customer.money} dollars")
        print()
