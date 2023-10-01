import json
from datetime import datetime

from car import Car
from customer import Customer
from shop import Shop


def calculate_distance(
        location1: list[int], location2: list[int]
) -> float:
    x1, y1 = location1
    x2, y2 = location2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def shop_trip() -> None:
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    fuel_price = config["FUEL_PRICE"]
    customers_data = config["customers"]
    shops_data = config["shops"]

    customers = []
    shops = []

    for customer_data in customers_data:
        car_data = customer_data["car"]
        car = Car(car_data["brand"], car_data["fuel_consumption"])
        cust = Customer(
            customer_data["name"],
            customer_data["product_cart"],
            customer_data["location"],
            customer_data["money"],
            car
        )
        customers.append(cust)

    for shop_data in shops_data:
        shop = Shop(
            shop_data["name"],
            shop_data["location"],
            shop_data["products"]
        )
        shops.append(shop)

    for cust in customers:
        print(f"{cust.name} has {cust.money} dollars")
        cheapest = None
        min_cost = float("inf")

        for shop in shops:
            distance_to_shop = (
                calculate_distance(cust.location, shop.location)
            )

            fuel_cost_to_shop = (
                (distance_to_shop / 100) * cust.car.fuel_cons * fuel_price
            )

            product_cost = sum(
                cust.product_cart[product] * shop.products[product]
                for product in cust.product_cart)

            tr_total_cost = (
                fuel_cost_to_shop + product_cost + fuel_cost_to_shop)

            if tr_total_cost < min_cost and tr_total_cost <= cust.money:
                min_cost = tr_total_cost
                cheapest = shop

        if cheapest:
            print(
                f"{cust.name}'s trip to {cheapest.name} costs {min_cost:.2f}"
            )
            cust.location = cheapest.location

            current_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            print(f"\nDate: {current_time}")
            print(f"Thanks, {cust.name}, for your purchase!")
            print("You have bought:")
            for product, quantity in cust.product_cart.items():
                product_price = cheapest.products[product]
                pr_total_cost = product_price * quantity
                print(f"{quantity} {product}s for {pr_total_cost:.2f} dollars")
            print(f"Total cost is {min_cost:.2f} dollars")
            print("See you again!\n")

            cust.money -= min_cost
            print(f"{cust.name} rides home")
            print(f"{cust.name} now has {cust.money:.2f} dollars")
        else:
            print(
                f"{cust.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
