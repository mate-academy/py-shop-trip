import json

from app.Receipt import Receipt
from app.Trip_cost import Trip

PATH = "app/config.json"


def shop_trip() -> None:
    with open(PATH, "r") as config_in:
        config = json.load(config_in)

    fuel_price = config["FUEL_PRICE"]
    shops = config["shops"]
    customers = config["customers"]

    for customer in customers:
        name = customer["name"]
        money = customer["money"]
        product_cart = customer["product_cart"]
        car = customer["car"]

        print(f"{name} has {money} dollars")

        shop_list = select_shop(
            customer, fuel_price, shops, name, money, product_cart, car
        )

        if len(shop_list) == 0:
            print(f"{name} doesn't have enough money "
                  f"to make purchase in any shop")
            continue

        shop_list.sort(key=lambda x: x[2])
        shop_name, cost_prod, total_cost, receipt = shop_list[0]
        print(f"{name} rides to {shop_name}\n")

        print(receipt)
        print(f"{name} rides home")
        print(f"{name} now has {money - total_cost} dollars\n")


def select_shop(customer, fuel_price, shops, name, money, product_cart, car):
    purchase_price = []
    for shop in shops:
        shop_name = shop["name"]
        products = shop["products"]

        trip = Trip(
            customer["location"],
            shop["location"],
            fuel_price,
            car["fuel_consumption"]
        )
        cost_trip = trip.cost()
        cost_prod = sum([products.get(key, 0) * value
                         for key, value in product_cart.items()])
        tot_cost = round(cost_prod + 2 * cost_trip, 2)

        purchase_list = {}
        for product, quantity in product_cart.items():
            price = products.get(product, 0)
            if price > 0:
                purchase_list[product] = (quantity, quantity * price)
        receipt = Receipt(name, shop_name, purchase_list, cost_prod)

        if tot_cost <= money:
            purchase_price.append(
                (shop_name, cost_prod, tot_cost, receipt)
            )
        print(f"{name}'s trip to the {shop_name} costs {tot_cost}")
    return purchase_price


shop_trip()
