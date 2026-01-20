import json
from app.shop import Shop
from app.car import Car
from app.customer import Customer
from pathlib import Path


def shop_trip() -> None:
    current_dir = Path(__file__).parent
    config_path = current_dir / "config.json"

    with open(config_path, "r") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]
    customers_data = config["customers"]
    shops_data = config["shops"]
    shops = []

    for shop_data in shops_data:
        shops.append(Shop(
            shop_data["name"], shop_data["location"], shop_data["products"]
        ))

    for customer_data in customers_data:
        car_data = customer_data["car"]
        car = Car(car_data["brand"], car_data["fuel_consumption"])
        customer = Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=car
        )

        print(f"{customer.name} has {customer.money} dollars")

        shop_costs = {}

        for shop in shops:
            total_cost = customer.calculate_total_cost(shop, fuel_price)
            shop_costs[shop.name] = round(total_cost, 2)

            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {total_cost}")

        cheapest_shop_name = min(shop_costs, key=shop_costs.get)
        cheapest_shop_object = next(
            shop for shop in shops if shop.name == cheapest_shop_name
        )

        if shop_costs[cheapest_shop_name] > customer.money:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            continue

        print(f"{customer.name} rides to {cheapest_shop_object.name}\n")

        customer.location = customer.moving_to_shop(cheapest_shop_object)
        receipt = cheapest_shop_object.print_receipt(
            customer.name, customer.product_cart
        )

        print(receipt)
        print(f"{customer.name} rides home")

        customer.location = customer.moving_home()
        customer.money -= shop_costs[cheapest_shop_object.name]

        print(f"{customer.name} now has {customer.money} dollars\n")
