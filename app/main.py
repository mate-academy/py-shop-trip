import json

from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:

    with open("app/config.json", "r") as f:
        config = json.load(f)

    shops = []
    for shop_data in config["shops"]:
        shop = Shop(
            shop_name=shop_data["name"],
            location=shop_data["location"],
            products=shop_data["products"]
        )
        shops.append(shop)

    customer_list = []
    for customer_data in config["customers"]:
        car = Car(
            brand=customer_data["car"]["brand"],
            fuel_consumption=customer_data["car"]["fuel_consumption"],
        )
        single_customer = Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=car
        )
        customer_list.append(single_customer)

    fuel_price = config["FUEL_PRICE"]
    for i, single_customer in enumerate(customer_list):
        if i > 0:
            print()
        print(f"{single_customer.name} has {single_customer.money} dollars")
        cheapest_shop = None
        min_cost = float("inf")

        for shop in shops:
            cost = single_customer.total_price(shop, fuel_price)
            print(
                f"{single_customer.name}'s "
                f"trip to the {shop.shop_name} "
                f"costs {cost:.2f}"
            )
            if cost < min_cost:
                min_cost = cost
                cheapest_shop = shop
        if single_customer.money >= min_cost:
            print(f"{single_customer.name} rides to {cheapest_shop.shop_name}")
            single_customer.location = tuple(cheapest_shop.location)
            cheapest_shop.print_check(single_customer)
            print(f"{single_customer.name} rides home")
            remaining_money = round(single_customer.money - min_cost, 2)
            print(f"{single_customer.name} now has {remaining_money} dollars")
        else:
            print(
                f"{single_customer.name} doesn't have "
                f"enough money to make a "
                f"purchase in any shop"
            )
