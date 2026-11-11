import json
from pathlib import Path

from app.shop import Shop
from app.car import Car
from app.customer import Customer


def shop_trip() -> None:
    config_path = Path(__file__).parent / "config.json"
    with config_path.open(encoding="utf-8") as file:
        config = json.load(file)
    fuel_price = config["FUEL_PRICE"]
    shop_objects = []
    for shop_data in config["shops"]:
        shop_objects.append(
            Shop(
                name=shop_data["name"],
                location=shop_data["location"],
                products_and_prices=shop_data["products"],
            )
        )
    for customer_data in config["customers"]:
        car_data = customer_data["car"]
        car = Car(
            car_data["brand"],
            car_data["fuel_consumption"],
        )
        customer = Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            current_location=customer_data["location"],
            money=customer_data["money"],
            car=car,
            home_location=customer_data["location"],
        )
        print(f"{customer.name} has {customer.money} dollars")
        result = customer.find_cheapest_shop(
            shop_objects,
            fuel_price,
        )
        if result is None:
            continue
        shop, trip_cost = result
        print()
        shop.print_receipt(
            customer,
            customer.product_cart,
        )
        print()
        customer.pay_for_trip(trip_cost)
        customer.go_home()
        print()
