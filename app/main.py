import json
import datetime
import os
from app.customer import Customer
from app.shop import Shop


def shop_trip():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "config.json")

    with open(file_path, "r") as f:
        data = json.load(f)

    fuel_price = data["FUEL_PRICE"]

    customers = [Customer(c["name"], c["product_cart"], c["location"], c["money"], c["car"]) for c in data["customers"]]
    shops = [Shop(s["name"], s["location"], s["products"]) for s in data["shops"]]
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        best_shop = None
        min_trip_cost = float("inf")
        for shop in shops:
            trip_cost = customer.evaluate_trip(shop, fuel_price)
            print(f"{customer.name}'s trip to the {shop.name} costs {trip_cost}")
            if trip_cost < min_trip_cost:
                min_trip_cost = trip_cost
                best_shop = shop
        if customer.money >= min_trip_cost:
            print(f"{customer.name} rides to {best_shop.name}\n")
            formatted_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"Date: {formatted_date}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            for product, quantity in customer.product_cart.items():
                product_price = best_shop.products[product]
                cost_per_product = quantity * product_price

                cost_str = int(cost_per_product) if cost_per_product.is_integer() else cost_per_product
                quantity_str = int(quantity) if isinstance(quantity, float) and quantity.is_integer() else quantity
                print(f"{quantity_str} {product}s for {cost_str} dollars")
            products_cost = best_shop.get_cart_cost(customer.product_cart)
            prod_cost_str = int(products_cost) if products_cost.is_integer() else products_cost
            print(f"Total cost is {prod_cost_str} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            customer.money = round(customer.money - min_trip_cost, 2)
            print(f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")

