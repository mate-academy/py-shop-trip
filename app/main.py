from __future__ import annotations
import json
import math
from car import Car
from customer import Customer
from receipt import print_receipt
from shop import Shop


def distance_km(a: list[float], b: list[float]) -> float:
    return math.hypot(b[0] - a[0], b[1] - a[1])


def products_cost(
    cart: dict[str, int],
    price_map: dict[str, float],
) -> float:
    total = 0.0
    for name, qty in cart.items():
        if qty <= 0:
            continue
        if name not in price_map:
            continue
        total += qty * price_map[name]
    return total


def roundtrip_fuel_cost(
    fuel_price: float,
    fuel_per_100km: float,
    one_way_km: float,
) -> float:
    round_km = one_way_km * 2.0
    liters = (round_km / 100.0) * fuel_per_100km
    return liters * fuel_price


def shop_trip() -> None:
    with open("config.json", "r", encoding="utf-8") as f:
        cfg = json.load(f)

    fuel_price = float(cfg["FUEL_PRICE"])

    customers: list[Customer] = []
    for c in cfg["customers"]:
        customers.append(
            Customer(
                name=c["name"],
                product_cart={k: int(v) for k, v in c["product_cart"].items()},
                location=[float(c["location"][0]), float(c["location"][1])],
                money=float(c["money"]),
                car=Car(
                    brand=c["car"]["brand"],
                    fuel_consumption=float(c["car"]["fuel_consumption"]),
                ),
            )
        )

    shops: list[Shop] = []
    for s in cfg["shops"]:
        shops.append(
            Shop(
                name=s["name"],
                location=[float(s["location"][0]), float(s["location"][1])],
                products={k: float(v) for k, v in s["products"].items()},
            )
        )

    for cust in customers:
        balance = (
            int(cust.money) if float(cust.money).is_integer() else cust.money
        )
        print(f"{cust.name} has {balance} dollars")

        options: list[tuple[Shop, float, float, float, float]] = []
        for shop in shops:
            one_way = distance_km(cust.location, shop.location)
            fuel_cost = roundtrip_fuel_cost(
                fuel_price=fuel_price,
                fuel_per_100km=cust.car.fuel_consumption,
                one_way_km=one_way,
            )
            goods_cost = products_cost(cust.product_cart, shop.products)
            full_cost = fuel_cost + goods_cost

            print(f"{cust.name}'s trip to the {shop.name} costs {full_cost:.2f}")

            options.append((shop, full_cost, fuel_cost, goods_cost, one_way))

        best_shop, best_full, best_fuel, best_goods, _ = min(
            options, key=lambda x: x[1]
        )

        if best_full > cust.money:
            print(
                f"{cust.name} doesn't have enough money to make a purchase "
                f"in any shop"
            )
            print()
            continue

        print(f"{cust.name} rides to {best_shop.name}")
        cust.location = list(best_shop.location)

        print_receipt(cust, best_shop, products_cost=best_goods)

        print(f"{cust.name} rides home")
        cust.location = list(cust.home_location)

        cust.money = round(cust.money - best_full, 2)
        print(f"{cust.name} now has {cust.money} dollars")
        print()
