import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)

    fuel_price = data["FUEL_PRICE"]
    customers = [Customer(customer) for customer in data["customers"]]
    shops = [Shop(shop) for shop in data["shops"]]

    for customer in customers:
        different_shops_trip_cost = {}
        print(f"{customer.name} has {customer.money} dollars")

        for shop in shops:
            trip_cost = customer.car.trip_cost(
                customer.location,
                shop.location,
                fuel_price
            )
            shopping_cost = shop.products_cost(customer.product_cart)
            total = round(trip_cost + shopping_cost, 2)
            print(f"{customer.name}'s trip to the {shop.name} costs {total}")

            if customer.money >= total:
                different_shops_trip_cost[total] = shop

        if not different_shops_trip_cost:
            print(f"{customer.name} doesn't have enough "
                  f"money to make purchase in any shop")

            return

        cheapest_trip = min(different_shops_trip_cost.keys())
        print(f"{customer.name} rides to "
              f"{different_shops_trip_cost[cheapest_trip].name}\n")
        different_shops_trip_cost[cheapest_trip].bill_info(customer)
        customer.money = round(customer.money - cheapest_trip, 2)
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {customer.money} dollars\n")
