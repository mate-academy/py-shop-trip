import json
from datetime import datetime
from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("/Users/olgierrd/projects/py-shop-trip/app/config.json", "rb") as datafile:
        data = json.load(datafile)
    fuel_price = data["FUEL_PRICE"]
    customers = data["customers"]
    shops = data["shops"]
    for customer in customers:
        cust = Customer(**customer)
        cust.car = Car(**customer["car"])
        print(f"{cust.name} has {cust.money} dollars")
        road_prices = {}
        for shop in shops:
            market = Shop(**shop)
            road_price = market.calculate_trip_price(
                customer_location=cust.location,
                fuel_price=fuel_price,
                fuel_consumption=cust.car.fuel_consumption,
                customer_cart=cust.product_cart
            )
            road_prices[road_price] = market
            print(f"{cust.name}'s trip to the {market.name} "
                  f"costs {road_price}")
        min_road_price = min(road_prices.keys())
        chosen = road_prices[min(road_prices.keys())]
        cust.money -= min_road_price
        if cust.money > 0:
            print(f"""{cust.name} rides to {chosen.name}
""")
        else:
            print(f"{cust.name} doesn't have enough money to make a purchase in any shop")
            break
        formatted_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {formatted_date}")
        cost_milk = cust.product_cart["milk"] * chosen.products["milk"]
        cost_bread = cust.product_cart["bread"] * chosen.products["bread"]
        cost_butter = cust.product_cart["butter"] * chosen.products["butter"]
        total = cost_milk + cost_bread + cost_butter
        print(f"""Thanks, {cust.name}, for your purchase!
You have bought: 
{cust.product_cart["milk"]} milks for {cost_milk} dollars
{cust.product_cart["bread"]} breads for {cost_bread} dollars
{cust.product_cart["butter"]} butters for {cost_butter} dollars
Total cost is {total} dollars
See you again!

{cust.name} rides home
{cust.name} now has {cust.money} dollars
""")
