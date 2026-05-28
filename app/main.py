import json
import datetime


from app.models.car import Car
from app.models.customer import Customer
from app.models.shop import Shop
from app.utils.distance import distance


def shop_trip() -> None:
    with open("app/config.json") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]

    shops: list[Shop] = [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"],
        )
        for shop in config["shops"]
    ]

    customers: list[Customer] = []
    for customer_data in config["customers"]:
        car = Car(fuel_consumption=customer_data["car"]["fuel_consumption"])
        customer = Customer(
            name=customer_data["name"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=car,
            product_cart=customer_data["product_cart"],
        )
        customers.append(customer)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        trip_costs: list[tuple[float, Shop]] = []

        for shop in shops:
            dist_to_shop = distance(customer.location, shop.location)
            dist_home = distance(shop.location, customer.location)

            fuel_to_shop = (
                (dist_to_shop / 100)
                * customer.car.fuel_consumption
                * fuel_price
            )

            fuel_home = (
                (dist_home / 100)
                * customer.car.fuel_consumption
                * fuel_price
            )

            products_cost = sum(
                shop.products[p] * q
                for p, q in customer.product_cart.items()
                if p in shop.products
            )

            total_cost = round(fuel_to_shop + fuel_home + products_cost, 2)
            trip_costs.append((total_cost, shop))
            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {total_cost}"
            )

        cheapest_cost, cheapest_shop = min(trip_costs, key=lambda x: x[0])

        customer.location = cheapest_shop.location

        if cheapest_cost > customer.money:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            continue

        print(f"{customer.name} rides to {cheapest_shop.name}")
        print()
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {now}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total_products_cost = 0.0
        for product, qty in customer.product_cart.items():
            price = cheapest_shop.products[product] * qty
            total_products_cost += price
            price_str = int(price) if price.is_integer() else price
            print(f"{qty} {product}s for {price_str} dollars")

        print(f"Total cost is {total_products_cost} dollars")
        print("See you again!")
        print()
        print(f"{customer.name} rides home")

        remaining_money = round(customer.money - cheapest_cost, 2)
        print(f"{customer.name} now has {remaining_money} dollars")
        print()
