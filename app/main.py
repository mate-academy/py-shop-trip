import datetime
import json
from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        source_dict = json.load(f)

    fuel_price = source_dict["FUEL_PRICE"]

    customers = [Customer(
        name=customer["name"],
        product_cart=customer["product_cart"],
        location=customer["location"],
        money=customer["money"],
        car=customer["car"]
    ) for customer in source_dict["customers"]]

    shops = [Shop(
        name=shop["name"],
        location=shop["location"],
        products=shop["products"]
    ) for shop in source_dict["shops"]]

    for customer in customers:
        car = Car(
            brand=customer.car["brand"],
            fuel_consumption=customer.car["fuel_consumption"]
        )

        print(f"{customer.name} has {customer.money} dollars")

        shop_dict = {}
        for shop in shops:
            shop_dict[shop] = car.get_total_trip_cost(
                customer, shop, fuel_price
            )
            print(f"{customer.name}'s trip to the {shop.name} costs "
                  f"{car.get_total_trip_cost(customer, shop, fuel_price)}")

        best_shop = min(shop_dict, key=shop_dict.get)
        if customer.money >= shop_dict[best_shop]:
            print(f"{customer.name} rides to {best_shop.name}")

            current_date = datetime.datetime.now()
            print(f"\nDate: {current_date.strftime('%d/%m/%Y %H:%M:%S')}\n"
                  f"Thanks, {customer.name}, for you purchase!\n"
                  f"You have bought: ")

            for product in customer.product_cart:
                number = customer.product_cart[product]
                price = number * best_shop.products[product]
                print(f"{number} {product}s for {price} dollars")
            print(f"Total cost is "
                  f"{best_shop.get_shopping_cost(customer)} dollars\n"
                  f"See you again!\n")

            total_cost = car.get_total_trip_cost(
                customer, best_shop, fuel_price
            )
            rest_on_balance = customer.money - total_cost
            print(f"{customer.name} rides home\n"
                  f"{customer.name} now has {rest_on_balance} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make purchase in any shop")
