import datetime
import json


def check_shop(name, has_money, prices, shops):
    print(f"{name} has {has_money} dollars")
    for i in range(len(shops)):
        print(f"{name}'s trip to the {shops[i]} costs {prices[i]}")

    if has_money < prices[prices.index(min(prices))]:
        print(f"{name} doesn't have enough money to make purchase in any shop")
        return False

    print(f"{name} rides to {shops[prices.index(min(prices))]}\n")
    return [name, prices[prices.index(min(prices))], has_money]


def purchase_receipt(name, product, number_of_product, price):
    current = datetime.datetime.now()
    lowest_shop = price.index(min(price))
    product = product[lowest_shop]
    number_of_product = number_of_product[lowest_shop]
    print(f'Date: {current.strftime("%d/%m/%Y %H:%M:%S")}')
    print(f"Thanks, {name}, for you purchase!")
    print("You have bought: ")
    print(f"""{product[0]} milks for {number_of_product[0]} dollars
{product[1]} breads for {number_of_product[1]} dollars
{product[2]} butters for {number_of_product[2]} dollars""")
    print(f"""Total cost is {sum(number_of_product)} dollars
See you again!""")


def customer_go_home(balance):
    print(f"\n{balance[0]} rides home")
    print(f"{balance[0]} now has {balance[2] - balance[1]} dollars\n")


def shop_trip():
    with open("config.json", "r") as file:
        shopping = json.load(file)
        fuel_price = shopping["FUEL_PRICE"]
        for customer in shopping["customers"]:
            shops = []
            user = customer["name"]
            fuel_consumption = customer["car"]["fuel_consumption"]
            prices_list = []
            products_count = []
            lower_price = []

            for shop in shopping["shops"]:
                shop_price = [value for value in shop["products"].values()]
                order = [value for value in customer["product_cart"].values()]
                cost_products = [shop_price[i] * order[i] for i in range(3)]
                prices_list.append(order)
                products_count.append(cost_products)
                sum_of_products = sum(cost_products)

                user_loc = (shop["location"][0] - customer["location"][0]) ** 2
                shop_loc = (shop["location"][1] - customer["location"][1]) ** 2
                distance = (user_loc + shop_loc) ** 0.5
                consumption = (fuel_consumption / 100 * fuel_price) * 2
                transport = sum([sum_of_products, distance * consumption])
                lower_price.append(round(transport, 2))
                shops.append(shop["name"])

            money = check_shop(user, customer["money"], lower_price, shops)

            if not money:
                return

            purchase_receipt(user, prices_list, products_count, lower_price)
            customer_go_home(money)
