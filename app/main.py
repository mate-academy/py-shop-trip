import json
from pathlib import Path
from .car import Car
from .customer import Customer
from .shop import Shop

def shop_trip():
    # Загружаем данные
    config_path = Path(__file__).parent / "config.json"
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]

    # Создаём объекты Shop
    shops = [Shop(**shop) for shop in config["shops"]]

    # Создаём объекты Customer
    customers = []
    for cust in config["customers"]:
        car = Car(**cust["car"])
        customers.append(Customer(
            name=cust["name"],
            product_cart=cust["product_cart"],
            location=cust["location"],
            money=cust["money"],
            car=car
        ))

    # Логика поездок
    for cust in customers:
        print(f"\n{cust.name} has {cust.money} dollars")
        trip_costs = {}
        for shop in shops:
            cost = cust.trip_cost(shop, fuel_price)
            trip_costs[shop] = cost
            print(f"{cust.name}'s trip to {shop.name} costs {cost}")

        # выбираем самый дешёвый
        shop, best_cost = min(trip_costs.items(), key=lambda x: x[1])
        if cust.money >= best_cost:
            print(f"{cust.name} rides to {shop.name}")
            cust.ride_to_shop(shop)
            shop.print_receipt(cust.name, cust.product_cart)
            cust.ride_home()
            cust.money = round(cust.money - best_cost, 2)
            print(f"{cust.name} rides home")
            print(f"{cust.name} now has {cust.money} dollars")
        else:
            print(f"{cust.name} doesn't have enough money to make a purchase in any shop")
