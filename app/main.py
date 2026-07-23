import json
import os
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))

    paths_to_check = [
        os.path.join(base_dir, "config.json"),
        os.path.join(base_dir, "..", "config.json"),
        "config.json"
    ]

    config_path = None
    for path in paths_to_check:
        if os.path.exists(path):
            config_path = path
            break

    if not config_path:
        raise FileNotFoundError("Файл config.json не знайдено!")

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]

    shops = [
        Shop(
            name=s["name"],
            location=s["location"],
            products=s["products"]
        )
        for s in config["shops"]
    ]

    for cust_data in config["customers"]:
        customer = Customer(
            name=cust_data["name"],
            product_cart=cust_data["product_cart"],
            location=cust_data["location"],
            money=cust_data["money"],
            car_data=cust_data["car"]
        )

        money_str = f"{customer.money:g}"
        print(f"{customer.name} has {money_str} dollars")

        cheapest_shop = None
        min_trip_cost = float("inf")

        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {round(trip_cost, 2)}")

            if trip_cost < min_trip_cost:
                min_trip_cost = trip_cost
                cheapest_shop = shop

        if cheapest_shop and customer.money >= min_trip_cost:
            # 1. Порожній рядок ПЕРЕД чеком (після rides to...):
            print(f"{customer.name} rides to {cheapest_shop.name}\n")

            customer.location = cheapest_shop.location.copy()

            # 2. Друк чека
            products_cost = cheapest_shop.print_receipt(
                customer.name,
                customer.product_cart
            )

            # 3. Порожній рядок ПІСЛЯ чека (перед rides home):
            print()

            round_trip_fuel_cost = (min_trip_cost - products_cost)
            customer.money -= (products_cost + round_trip_fuel_cost)

            print(f"{customer.name} rides home")
            customer.location = customer.home_location.copy()

            # 4. Порожній рядок між покупцями:
            print(f"{customer.name} now has "
                  f"{round(customer.money, 2)} dollars\n")
        else:
            print(f"{customer.name} "
                  f"doesn't have enough money to make a purchase in any shop")
