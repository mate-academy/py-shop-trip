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
        cus = Customer(**customer)
        cus.car = Car(**customer["car"])
        print(f"{cus.name} has {cus.money} dollars")
        road_prices = {}
        for shop in shops:
            market = Shop(**shop)
            road_price = market.calculate_trip_price(
                customer_location=cus.location,
                fuel_price=fuel_price,
                fuel_consumption=cus.car.fuel_consumption,
                customer_cart=cus.product_cart
            )
            road_prices[road_price] = market
            print(f"{cus.name}'s trip to the {market.name} "
                  f"costs {road_price}")
        min_road_price = min(road_prices.keys())
        chosen = road_prices[min(road_prices.keys())]
        cus.money -= min_road_price
        if cus.money > 0:
            print(f"""{cus.name} rides to {chosen.name}
""")
        else:
            print(
                f"{cus.name} doesn't have enough money to make "
                f"a purchase in any shop"
            )
            break
        formatted_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {formatted_date}")
        costs = {}
        for product in cus.product_cart:
            cost = cus.product_cart[product] * chosen.products[product]
            if cost == int(cost):
                cost = int(cost)
            costs[product] = cost
        total = sum(costs.values())
        print(f"""Thanks, {cus.name}, for your purchase!
You have bought: \n{cus.product_cart["milk"]} milks for {costs["milk"]} dollars
{cus.product_cart["bread"]} breads for {costs["bread"]} dollars
{cus.product_cart["butter"]} butters for {costs["butter"]} dollars
Total cost is {total} dollars
See you again!

{cus.name} rides home
{cus.name} now has {cus.money} dollars
""")
