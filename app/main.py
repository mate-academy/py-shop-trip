import json

from math import dist

from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("config.json", "r") as f:
        data = json.load(f)

    fuel_price = data["FUEL_PRICE"]
    customers = data["customers"]
    shops = data["shops"]

    shops_list = []
    for shop in shops:
        shop_ = Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
        shops_list.append(shop_)

    for customer in customers:
        customer_ = Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                brand=customer["car"]["brand"],
                fuel_consumption=customer["car"]["fuel_consumption"]
            )
        )

        costs = []
        for shop in shops_list:
            distance_km = dist(customer_.location, shop.location)
            fuel_cost_ = customer_.car.fuel_cost(distance_km, fuel_price)
            cart_price = shop.calculate_cart_price(customer_.product_cart)
            cost = round(2 * fuel_cost_ + cart_price, 2)
            costs.append(cost)

        print(f"{customer_.name} has {customer_.money} dollars")

        for i in range(len(shops_list)):
            print(
                f"{customer_.name}'s trip to the "
                f"{shops_list[i].name} costs {costs[i]}"
            )

        if customer_.money < min(costs):
            print(
                f"{customer_.name} doesn't have enough money "
                "to make a purchase in any shop"
            )
        else:
            min_index = costs.index(min(costs))
            target_shop = shops_list[min_index]
            print(f"{customer_.name} rides to {target_shop.name}")
            target_shop.print_receipt(customer_.name, customer_.product_cart)
            print(f"\n{customer_.name} rides home")
            remaining_money = customer_.money - costs[min_index]
            print(f"{customer_.name} now has {remaining_money} dollars\n")
