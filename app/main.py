import json
import os
from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:

    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "config.json")

    with open(config_path, "r") as file:
        data = json.load(file)

    shops = []
    customers = []

    for shop_data in data["shops"]:
        shop = Shop(
            name=shop_data["name"],
            location=shop_data["location"],
            products=shop_data["products"]
        )
        shops.append(shop)

    for customer_data in data["customers"]:
        car_data = customer_data["car"]
        car = Car(
            brand=car_data["brand"],
            fuel_consumption=car_data["fuel_consumption"]
        )
        customer = Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=car
        )
        customers.append(customer)

    for index, customer in enumerate(customers):
        print(f"{customer.name} has {customer.money} dollars")

        best_price = float("inf")
        best_shop = None
        home_location = customer.location.copy()

        for shop in shops:
            distance = customer.calculate_distance(shop.location)
            fuel_cost = customer.calculate_fuel_cost(distance,
                                                     data["FUEL_PRICE"])
            cart_cost = customer.calculate_cart_cost(shop.products)

            total_cost = fuel_cost + cart_cost

            print(f"{customer.name}'s trip to the {shop.name}"
                  f" costs {total_cost:.2f}")

            if total_cost < best_price:
                best_price = total_cost
                best_shop = shop

        if customer.money < best_price:
            print(f"{customer.name} doesn't have enough"
                  f" money to make a purchase in any shop")
        else:
            print(f"{customer.name} rides to {best_shop.name}")
            customer.location = best_shop.location.copy()

            print()
            best_shop.print_receipt(customer.name, customer.product_cart)
            print()

            customer.money = round(customer.money - best_price, 2)
            customer.location = home_location
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money:.2f} dollars")

        if index < len(customers) - 1:
            print()


if __name__ == "__main__":
    shop_trip()
