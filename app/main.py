import datetime
import json
from math import sqrt


def shop_trip():
    with open("config.json") as cfg:
        data = json.load(cfg)
    fuel_price = data["FUEL_PRICE"]
    customers = data["customers"]
    shops = data["shops"]
    for customer in customers:
        name = customer['name']
        money = customer['money']
        print(f"{name} has {customer['money']} dollars")
        fuel_cosum = customer["car"]["fuel_consumption"]
        location = customer["location"]
        customer_x = location[0]
        customer_y = location[1]
        lower_cost_shop = 0
        product_cart = customer["product_cart"]
        for shop in shops:
            shop_name = shop['name']
            products = shop['products']
            shop_x = shop["location"][0]
            shop_y = shop["location"][1]
            distance = sqrt(
                (shop_x - customer_x) ** 2 + (shop_y - customer_y) ** 2
            )
            cost = round((distance / 100 * fuel_cosum * fuel_price * 2), 2)
            products_cost = 0
            product_str = ""
            for product, amount in product_cart.items():
                product_cost = products[product] * amount
                product_str += f"{amount} {product}s " \
                               f"for {product_cost} dollars\n"
                products_cost += product_cost
            product_str += f"Total cost is {products_cost} dollars\n" \
                           f"See you again!\n"
            cost += products_cost
            print(f"{customer['name']}'s trip to the {shop_name} costs {cost}")
            if lower_cost_shop > cost or lower_cost_shop == 0:
                lower_cost_shop = cost
                lower_cost_shop_obj = shop
                lower_cost_shop_str = product_str
        if money < cost:
            print(f"{name} doesn't have enough money "
                  f"to make purchase in any shop")
        else:
            print(f"{customer['name']} rides to "
                  f"{lower_cost_shop_obj['name']}\n")
            print(f"Date: "
                  f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f'Thanks, {name}, for you purchase!')
            print('You have bought: ')
            print(lower_cost_shop_str)
            print(f'{name} rides home')
            print(f"{name} now has "
                  f"{round((money - lower_cost_shop), 2)} dollars\n")


if __name__ == '__main__':
    shop_trip()
