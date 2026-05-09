import json
from datetime import datetime

from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    shops = []
    customers = []

    with open("app\\config.json", "r") as file:
        json_data = json.load(file)

    fuel_price = json_data["FUEL_PRICE"]

    for shop in json_data["shops"]:
        shops.append(Shop(shop["name"], shop["location"], shop["products"]))

    for customer in json_data["customers"]:
        customers.append(
            Customer(
                customer["name"],
                customer["money"],
                customer["location"],
                customer["car"]["fuel_consumption"],
                customer["product_cart"]
            )
        )

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        temp_dict = {}
        for index, shop in enumerate(shops):
            trip_coast = (
                customer.fuel_to_shop(shop) * fuel_price * 2
                + shop.what_you_want_to_buy(customer.product_cart))
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {trip_coast:.2f}")
            temp_dict[trip_coast] = index

        total_coast, index = min(temp_dict.items())
        total_coast = round(total_coast, 2)
        shop_name = shops[index]
        if customer.money < total_coast:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            break
        print(f"{customer.name} rides to {shop_name.name}\n")
        customer.location = shop_name.location
        print("Date:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for your purchase!\nYou have bought:")
        purchase_coast = 0
        for product_name, quantity in customer.product_cart.items():
            coast = quantity * shop_name.products.get(product_name, 0)
            print(f"{quantity} {product_name}s for {coast:g} dollars")
            purchase_coast += coast
        print(f"Total cost is {purchase_coast} dollars\nSee you again!\n")
        customer.money -= total_coast
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {customer.money} dollars\n")
