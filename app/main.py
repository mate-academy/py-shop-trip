import datetime
import json
from app.car import Car
from app.customer import Customer
from app.location import Location
from app.shop import Shop


def shop_trip() -> None:

    with open("app/config.json", "r") as config_file:
        config_dict = json.load(config_file)

    fuel_price = config_dict["FUEL_PRICE"]
    customers = [
        Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=Location(
                customer["location"][0],
                customer["location"][1]
            ),
            money=customer["money"],
            car=Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]
            )
        )
        for customer in config_dict["customers"]
    ]

    shops = [
        Shop(
            name=shop["name"],
            location=Location(shop["location"][0], shop["location"][1]),
            products=shop["products"],
        )
        for shop in config_dict["shops"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        min_total_costs = 10**7
        cheapest_shop: Shop
        for shop in shops:
            shoping_costs = customer.calculate_shoping_costs(shop)
            distance = customer.location.calculate_distance(shop.location)
            road_costs = customer.car.calculate_fuel_costs(
                distance, fuel_price
            )
            total_costs = round(shoping_costs + road_costs * 2, 2)
            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {total_costs}"
            )
            if total_costs < min_total_costs:
                min_total_costs = total_costs
                cheapest_shop = shop
                min_shoping_costs = shoping_costs

        if customer.money >= min_total_costs:
            print(f"{customer.name} rides to {cheapest_shop.name}")
            print()
            customer.location = cheapest_shop.location

            timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"Date: {timestamp}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            for product, amount in customer.product_cart.items():
                product_costs = amount * cheapest_shop.products[product]
                if int(product_costs) == product_costs:
                    product_costs = int(product_costs)
                print(f"{amount} {product}s for {product_costs} dollars")
            print(f"Total cost is {min_shoping_costs} dollars")
            print("See you again!")
            print()

            print(f"{customer.name} rides home")
            customer.money -= min_total_costs
            print(f"{customer.name} now has {customer.money} dollars")
            print()
        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
