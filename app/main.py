import json
import datetime

from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open(
            "app/config.json",
            "rb"
    ) as datafile:
        data = json.load(datafile)

    fuel_price = data["FUEL_PRICE"]
    customers = data["customers"]
    shops = data["shops"]

    for customer in customers:
        buyer = Customer(**customer)
        buyer.car = Car(**customer["car"])
        print(f"{buyer.name} has {buyer.money} dollars")
        road_prices = {}

        for shop in shops:
            market = Shop(**shop)
            road_price = market.calc_trip_price(
                customer_location=buyer.location,
                fuel_price=fuel_price,
                fuel_consumption=buyer.car.fuel_consumption,
                customer_cart=buyer.product_cart)
            road_prices[road_price] = market
            print(f"{buyer.name}'s trip to the {market.name} "
                  f"costs {road_price}")

        min_road_price = min(road_prices.keys())

        chosen_shop = road_prices[min_road_price]
        buyer.money -= min_road_price
        if buyer.money > 0:
            print(f"{buyer.name} rides to {chosen_shop.name}\n")
        else:
            print(
                f"{buyer.name} doesn't have enough money to make "
                f"a purchase in any shop"
            )
            break

        formatted_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {formatted_date}")

        costs = {}
        for product in buyer.product_cart:
            cost = chosen_shop.calc_product_price(buyer.product_cart, product)
            costs[product] = cost
        total = sum(costs.values())

        print(f"Thanks, {buyer.name}, for your purchase!")
        print("You have bought: ")
        for product in buyer.product_cart:
            print(
                f"{buyer.product_cart[product]} {product}s for "
                f"{costs[product]} dollars"
            )
        print(f"""Total cost is {total} dollars
See you again!

{buyer.name} rides home
{buyer.name} now has {buyer.money} dollars
""")
