from app.shops import Shop
from app.customers import Customer
import json
import datetime


def shop_trip():

    with open("app/config.json") as json_file:
        config = json.load(json_file)

    customers = []
    shops = []
    for customer in config["customers"]:
        customers.append(
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                customer["car"]["fuel_consumption"],
            )
        )
    for shop in config["shops"]:
        shops.append(Shop(shop["name"], shop["location"], shop["products"]))

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        trip_cost = float("inf")
        chosen_shop = None
        product_cost = 0
        for shop in shops:
            x = shop.location[0] - customer.location[0]
            y = shop.location[1] - customer.location[1]
            distance = (x ** 2 + y ** 2) ** 0.5 * 2
            fuel = (customer.fuel_consumption / 100) * config["FUEL_PRICE"]
            distance_cost = distance * fuel
            total_product_cost = 0
            for product, amount in customer.products.items():
                total_product_cost += amount * shop.products[product]
            current_trip_cost = round(distance_cost + total_product_cost, 2)
            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {current_trip_cost}"
            )
            if current_trip_cost < trip_cost:
                trip_cost = current_trip_cost
                product_cost = total_product_cost
                chosen_shop = shop
        if trip_cost > customer.money:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make purchase in any shop"
            )
        else:
            customer.money -= trip_cost
            print(f"{customer.name} rides to {chosen_shop.name}\n")
            now_ = datetime.datetime.now()
            print(f"Date: {now_.strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for you purchase!")
            print("You have bought: ")
            for product, amount in customer.products.items():
                print(
                    f"{amount} {product}s for "
                    f"{amount * chosen_shop.products[product]} dollars"
                )
            print(f"Total cost is {product_cost} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money} dollars")
        if customer is not customers[-1]:
            print()


if __name__ == "__main__":
    shop_trip()
