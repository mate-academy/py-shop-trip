import json
import datetime
from app.shop import Shop
from app.customer import Customer
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        config_dict = json.load(config_file)
        fuel_price = config_dict["FUEL_PRICE"]
        customers = [
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(customer["car"]["brand"],
                    customer["car"]["fuel_consumption"]))
            for customer in config_dict["customers"]
        ]
        shops = [
            Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            ) for shop in config_dict["shops"]
        ]
        for customer in customers:
            home_location = customer.location
            min_total_costs = 10 ** 6
            min_shop_costs: int
            print(f"{customer.name} has {customer.money} dollars")

            for shop in shops:
                if customer.calculate_costs(shop):
                    costs = customer.calculate_costs(shop)
                    total_costs = round(
                        costs + customer.car.trip_consumption(
                            customer.location, shop.location
                        )
                        * fuel_price * 2,
                        2)
                    if total_costs < min_total_costs:
                        min_total_costs = total_costs
                        min_shop_costs = costs
                        cheapest_shop = shop
                    print(f"{customer.name}'s trip to the "
                          f"{shop.name} costs {total_costs}")

            if min_total_costs <= customer.money:
                print(f"{customer.name} rides to {cheapest_shop.name}")
                customer.location = cheapest_shop.location
                print()
                print(
                    datetime.datetime.now().strftime(
                        "Date: %d/%m/%Y %H:%M:%S"
                    )
                )
                print(f"Thanks, {customer.name}, for you purchase!\n"
                      f"You have bought: ")
                for item, quantity in customer.product_cart.items():
                    print(f"{quantity} {item}s for "
                          f"{cheapest_shop.products[item] * quantity} dollars")
                print(f"Total cost is {min_shop_costs} dollars\n"
                      f"See you again!")
                customer.money -= min_total_costs
                print()
                print(f"{customer.name} rides home")
                customer.location = home_location
                print(f"{customer.name} now has {customer.money} dollars")
                print()

            else:
                print(
                    f"{customer.name} doesn't have enough money"
                    f" to make purchase in any shop"
                )
