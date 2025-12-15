from app.config import load_config
from app.car import Car
from app.shop import Shop
from app.customer import Customer
from datetime import datetime


def shop_trip() -> None:
    config = load_config("config.json")
    fuel_price = config["FUEL_PRICE"]
    shops = [Shop(**shop) for shop
             in config["shops"]]
    customers = [Customer(customer["name"],
                          customer["product_cart"],
                          customer["location"],
                          customer["location"],
                          customer["money"],
                          Car(customer["car"]["brand"],
                              customer["car"]["fuel_consumption"]))
                 for customer in config["customers"]]
    for customer in customers:
        min_price = float("inf")
        best_shop = ""
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            price = customer.get_full_price(shop, fuel_price)
            print(f"{customer.name}'s trip to the {shop.name} costs {price}")

            if price < min_price:
                min_price = price
                best_shop = shop

        if not customer.can_afford_trip(best_shop, fuel_price):
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            continue

        print(f"{customer.name} rides to {best_shop.name}\n")
        customer.make_purchase(best_shop, fuel_price)
        date = (datetime(
            2021, 4, 1, 12, 33, 41
        ).strftime("%m/%d/%Y %H:%M:%S"))
        print(
            f"Date: {date}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought:"
        )

        total_price = 0
        for product_name, product_count in customer.product_cart.items():
            product_account_price = (
                product_count * best_shop.get_product_price(product_name)
            )
            total_price += product_account_price
            print(f"{product_count} {product_name}s "
                  f"for{product_account_price: .2f}".rstrip("0").rstrip(".")
                  + " dollars")

        print(f"Total cost is {total_price} dollars\nSee you again!\n")
        customer.go_back()
        print(f"{customer.name} rides home\n"
              f"{customer.name} now has {customer.money} dollars\n")


shop_trip()
