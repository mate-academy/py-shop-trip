import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        data = json.load(config)

    customers = [Customer(**customer) for customer in data["customers"]]
    shops = [Shop(**shop) for shop in data["shops"]]
    fuel_price = data["FUEL_PRICE"]

    for customer in customers:
        car = Car(customer.car["brand"], customer.car["fuel_consumption"])

        print(f"{customer.name} has {customer.money} dollars")

        prices_in_shops = {}
        for shop in shops:
            fuel_cost = car.calculate_fuel_cost(customer, shop, fuel_price)
            products_cost = customer.calculate_products_cost(shop)
            total = round(products_cost + fuel_cost, 2)

            print(f"{customer.name}'s trip to the {shop.name} costs {total}")
            prices_in_shops[total] = shop

        cheapest_shop = prices_in_shops.get(min(prices_in_shops.keys()))

        if customer.money >= min(prices_in_shops.keys()):
            print(f"{customer.name} rides to {cheapest_shop.name}\n")

            cheapest_shop.make_purchase(customer)

            print(f"{customer.name} rides home\n"
                  f"{customer.name} now has "
                  f"{customer.money - min(prices_in_shops.keys())} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make purchase in any shop")
