import json
import datetime


def shop_trip():
    with open("app/config.json", "r") as f:
        data = json.load(f)
    fuel_price = data["FUEL_PRICE"]
    customers = data["customers"]
    shops = data["shops"]
    text = ""
    for customer in customers:
        text += f"{customer['name']} has {customer['money']} dollars\n"
        cheapest_trip = []
        for shop in shops:
            diff_x = shop["location"][0] - customer["location"][0]
            diff_y = shop["location"][1] - customer["location"][1]
            distance = (diff_x ** 2 + diff_y ** 2) ** (1 / 2)
            fuel_need = customer["car"]["fuel_consumption"] / 50 * distance
            fuel_costs = fuel_need * fuel_price
            product_costs = sum(
                customer["product_cart"][key] * shop["products"][key]
                for key in shop["products"])
            total_costs = fuel_costs + product_costs
            text += f"{customer['name']}'s trip to the {shop['name']} " \
                    f"costs {round(total_costs, 2)}\n"
            if len(cheapest_trip) == 0:
                cheapest_trip = [shop["name"], total_costs, product_costs,
                                 shop["products"]["milk"],
                                 shop["products"]["bread"],
                                 shop["products"]["butter"]]
            elif total_costs < cheapest_trip[1]:
                cheapest_trip = [shop["name"], total_costs, product_costs,
                                 shop["products"]["milk"],
                                 shop["products"]["bread"],
                                 shop["products"]["butter"]]
        if customer['money'] < cheapest_trip[1]:
            text += f"{customer['name']} doesn't have " \
                    f"enough money to make purchase in any shop"
        else:
            text += f"{customer['name']} rides to {cheapest_trip[0]}\n"
            current = datetime.datetime.now()
            timestamp = current.strftime("%d/%m/%Y %H:%M:%S")
            text += f"\nDate: {timestamp}\n" \
                    f"Thanks, {customer['name']}, for you purchase!\n" \
                    f"You have bought: \n"
            i = 3
            for key in customer["product_cart"]:
                purchase_cost = \
                    customer["product_cart"][key] * cheapest_trip[i]
                text += f"{customer['product_cart'][key]} {key}s " \
                        f"for {purchase_cost} dollars\n"
                i += 1
            text += f"Total cost is {cheapest_trip[2]} dollars\n" \
                    f"See you again!\n"
            text += f"\n{customer['name']} rides home\n" \
                    f"{customer['name']} now has " \
                    f"{round(customer['money'] - cheapest_trip[1], 2)} " \
                    f"dollars\n\n"
    print(text)
