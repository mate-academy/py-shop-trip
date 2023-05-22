import json
import datetime

from app.calculate_price import calculate_trip_price
from app.customer import Car, Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)

    fuel_price = data["FUEL_PRICE"]

    customers = [
        Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                brand=customer["car"]["brand"],
                fuel_consumption=customer["car"]["fuel_consumption"]
            )
        )
        for customer in data["customers"]
    ]
    shops = [Shop(
        name=shop["name"],
        location=shop["location"],
        products=shop["products"]) for shop in data["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        min_trip = [shops[0],
                    calculate_trip_price(customer, shops[0], fuel_price)]
        for shop in shops:
            current_trip_price = calculate_trip_price(customer, shop,
                                                      fuel_price)
            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {round(current_trip_price, 2)}")

            if current_trip_price < min_trip[1]:
                min_trip = [shop, current_trip_price]

        if customer.money < min_trip[1]:
            print(f"{customer.name} doesn't"
                  f" have enough money to make a purchase in any shop")
            break

        print(f"{customer.name} rides to {min_trip[0].name}\n")
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")

        total_cost = 0

        for product, amount in customer.product_cart.items():
            total_cost += amount * min_trip[0].products[product]
            print(
                f"{amount} {product}s for"
                f" {amount * min_trip[0].products[product]} dollars")

        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has "
              f"{round(customer.money - min_trip[1], 2)} dollars\n")
