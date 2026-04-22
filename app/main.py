import json
from .car import Car
from .shop import Shop
from .customer import Customer


def shop_trip() -> None:
    from pathlib import Path
    config_path = Path(__file__).parent.parent / "config.json"
    with open(config_path, "r") as f:
        data = json.load(f)
    fuel_price = data.get("FUEL_PRICE", 50.0)
    shops = [Shop(s["name"], s["location"], s["products"])
             for s in data["shops"]]
    for c_data in data["customers"]:
        car = Car(c_data["car"]["brand"], c_data["car"]["fuel_consumption"])
        customer = Customer(
            c_data["name"],
            c_data["location"],
            c_data["money"],
            c_data["product_cart"],
            car
        )
        print(f"{customer.name} has {customer.money} dollars")
        valid_trips = []
        for shop in shops:
            result = customer.calculate_trip_cost(shop, fuel_price)
            if result is not None:
                products_cost, fuel_cost, total_cost = result
                print(f"{customer.name}'s trip to the "
                      f"{shop.name} costs {total_cost}")
                if total_cost <= customer.money:
                    valid_trips.append((total_cost, products_cost,
                                        fuel_cost, shop))
        if valid_trips:
            best = min(valid_trips, key=lambda x: x[0])
            customer.perform_trip(best[3], best[1], best[2])
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
