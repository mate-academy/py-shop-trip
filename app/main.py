import json
import datetime


with open("app/config.json", "r") as f:
    data = json.load(f)


def shop_trip():
    fuel_price = data["FUEL_PRICE"]
    customers = data["customers"]
    shops = data["shops"]

    result = ''
    for customer in customers:
        result += f"{customer['name']} has {customer['money']} dollars\n"
        min = customer['money']
        prods_prices = []
        total_products_cost_customers = 0
        name = ""
        for shop in shops:

            x = (shop["location"][0] - customer["location"][0]) ** 2
            y = (shop["location"][1] - customer["location"][1]) ** 2

            distance = (x + y) ** 0.5
            fuel_consumption = customer["car"]["fuel_consumption"]

            ride_cost = 2 * (fuel_price * distance * fuel_consumption / 100)

            total_products_cost = 0
            list_of_prods_prices_in_shop = []

            customer_products = [values for values in
                                 customer["product_cart"].values()]
            shop_products = [values for values in shop["products"].values()]

            for i in range(len(shop_products)):
                total_products_cost += customer_products[i] * shop_products[i]
                list_of_prods_prices_in_shop.append(shop_products[i])

            total = round(total_products_cost + ride_cost, 2)

            if total < min:
                min = total
                total_products_cost_customers = total_products_cost
                prods_prices = list_of_prods_prices_in_shop
                name = shop['name']

            result += f"{customer['name']}'s trip to " \
                      f"the {shop['name']} costs {total}\n"

        date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        if len(name) != 0:
            result += f"{customer['name']} rides to {name}\n"
            result += "\n" \
                      f"Date: {date}\n"

            milk = customer['product_cart']['milk']
            bread = customer['product_cart']['bread']
            butter = customer['product_cart']['butter']

            result += f"Thanks, {customer['name']}, for you purchase!\n" \
                      f"You have bought: \n" \
                      f"{milk} milks for {milk * prods_prices[0]} " \
                      f"dollars\n" \
                      f"{bread} breads for {bread * prods_prices[1]} " \
                      f"dollars\n" \
                      f"{butter} butters for {butter * prods_prices[2]} " \
                      f"dollars\n" \
                      f"Total cost is {total_products_cost_customers} " \
                      f"dollars\n" \
                      f"See you again!\n" \
                      f"\n"

            result += f"{customer['name']} rides home\n" \
                      f"{customer['name']} now " \
                      f"has {customer['money'] - min} dollars\n" \
                      f"\n"

        else:
            result += f"{customer['name']} doesn't have " \
                      f"enough money to make purchase in any shop"

    print(result)
