import json
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:

    with open("app/config.json", "r") as f:
        data = json.load(f)

    customers = [Customer(customer) for customer in data["customers"]]
    shops = [Shop(shop) for shop in data["shops"]]

    for customer in customers:
        preferred_shops = []
        print(f"{customer.name} has {customer.money} dollars")
        car = Car(customer.car)

        for shop in shops:
            product_cost = shop.calculate_costs(customer.product_cart)
            distance = customer.calculate_distance(shop)
            trip_cost = car.fuel_costs(distance, data["FUEL_PRICE"]) * 2
            total_cost = round(trip_cost + product_cost, 2)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_cost}")

            if customer.money > total_cost:
                preferred_shops.append((shop, total_cost))

        if not preferred_shops:
            print(f"{customer.name} doesn't have enough money "
                  f"to make purchase in any shop")
            break

        grocery, total_cost = sorted(
            preferred_shops, key=lambda x: x[1]
        )[0]
        print(f"{customer.name} rides to {grocery.name}\n")
        grocery.receipt(customer.name, customer.product_cart)
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has "
              f"{customer.money - total_cost} dollars\n")
