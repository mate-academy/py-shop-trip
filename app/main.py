import json
import datetime


def shop_trip():
    with open('app/config.json', 'r') as json_file:
        json_data = json.load(json_file)

    fuel_price = json_data["FUEL_PRICE"]
    customers = json_data["customers"]
    shops = json_data["shops"]

    for c in customers:
        print(f"{c['name']} has {c['money']} dollars")

        c["costs"] = []
        x0 = c["location"][0]
        y0 = c["location"][1]

        for shop in shops:
            x1 = shop["location"][0]
            y1 = shop["location"][1]
            dist = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5

            # count of travel cost
            costs = dist * c["car"]["fuel_consumption"] / 100 * fuel_price * 2

            # adding product cost
            for product, amount in c["product_cart"].items():
                if product in shop["products"]:
                    costs += amount * shop["products"][product]

            costs = round(costs, 2)
            print(f"{c['name']}'s trip to the {shop['name']} costs {costs}")

            c["costs"].append(costs)

        min_cost = min(c["costs"])
        if min_cost <= c['money']:
            shop_index = c["costs"].index(min_cost)
            print(f"{c['name']} rides to {shops[shop_index]['name']}\n")
        else:
            print(f"{c['name']} doesn't have enough money "
                  f"to make purchase in any shop")
            continue

        print("Date:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {c['name']}, for you purchase!\nYou have bought: ")

        product_costs = 0
        for product, amount in c["product_cart"].items():
            product_price = shops[shop_index]['products'][product]
            product_costs += amount * product_price
            print(f"{amount} {product}s for {amount * product_price} dollars")

        print(f"Total cost is {product_costs} dollars\nSee you again!\n")
        print(f"{c['name']} rides home")
        print(f"{c['name']} now has {c['money'] - min_cost} dollars\n")
