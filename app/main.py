import json
import datetime
from app.auto import calculate_price
from app.shop import calculate_money_for_shop, Shop
from app.customer import Customer
import os


def shop_trip() -> None:
    current_dir = os.path.dirname(__file__)
    path = os.path.join(current_dir, "config.json")
    with open(path, "r") as f:
        data = json.load(f)

    customers_data = data["customers"]
    shops_data = data["shops"]
    product_costs = calculate_money_for_shop()
    fuel_costs = calculate_price()

    shops = [Shop(s["name"], s["location"], s["products"]) for s in shops_data]

    for i, customer_data in enumerate(customers_data):
        customer = Customer(
            customer_data["name"],
            customer_data["product_cart"],
            customer_data["location"],
            customer_data["money"],
            customer_data["car"]
        )

        print(f"{customer.name} has {customer.money} dollars")
        trip_options = []

        for row in range(3):
            idx = i * 3 + row
            shop = shops[row]
            product_cost = product_costs[idx]
            fuel_cost = fuel_costs[idx]
            total = round(product_cost + fuel_cost, 2)
            trip_options.append((total, row, product_cost, fuel_cost))

            print(f"{customer.name}'s trip to the {shop.name} costs {total}")

        affordable = [option for option in trip_options if option[0]
                      <= customer.money]

        if not affordable:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            continue

        best_option = min(affordable, key=lambda x: x[0])
        total, shop_index, product_sum, fuel_sum = best_option
        shop = shops[shop_index]

        print(f"{customer.name} rides to {shop.name}")
        print("")
        now = datetime.datetime.now()
        print("Date:", now.strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        for product, amount in customer.product_cart.items():
            price = shop.products[product]
            total_price = round(price * amount, 2)
            if total_price == int(total_price):
                total_price = int(total_price)
            print(f"{amount} {product}s for {total_price} dollars")

        print(f"Total cost is {product_sum} dollars")
        print("See you again!")
        print("")
        print(f"{customer.name} rides home")
        remaining = round(customer.money - total, 2)
        print(f"{customer.name} now has {remaining} dollars\n")
