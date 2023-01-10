import json
import math
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as config:
        info = json.load(config)

    fuel_price = info["FUEL_PRICE"]

    customers_ls = []
    for customer in info["customers"]:
        customers_ls.append(Customer(customer))

    shops_ls = []
    for shop in info["shops"]:
        shops_ls.append(Shop(shop))

    for customer in customers_ls:
        print(f"{customer.name} has {customer.money} dollars")
        cost_dict = {}
        for shop in shops_ls:
            road_km = math.floor(
                math.dist(customer.location, shop.location) * 2 * 100
            ) / 100
            trip_cost = round(
                (fuel_price * road_km * customer.car.consumption / 100), 2)
            product_cost = 0
            for goods, amount in customer.product_cart.items():
                product_cost += amount * shop.products[goods]
            cost_dict[shop] = [trip_cost, product_cost]
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {sum(cost_dict[shop])}")

        cheapest_shop = min(sum(value) for value in cost_dict.values())
        if cheapest_shop > customer.money:
            print(f"{customer.name} doesn't have "
                  f"enough money to make purchase in any shop")
            return
        for key, value in cost_dict.items():
            if sum(value) == cheapest_shop:
                shop_to_go = key
        print(f"{customer.name} rides to {shop_to_go.name}\n")
        customer.location = shop_to_go.location
        customer.money -= sum(cost_dict[shop_to_go])

        shop_to_go.shopping(customer)
